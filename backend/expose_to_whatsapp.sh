#!/bin/bash

# Script to expose local bot to WhatsApp using ngrok

echo "🌐 Exposing your local WhatsApp bot to the internet..."

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok not found. Installing..."
    echo ""
    echo "Mac users:"
    echo "  brew install ngrok"
    echo ""
    echo "Other platforms:"
    echo "  Download from: https://ngrok.com/download"
    echo ""
    exit 1
fi

# Check if local server is running
if ! curl -s http://localhost:5000/health > /dev/null; then
    echo "❌ Local server not running on port 5000"
    echo "   Start it first: ./start_local.sh"
    exit 1
fi

echo "✅ Local server is running"
echo "🚀 Starting ngrok tunnel..."
echo ""
echo "📋 Instructions:"
echo "1. Copy the HTTPS URL that appears below"
echo "2. Go to Twilio Console → WhatsApp Sandbox"
echo "3. Set webhook URL to: https://your-url.ngrok.io/webhook"
echo "4. Set HTTP method to: POST"
echo "5. Test by sending 'hi' to +1 415 523 8886"
echo ""
echo "Press Ctrl+C to stop ngrok"
echo ""

# Start ngrok
ngrok http 5000