#!/usr/bin/env python3
"""
LLM Integration for WhatsApp Medical Chatbot
Supports OpenAI GPT, Anthropic Claude, and local models
"""

import os
import logging
from typing import Dict, Any, Optional
import openai
from anthropic import Anthropic
import requests
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMProvider:
    """Base class for LLM providers"""
    
    def __init__(self):
        self.medical_prompt = """You are a helpful medical AI assistant. Provide informative medical guidance while always including appropriate disclaimers.

IMPORTANT GUIDELINES:
- Always include medical disclaimers
- Encourage consulting healthcare professionals for serious symptoms
- Provide evidence-based information
- Be empathetic and supportive
- Keep responses concise for WhatsApp

DISCLAIMER TEMPLATE:
"⚠️ This is AI-generated medical information for educational purposes only. Always consult qualified healthcare professionals for proper diagnosis and treatment."
"""

    def generate_response(self, user_message: str) -> str:
        """Generate response using the LLM"""
        raise NotImplementedError

class OpenAIProvider(LLMProvider):
    """OpenAI GPT integration"""
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        super().__init__()
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        
    def generate_response(self, user_message: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.medical_prompt},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return "I'm sorry, I'm having trouble processing your request right now. Please try again later."

class AnthropicProvider(LLMProvider):
    """Anthropic Claude integration"""
    
    def __init__(self, api_key: str, model: str = "claude-3-haiku-20240307"):
        super().__init__()
        self.client = Anthropic(api_key=api_key)
        self.model = model
        
    def generate_response(self, user_message: str) -> str:
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=500,
                system=self.medical_prompt,
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )
            
            return response.content[0].text
            
        except Exception as e:
            logger.error(f"Anthropic API error: {e}")
            return "I'm sorry, I'm having trouble processing your request right now. Please try again later."

class OllamaProvider(LLMProvider):
    """Local Ollama integration (free, runs on your server)"""
    
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama2"):
        super().__init__()
        self.base_url = base_url
        self.model = model
        
    def generate_response(self, user_message: str) -> str:
        try:
            payload = {
                "model": self.model,
                "prompt": f"{self.medical_prompt}\n\nUser: {user_message}\nAssistant:",
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "max_tokens": 500
                }
            }
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()["response"]
            else:
                logger.error(f"Ollama API error: {response.status_code}")
                return "I'm sorry, I'm having trouble processing your request right now."
                
        except Exception as e:
            logger.error(f"Ollama error: {e}")
            return "I'm sorry, I'm having trouble processing your request right now. Please try again later."

class HuggingFaceProvider(LLMProvider):
    """Hugging Face API integration (free tier available)"""
    
    def __init__(self, api_key: str, model: str = "microsoft/DialoGPT-medium"):
        super().__init__()
        self.api_key = api_key
        self.model = model
        self.api_url = f"https://api-inference.huggingface.co/models/{model}"
        
    def generate_response(self, user_message: str) -> str:
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            payload = {
                "inputs": f"{self.medical_prompt}\n\nUser: {user_message}\nAssistant:",
                "parameters": {
                    "max_length": 500,
                    "temperature": 0.7,
                    "do_sample": True
                }
            }
            
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get("generated_text", "").split("Assistant:")[-1].strip()
                return "I'm sorry, I couldn't generate a proper response."
            else:
                logger.error(f"HuggingFace API error: {response.status_code}")
                return "I'm sorry, I'm having trouble processing your request right now."
                
        except Exception as e:
            logger.error(f"HuggingFace error: {e}")
            return "I'm sorry, I'm having trouble processing your request right now. Please try again later."

class LLMManager:
    """Manages multiple LLM providers with fallback"""
    
    def __init__(self):
        self.providers = []
        self.current_provider = None
        self.setup_providers()
        
    def setup_providers(self):
        """Setup available LLM providers based on environment variables"""
        
        # OpenAI GPT
        openai_key = os.getenv('OPENAI_API_KEY')
        if openai_key:
            self.providers.append(OpenAIProvider(openai_key))
            logger.info("OpenAI provider configured")
            
        # Anthropic Claude
        anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        if anthropic_key:
            self.providers.append(AnthropicProvider(anthropic_key))
            logger.info("Anthropic provider configured")
            
        # Hugging Face (free tier)
        hf_key = os.getenv('HUGGINGFACE_API_KEY')
        if hf_key:
            self.providers.append(HuggingFaceProvider(hf_key))
            logger.info("HuggingFace provider configured")
            
        # Local Ollama (free, runs locally)
        if os.getenv('USE_OLLAMA', 'false').lower() == 'true':
            self.providers.append(OllamaProvider())
            logger.info("Ollama provider configured")
            
        if self.providers:
            self.current_provider = self.providers[0]
            logger.info(f"Using {type(self.current_provider).__name__} as primary provider")
        else:
            logger.warning("No LLM providers configured")
    
    def generate_response(self, user_message: str) -> Optional[str]:
        """Generate response with fallback to other providers"""
        if not self.providers:
            return None
            
        for provider in self.providers:
            try:
                response = provider.generate_response(user_message)
                if response and "I'm sorry" not in response:
                    return response
            except Exception as e:
                logger.error(f"Provider {type(provider).__name__} failed: {e}")
                continue
                
        return None
    
    def is_available(self) -> bool:
        """Check if any LLM provider is available"""
        return len(self.providers) > 0

# Example usage
if __name__ == "__main__":
    # Test the LLM integration
    llm_manager = LLMManager()
    
    if llm_manager.is_available():
        test_message = "I have fever and headache for 2 days"
        response = llm_manager.generate_response(test_message)
        print(f"User: {test_message}")
        print(f"AI: {response}")
    else:
        print("No LLM providers configured. Please set API keys in environment variables.")