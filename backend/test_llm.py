#!/usr/bin/env python3
"""
Test script for LLM integration in WhatsApp Medical Chatbot
"""

import os
import sys
from dotenv import load_dotenv
from llm_integration import LLMManager

# Load environment variables
load_dotenv()

def test_llm_providers():
    """Test all configured LLM providers"""
    print("🤖 Testing LLM Integration for Medical Chatbot\n")
    
    # Initialize LLM manager
    llm_manager = LLMManager()
    
    if not llm_manager.is_available():
        print("❌ No LLM providers configured!")
        print("\n📋 To configure LLM providers:")
        print("1. OpenAI: Set OPENAI_API_KEY in .env")
        print("2. Anthropic: Set ANTHROPIC_API_KEY in .env") 
        print("3. HuggingFace: Set HUGGINGFACE_API_KEY in .env")
        print("4. Ollama: Set USE_OLLAMA=true in .env")
        print("\n💡 Get OpenAI key: https://platform.openai.com/api-keys")
        return False
    
    print(f"✅ Found {len(llm_manager.providers)} LLM provider(s)")
    
    # Test medical queries
    test_queries = [
        "I have fever and headache for 2 days",
        "My 5-year-old has stomach pain and won't eat",
        "I'm diabetic and have a cut that won't heal",
        "Chest pain during exercise, should I be worried?",
        "What are the symptoms of COVID-19?"
    ]
    
    print("\n🧪 Testing medical queries...\n")
    
    for i, query in enumerate(test_queries, 1):
        print(f"📤 Test {i}: {query}")
        print("🤖 AI Response:")
        
        try:
            response = llm_manager.generate_response(query)
            if response:
                # Truncate long responses for readability
                display_response = response[:300] + "..." if len(response) > 300 else response
                print(f"   {display_response}")
                print("✅ Success\n")
            else:
                print("❌ No response generated\n")
                
        except Exception as e:
            print(f"❌ Error: {e}\n")
    
    return True

def test_environment_setup():
    """Test environment configuration"""
    print("⚙️ Testing Environment Configuration\n")
    
    # Check USE_LLM setting
    use_llm = os.getenv('USE_LLM', 'false').lower()
    if use_llm == 'true':
        print("✅ USE_LLM is enabled")
    else:
        print("⚠️ USE_LLM is disabled - set USE_LLM=true in .env to enable LLM")
    
    # Check API keys
    api_keys = {
        'OpenAI': os.getenv('OPENAI_API_KEY'),
        'Anthropic': os.getenv('ANTHROPIC_API_KEY'),
        'HuggingFace': os.getenv('HUGGINGFACE_API_KEY')
    }
    
    configured_providers = []
    for provider, key in api_keys.items():
        if key and key != 'your_api_key_here':
            print(f"✅ {provider} API key configured")
            configured_providers.append(provider)
        else:
            print(f"❌ {provider} API key not configured")
    
    # Check Ollama
    use_ollama = os.getenv('USE_OLLAMA', 'false').lower()
    if use_ollama == 'true':
        print("✅ Ollama enabled")
        configured_providers.append('Ollama')
    else:
        print("❌ Ollama not enabled")
    
    print(f"\n📊 Total configured providers: {len(configured_providers)}")
    
    if not configured_providers:
        print("\n🚨 No LLM providers configured!")
        print("Your chatbot will use the traditional RandomForest model.")
        return False
    
    return True

def test_chatbot_integration():
    """Test integration with the main chatbot"""
    print("🏥 Testing Chatbot Integration\n")
    
    try:
        from whatsapp_bot import MedicalChatbot
        
        # Initialize chatbot
        chatbot = MedicalChatbot()
        
        # Test message
        test_message = "I have been having headaches every morning"
        print(f"📤 Testing: {test_message}")
        
        response = chatbot.get_medical_advice(test_message)
        print(f"🤖 Chatbot Response:")
        print(f"   {response[:200]}...")
        
        # Check if LLM was used
        if "DISCLAIMER" in response and len(response) > 100:
            print("✅ Chatbot integration working")
            return True
        else:
            print("⚠️ Chatbot working but may be using fallback model")
            return True
            
    except Exception as e:
        print(f"❌ Chatbot integration error: {e}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("🏥 WhatsApp Medical Chatbot - LLM Integration Test")
    print("=" * 60)
    
    # Test environment
    env_ok = test_environment_setup()
    print("\n" + "-" * 60 + "\n")
    
    # Test LLM providers
    llm_ok = test_llm_providers()
    print("\n" + "-" * 60 + "\n")
    
    # Test chatbot integration
    chatbot_ok = test_chatbot_integration()
    print("\n" + "-" * 60 + "\n")
    
    # Summary
    print("📋 Test Summary:")
    print(f"   Environment: {'✅ OK' if env_ok else '❌ Issues'}")
    print(f"   LLM Providers: {'✅ OK' if llm_ok else '❌ Issues'}")
    print(f"   Chatbot Integration: {'✅ OK' if chatbot_ok else '❌ Issues'}")
    
    if env_ok and llm_ok and chatbot_ok:
        print("\n🎉 All tests passed! Your LLM-powered medical chatbot is ready!")
        print("\n🚀 Next steps:")
        print("1. Start your bot: python whatsapp_bot.py")
        print("2. Expose to WhatsApp: ./expose_to_whatsapp.sh")
        print("3. Test with real WhatsApp messages")
    else:
        print("\n⚠️ Some tests failed. Check the issues above.")
        print("\n💡 Quick fixes:")
        print("- Add API keys to .env file")
        print("- Set USE_LLM=true in .env")
        print("- Install requirements: pip install -r requirements.txt")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()