#!/bin/bash

# Railway Deployment Script for WhatsApp Medical Chatbot

echo "🚂 Starting Railway deployment process..."

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Installing..."
    echo "Run: npm install -g @railway/cli"
    echo "Or visit: https://railway.app/cli"
    exit 1
fi

# Login to Railway
echo "🔐 Logging into Railway..."
railway login

# Initialize Railway project
echo "📱 Initializing Railway project..."
railway init

# Get Twilio credentials
echo ""
echo "🔑 Setting up environment variables..."
echo "   Get them from: https://console.twilio.com"
echo ""

read -p "Enter your Twilio Account SID: " TWILIO_SID
read -p "Enter your Twilio Auth Token: " TWILIO_TOKEN

# Set environment variables
echo "⚙️ Setting environment variables..."
railway variables set TWILIO_ACCOUNT_SID=$TWILIO_SID
railway variables set TWILIO_AUTH_TOKEN=$TWILIO_TOKEN
railway variables set TWILIO_PHONE_NUMBER=whatsapp:+14155238886
railway variables set PORT=8080

# Deploy
echo "🚀 Deploying to Railway..."
railway up

# Get deployment URL
echo ""
echo "✅ Deployment completed!"
echo ""
echo "🔧 Next steps:"
echo "1. Get your Railway app URL from the dashboard"
echo "2. Go to Twilio Console → WhatsApp Sandbox"
echo "3. Set webhook URL to: https://your-app.railway.app/webhook"
echo "4. Set HTTP method to: POST"
echo "5. Test by sending 'hi' to your Twilio WhatsApp number"
echo ""

echo "🎉 Your WhatsApp medical chatbot should be live on Railway!"