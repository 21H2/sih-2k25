#!/usr/bin/env python3
"""
Compare Traditional RandomForest vs LLM responses
"""

import os
from dotenv import load_dotenv
from whatsapp_bot import MedicalChatbot
from llm_integration import LLMManager

load_dotenv()

def compare_responses():
    """Compare traditional vs LLM responses side by side"""
    
    print("🆚 Traditional RandomForest vs LLM Comparison\n")
    print("=" * 80)
    
    # Initialize both systems
    chatbot = MedicalChatbot()
    llm_manager = LLMManager()
    
    # Test queries
    test_queries = [
        "I have fever and headache",
        "My stomach hurts after eating",
        "I'm having chest pain during exercise",
        "My child has a rash on their arms",
        "I'm diabetic and my wound isn't healing"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n📋 Test {i}: {query}")
        print("-" * 80)
        
        # Traditional RandomForest Response
        print("🔹 TRADITIONAL MODEL (RandomForest):")
        try:
            # Temporarily disable LLM to get traditional response
            original_use_llm = chatbot.use_llm
            chatbot.use_llm = False
            
            traditional_response = chatbot.get_medical_advice(query)
            print(f"   {traditional_response[:200]}...")
            
            # Restore LLM setting
            chatbot.use_llm = original_use_llm
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        print()
        
        # LLM Response
        print("🤖 LLM MODEL (GPT/Claude):")
        try:
            if llm_manager.is_available():
                llm_response = llm_manager.generate_response(query)
                if llm_response:
                    print(f"   {llm_response[:200]}...")
                else:
                    print("   ❌ No response generated")
            else:
                print("   ❌ No LLM providers configured")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
        
        print("\n" + "=" * 80)
    
    # Summary
    print("\n📊 COMPARISON SUMMARY:")
    print("\n🔹 Traditional RandomForest:")
    print("   ✅ Fast (instant response)")
    print("   ✅ Free (no API costs)")
    print("   ✅ Reliable (always works)")
    print("   ❌ Limited responses (pre-trained only)")
    print("   ❌ No context understanding")
    print("   ❌ Can't handle complex queries")
    
    print("\n🤖 LLM (GPT/Claude):")
    print("   ✅ Intelligent (understands context)")
    print("   ✅ Dynamic responses (generates new answers)")
    print("   ✅ Handles complex medical scenarios")
    print("   ✅ Conversational (can ask follow-up questions)")
    print("   ❌ Slower (2-3 seconds)")
    print("   ❌ Costs money (~$0.01 per message)")
    print("   ❌ Requires internet/API")
    
    print("\n💡 RECOMMENDATION:")
    print("   Use HYBRID approach (current setup):")
    print("   - LLM for complex queries")
    print("   - RandomForest as fallback")
    print("   - Best of both worlds!")

if __name__ == "__main__":
    compare_responses()