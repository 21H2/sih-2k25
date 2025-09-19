#!/bin/bash

# Test script for local WhatsApp bot

echo "🧪 Testing your local WhatsApp bot..."

# Test if server is running
echo "1. Testing server health..."
if curl -s http://localhost:5000/health > /dev/null; then
    echo "✅ Server is running"
    curl -s http://localhost:5000/health | python3 -m json.tool
else
    echo "❌ Server not running. Start it with: ./start_local.sh"
    exit 1
fi

echo ""
echo "2. Testing chatbot functionality..."

# Test chatbot with sample messages
test_messages=("hi" "I have fever and headache" "My stomach hurts" "bye")

for message in "${test_messages[@]}"; do
    echo "📤 Testing: '$message'"
    response=$(curl -s -X POST http://localhost:5000/test \
        -H "Content-Type: application/json" \
        -d "{\"message\": \"$message\"}")
    
    if [ $? -eq 0 ]; then
        echo "📥 Response: $(echo $response | python3 -c "import sys, json; print(json.load(sys.stdin)['response'][:100] + '...')")"
    else
        echo "❌ Request failed"
    fi
    echo ""
done

echo "3. Testing model files..."
if [ -f "medical_model.pkl" ] && [ -f "vectorizer.pkl" ]; then
    echo "✅ Model files exist"
    echo "   medical_model.pkl: $(ls -lh medical_model.pkl | awk '{print $5}')"
    echo "   vectorizer.pkl: $(ls -lh vectorizer.pkl | awk '{print $5}')"
else
    echo "❌ Model files missing. Run: python extract_model.py"
fi

echo ""
echo "4. Testing environment variables..."
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()

sid = os.getenv('TWILIO_ACCOUNT_SID')
token = os.getenv('TWILIO_AUTH_TOKEN')
phone = os.getenv('TWILIO_PHONE_NUMBER')

if sid and sid != 'your_twilio_account_sid_here':
    print('✅ TWILIO_ACCOUNT_SID configured')
else:
    print('❌ TWILIO_ACCOUNT_SID not configured')

if token and token != 'your_twilio_auth_token_here':
    print('✅ TWILIO_AUTH_TOKEN configured')
else:
    print('❌ TWILIO_AUTH_TOKEN not configured')

if phone:
    print(f'✅ TWILIO_PHONE_NUMBER: {phone}')
else:
    print('❌ TWILIO_PHONE_NUMBER not configured')
"

echo ""
echo "🎉 Local testing complete!"
echo ""
echo "📱 To connect to WhatsApp:"
echo "   1. Run: ./expose_to_whatsapp.sh"
echo "   2. Copy the ngrok HTTPS URL"
echo "   3. Set Twilio webhook to: https://your-url.ngrok.io/webhook"
echo "   4. Test by messaging +1 415 523 8886"