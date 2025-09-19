#!/usr/bin/env python3
"""
Simple WhatsApp Medical Chatbot without ML dependencies
Use this if you're having trouble with pandas/scikit-learn installation
"""

import os
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class SimpleMedicalChatbot:
    def __init__(self):
        # Simple rule-based responses
        self.responses = {
            'fever': """For fever:
• Rest and stay hydrated
• Take paracetamol/acetaminophen as directed
• Monitor temperature regularly
• Seek medical help if fever >39°C (102°F) or persists >3 days

⚠️ DISCLAIMER: This is general information only. Consult a healthcare professional for proper medical advice.""",
            
            'headache': """For headaches:
• Rest in a quiet, dark room
• Apply cold/warm compress
• Stay hydrated
• Consider over-the-counter pain relief
• Avoid triggers like stress, certain foods

⚠️ DISCLAIMER: Severe or persistent headaches require medical evaluation.""",
            
            'stomach': """For stomach issues:
• Eat bland foods (rice, toast, bananas)
• Stay hydrated with small sips
• Avoid dairy, spicy, or fatty foods
• Consider probiotics
• Rest and avoid stress

⚠️ DISCLAIMER: Persistent stomach problems need medical attention.""",
            
            'cough': """For cough:
• Stay hydrated
• Use honey (for adults)
• Humidify the air
• Avoid irritants like smoke
• Rest your voice

⚠️ DISCLAIMER: Persistent cough or breathing difficulties require immediate medical care.""",
            
            'default': """I understand you're not feeling well. Here are some general health tips:

• Stay hydrated
• Get adequate rest
• Eat nutritious foods
• Monitor your symptoms
• Seek medical help if symptoms worsen

⚠️ DISCLAIMER: This is general health information. Always consult qualified healthcare professionals for proper medical diagnosis and treatment."""
        }
    
    def get_medical_advice(self, user_message):
        """Generate medical advice based on keywords"""
        message_lower = user_message.lower()
        
        # Check for keywords and return appropriate response
        if any(word in message_lower for word in ['fever', 'temperature', 'hot']):
            return self.responses['fever']
        elif any(word in message_lower for word in ['headache', 'head', 'migraine']):
            return self.responses['headache']
        elif any(word in message_lower for word in ['stomach', 'nausea', 'vomit', 'belly']):
            return self.responses['stomach']
        elif any(word in message_lower for word in ['cough', 'throat', 'cold']):
            return self.responses['cough']
        else:
            return self.responses['default']

# Initialize the chatbot
chatbot = SimpleMedicalChatbot()

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
• Symptom guidance
• Basic medical advice
• Health tips

Please describe your symptoms or health concern, and I'll provide guidance.

⚠️ Remember: This is for informational purposes only. Always consult a healthcare professional for serious medical issues."""
        
        elif incoming_msg.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            response = "Thank you for using Medical AI Assistant. Take care of your health! 🏥"
        
        else:
            # Get medical advice
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
        'bot_type': 'simple_rule_based',
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