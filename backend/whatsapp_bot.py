#!/usr/bin/env python3
"""
WhatsApp Medical AI Chatbot
Integrates the ML model from ml.ipynb with WhatsApp Business API
"""

import os
import json
import pickle
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import re
from llm_integration import LLMManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class MedicalChatbot:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.llm_manager = LLMManager()
        self.use_llm = os.getenv('USE_LLM', 'false').lower() == 'true'
        self.load_model()
        
    def load_model(self):
        """Load the trained ML model and vectorizer"""
        try:
            # Try to load pre-trained model
            if os.path.exists('medical_model.pkl') and os.path.exists('vectorizer.pkl'):
                with open('medical_model.pkl', 'rb') as f:
                    self.model = pickle.load(f)
                with open('vectorizer.pkl', 'rb') as f:
                    self.vectorizer = pickle.load(f)
                logger.info("Model loaded successfully")
            else:
                logger.warning("Model files not found. Please train the model first.")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
    
    def preprocess_text(self, text):
        """Clean and preprocess user input"""
        # Remove special characters and normalize
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
        text = ' '.join(text.split())  # Remove extra whitespace
        return text
    
    def get_medical_advice(self, user_message):
        """Generate medical advice based on user input"""
        
        # Try LLM first if enabled and available
        if self.use_llm and self.llm_manager.is_available():
            try:
                llm_response = self.llm_manager.generate_response(user_message)
                if llm_response:
                    logger.info("Using LLM response")
                    return llm_response
            except Exception as e:
                logger.error(f"LLM error, falling back to traditional model: {e}")
        
        # Fallback to traditional RandomForest model
        if not self.model or not self.vectorizer:
            return "I'm sorry, the medical AI is currently unavailable. Please try again later."
        
        try:
            # Preprocess the message
            processed_message = self.preprocess_text(user_message)
            
            # Vectorize the input
            message_vector = self.vectorizer.transform([processed_message])
            
            # Get prediction
            prediction = self.model.predict(message_vector)[0]
            
            # Add disclaimer to medical advice
            disclaimer = "\n\n⚠️ DISCLAIMER: This is AI-generated advice for informational purposes only. Please consult a qualified healthcare professional for proper medical diagnosis and treatment."
            
            logger.info("Using traditional RandomForest model")
            return f"{prediction}{disclaimer}"
            
        except Exception as e:
            logger.error(f"Error generating advice: {e}")
            return "I'm sorry, I couldn't process your medical query. Please try rephrasing your question."

# Initialize the chatbot
chatbot = MedicalChatbot()

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
else:
    twilio_client = None
    logger.warning("Twilio credentials not found. WhatsApp functionality will be limited.")

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    """Handle incoming WhatsApp messages"""
    try:
        # Get message data from Twilio
        incoming_msg = request.values.get('Body', '').strip()
        sender_number = request.values.get('From', '')
        
        logger.info(f"Received message from {sender_number}: {incoming_msg}")
        
        # Handle different types of messages
        if incoming_msg.lower() in ['hi', 'hello', 'start', 'help']:
            response = """🏥 Welcome to Medical AI Assistant!
            
I can help you with:
• General health questions
• Symptom analysis
• Basic medical advice
• Health tips

Please describe your symptoms or health concern, and I'll provide guidance.

⚠️ Remember: This is for informational purposes only. Always consult a healthcare professional for serious medical issues."""
        
        elif incoming_msg.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            response = "Thank you for using Medical AI Assistant. Take care of your health! 🏥"
        
        else:
            # Get medical advice from the AI model
            response = chatbot.get_medical_advice(incoming_msg)
        
        # Send response back via WhatsApp
        if twilio_client:
            message = twilio_client.messages.create(
                body=response,
                from_=TWILIO_PHONE_NUMBER,
                to=sender_number
            )
            logger.info(f"Response sent to {sender_number}")
        
        return jsonify({'status': 'success'})
        
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': chatbot.model is not None,
        'twilio_configured': twilio_client is not None
    })

@app.route('/test', methods=['POST'])
def test_chatbot():
    """Test endpoint for the chatbot without WhatsApp"""
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        response = chatbot.get_medical_advice(message)
        return jsonify({'response': response})
        
    except Exception as e:
        logger.error(f"Error in test endpoint: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)