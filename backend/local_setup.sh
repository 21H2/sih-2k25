#!/bin/bash

# Local Setup Script for WhatsApp Medical Chatbot

echo "🏥 Setting up WhatsApp Medical Chatbot locally..."

# Check Python version
python_version=$(python3 --version 2>&1 | grep -o '[0-9]\+\.[0-9]\+')
echo "🐍 Python version: $python_version"

# Install requirements
echo "📦 Installing requirements..."
pip3 install -r requirements.txt

# Setup environment file
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env file..."
    cp .env.example .env
    echo "✏️ Please edit .env file with your Twilio credentials"
else
    echo "✅ .env file already exists"
fi

# Extract and train model
echo "🤖 Extracting ML model..."
python3 extract_model.py

# Test the setup
echo "🧪 Testing the setup..."
python3 -c "
import pickle
import os

try:
    # Test model loading
    with open('medical_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    print('✅ Model loaded successfully')
    
    # Test environment
    from dotenv import load_dotenv
    load_dotenv()
    
    twilio_sid = os.getenv('TWILIO_ACCOUNT_SID')
    if twilio_sid and twilio_sid != 'your_twilio_account_sid_here':
        print('✅ Twilio credentials configured')
    else:
        print('⚠️ Please update .env with your Twilio credentials')
    
    print('🎉 Setup completed successfully!')
    
except Exception as e:
    print(f'❌ Setup error: {e}')
"

echo ""
echo "🚀 To start the server locally:"
echo "   python3 whatsapp_bot.py"
echo ""
echo "🌐 For WhatsApp testing, you'll need ngrok:"
echo "   brew install ngrok  # Mac"
echo "   ngrok http 5000"
echo ""
echo "📱 Then set your Twilio webhook to the ngrok URL + /webhook"