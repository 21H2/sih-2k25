#!/bin/bash

# Complete Local Setup Script for WhatsApp Medical Chatbot

echo "🏥 Starting WhatsApp Medical Chatbot Local Setup..."

# Check if we're in the backend directory
if [ ! -f "whatsapp_bot.py" ]; then
    echo "❌ Please run this script from the backend directory"
    echo "   cd backend && ./start_local.sh"
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | grep -o '[0-9]\+\.[0-9]\+' | head -1)
echo "🐍 Python version: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

# Setup environment file
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env file..."
    cp .env.example .env
    echo ""
    echo "🔑 IMPORTANT: Edit .env file with your Twilio credentials!"
    echo "   Get them from: https://console.twilio.com"
    echo ""
    read -p "Press Enter when you've updated .env file..."
fi

# Extract ML model
echo "🤖 Extracting ML model..."
python extract_model.py

# Check if model files were created
if [ -f "medical_model.pkl" ] && [ -f "vectorizer.pkl" ]; then
    echo "✅ Model files created successfully"
else
    echo "❌ Model extraction failed"
    exit 1
fi

# Test the setup
echo "🧪 Testing the setup..."
python -c "
import os
from dotenv import load_dotenv
load_dotenv()

# Test environment variables
sid = os.getenv('TWILIO_ACCOUNT_SID')
token = os.getenv('TWILIO_AUTH_TOKEN')

if sid and sid != 'your_twilio_account_sid_here':
    print('✅ Twilio credentials configured')
else:
    print('⚠️  Please update .env with your Twilio credentials')
    print('   TWILIO_ACCOUNT_SID=your_account_sid')
    print('   TWILIO_AUTH_TOKEN=your_auth_token')

# Test model loading
try:
    import pickle
    with open('medical_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    print('✅ ML model loaded successfully')
except Exception as e:
    print(f'❌ Model loading error: {e}')
"

echo ""
echo "🚀 Starting the WhatsApp bot server..."
echo "   Server will run on: http://localhost:5000"
echo "   Health check: http://localhost:5000/health"
echo ""
echo "📱 To connect to WhatsApp:"
echo "   1. Install ngrok: brew install ngrok"
echo "   2. In another terminal: ngrok http 5000"
echo "   3. Copy the HTTPS URL from ngrok"
echo "   4. Set Twilio webhook to: https://your-ngrok-url.ngrok.io/webhook"
echo ""
echo "🎉 Starting server now..."
echo ""

# Start the Flask app
python whatsapp_bot.py