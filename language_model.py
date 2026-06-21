"""
Language Model interface for conversational AI with YarnGPT integration
"""

import os
from typing import Optional, List, Dict
from openai import OpenAI
import openai
from config import (
    OPENAI_API_CONFIG, 
    SYSTEM_PROMPTS, 
    SUPPORTED_LANGUAGES,
    YARNGPT_CONFIG,
    CULTURAL_PREAMBLES
)


class LanguageModel:
    """Interface with OpenAI GPT models using YarnGPT techniques"""
    
    def __init__(self, api_key: Optional[str] = None, enable_yarngpt: bool = True):
        """
        Initialize language model
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            enable_yarngpt: Enable YarnGPT-style prompt engineering
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "OpenAI API key not found. "
                "Please set OPENAI_API_KEY environment variable or pass it as argument."
            )
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = OPENAI_API_CONFIG["model"]
        self.enable_yarngpt = enable_yarngpt and YARNGPT_CONFIG.get("enabled", True)
        self.conversation_history = {}  # Per-language conversation history
        
        print(f"✓ OpenAI API initialized with model: {self.model}")
        if self.enable_yarngpt:
            print(f"✓ YarnGPT-style prompt engineering enabled")
    
    def _build_message_context(self, user_input: str, language: str) -> List[Dict]:
        """
        Build message context with conversation history using YarnGPT principles
        
        Args:
            user_input: Current user input
            language: Language code
            
        Returns:
            List of message dictionaries for API
        """
        if language not in self.conversation_history:
            self.conversation_history[language] = []
        
        messages = []
        
        # Add system prompt with cultural context
        system_prompt = SYSTEM_PROMPTS.get(language, SYSTEM_PROMPTS["yoruba"])
        if self.enable_yarngpt:
            yarngpt_enhancement = self._get_yarngpt_enhancement(language)
            system_prompt = f"{system_prompt}\n\n{yarngpt_enhancement}"
        
        messages.append({"role": "system", "content": system_prompt})
        
        # Add conversation history (limited by config)
        history_limit = YARNGPT_CONFIG.get("conversation_memory_limit", 10)
        recent_history = self.conversation_history[language][-history_limit:]
        
        for msg in recent_history:
            messages.append(msg)
        
        # Add current user input
        messages.append({"role": "user", "content": user_input})
        
        return messages
    
    def _get_yarngpt_enhancement(self, language: str) -> str:
        """
        Get YarnGPT-style enhancement for better context awareness
        
        Args:
            language: Language code
            
        Returns:
            Enhancement prompt
        """
        enhancements = {
            "yoruba": """Cultural Context Awareness:
- Greet using Yoruba traditions
- Understand Yoruba proverbs and idioms
- Respect age, titles, and social hierarchy
- Use "E" as respectful form
- Include cultural references where appropriate""",
            
            "hausa": """Cultural Context Awareness:
- Greet using Hausa traditions
- Understand Islamic greetings and context (prevalent in Hausa culture)
- Respect social hierarchy and titles
- Include cultural references where appropriate
- Be aware of Hausa business and trading traditions""",
            
            "igbo": """Cultural Context Awareness:
- Greet using Igbo traditions
- Understand Igbo Ubuntu philosophy
- Value community and family in responses
- Include cultural references where appropriate
- Be aware of Igbo entrepreneurial spirit
- Respect elder wisdom"""
        }
        return enhancements.get(language, enhancements["yoruba"])
    
    def generate_response(self, user_input: str, language: str = "yoruba") -> str:
        """
        Generate response using GPT with YarnGPT techniques
        
        Args:
            user_input: User's input text
            language: Language code (yoruba, hausa, igbo)
            
        Returns:
            Generated response
        """
        try:
            if language not in SUPPORTED_LANGUAGES:
                raise ValueError(f"Unsupported language: {language}")
            
            lang_name = SUPPORTED_LANGUAGES[language]["display_name"]
            
            print(f"\n🤖 Generating response in {lang_name} (YarnGPT-enhanced)..." if self.enable_yarngpt else f"\n🤖 Generating response in {lang_name}...")
            
            # Build message context with conversation history
            messages = self._build_message_context(user_input, language)
            
            # Select temperature based on YarnGPT config
            temperature = YARNGPT_CONFIG.get("temperature_for_creativity", 0.7)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=OPENAI_API_CONFIG["max_tokens"]
            )
            
            # Extract response text
            generated_text = response.choices[0].message.content.strip()
            
            # Store in conversation history
            if language not in self.conversation_history:
                self.conversation_history[language] = []
            
            self.conversation_history[language].append({
                "role": "user",
                "content": user_input
            })
            self.conversation_history[language].append({
                "role": "assistant",
                "content": generated_text
            })
            
            print(f"✓ Response generated: {generated_text}")
            
            return generated_text
        
        except openai.AuthenticationError:
            print("❌ Authentication failed. Please check your OpenAI API key.")
            raise
        except openai.RateLimitError:
            print("❌ Rate limit reached. Please wait before trying again.")
            raise
        except Exception as e:
            print(f"❌ Error generating response: {e}")
            raise
    
    def clear_history(self, language: Optional[str] = None):
        """
        Clear conversation history
        
        Args:
            language: Language to clear history for (None = all)
        """
        if language:
            if language in self.conversation_history:
                self.conversation_history[language] = []
                print(f"✓ History cleared for {language}")
        else:
            self.conversation_history = {}
            print("✓ All conversation history cleared")
    
    
    def set_model(self, model_name: str):
        """
        Change the model being used
        
        Args:
            model_name: Model name (gpt-3.5-turbo, gpt-4, etc.)
        """
        self.model = model_name
        print(f"✓ Model changed to: {model_name}")


class YarnGPTStyle:
    """Enhanced prompting using YarnGPT-style techniques"""
    
    @staticmethod
    def create_context_prompt(language: str, context: str, cultural_background: str = "") -> str:
        """
        Create context-aware prompt in YarnGPT style
        
        Args:
            language: Language code
            context: Context information
            cultural_background: Optional cultural background for enhanced context
            
        Returns:
            Enhanced prompt
        """
        templates = {
            "yoruba": f"""Báwo ni? 
Context: {context}
{f"Cultural Background: {cultural_background}" if cultural_background else ""}

Jówó alwada lailai nípa àsìkò yìí:""",
            
            "hausa": f"""Sannu! 
Context: {context}
{f"Cultural Background: {cultural_background}" if cultural_background else ""}

Jiya na gida game da abin yau:""",
            
            "igbo": f"""Kedu? 
Context: {context}
{f"Cultural Background: {cultural_background}" if cultural_background else ""}

Biko nyere m aziza mma banyere ube a na-ekwu:"""
        }
        
        return templates.get(language, templates["yoruba"])
    
    @staticmethod
    def enhance_user_input(user_input: str, language: str, add_cultural_context: bool = True) -> str:
        """
        Enhance user input with cultural context (YarnGPT technique)
        
        Args:
            user_input: Raw user input
            language: Language code
            add_cultural_context: Whether to add cultural context
            
        Returns:
            Enhanced input with context
        """
        if not add_cultural_context:
            return user_input
        
        cultural_contexts = {
            "yoruba": "In Yoruba tradition, ",
            "hausa": "In Hausa tradition, ",
            "igbo": "In Igbo tradition, "
        }
        
        prefix = cultural_contexts.get(language, "")
        return user_input  # Return as is for now - enhancement happens in system prompt
    
    @staticmethod
    def build_multi_turn_memory(language: str, conversation_history: List[Dict]) -> str:
        """
        Build memory context from multi-turn conversation
        
        Args:
            language: Language code
            conversation_history: List of previous messages
            
        Returns:
            Memory context string
        """
        if not conversation_history:
            return ""
        
        memory_intro = {
            "yoruba": "Ìròyìn tó ti wáyé tẹ́lẹ̀:",
            "hausa": "Abin da muka sani:",
            "igbo": "Ihe mụ maara tupu ụta:"
        }
        
        context = memory_intro.get(language, "Previous context:")
        
        # Build summary of last few exchanges
        recent = conversation_history[-6:]  # Last 3 exchanges
        for msg in recent:
            role_prefix = "👤:" if msg["role"] == "user" else "🤖:"
            context += f"\n{role_prefix} {msg['content'][:100]}..."
        
        return context
    
    @staticmethod
    def create_fallback_response(language: str, error_type: str = "general") -> str:
        """
        Create culturally appropriate fallback responses
        
        Args:
            language: Language code
            error_type: Type of error
            
        Returns:
            Fallback response in target language
        """
        responses = {
            "yoruba": {
                "general": "Mo sọ̀rọ̀ pé mo ní iṣoro. Jówó ṣe ewu ni.",
                "network": "Àsopọ̀ internet náà kò ṣiṣẹ́ dáadáa.",
                "timeout": "A gidigidi lójú akókò. Jówó ṣe ewu ni."
            },
            "hausa": {
                "general": "Gamda na shakare. Jiya na gida.",
                "network": "Sadarwar internet ba ta aiki da kyau.",
                "timeout": "An jere tsada. Jiya na gida."
            },
            "igbo": {
                "general": "M wụsuru mma. Biko onemore.",
                "network": "Internet n'uzo adịghị mma.",
                "timeout": "Abanye ohere ụtụ. Biko onemore."
            }
        }
        
        lang_responses = responses.get(language, responses["yoruba"])
        return lang_responses.get(error_type, lang_responses["general"])
