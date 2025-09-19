#!/bin/bash

# Quick Heroku Deployment Script for WhatsApp Medical Chatbot

echo "🚀 Starting deployment process..."

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found. Please install it first:"
    echo "   Mac: brew install heroku/brew/heroku"
    echo "   Or download from: https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Login to Heroku
echo "🔐 Logging into Heroku..."
heroku login

# Get app name from user
read -p "Enter your Heroku app name (e.g., my-medical-bot): " APP_NAME

if [ -z "$APP_NAME" ]; then
    echo "❌ App name cannot be empty"
    exit 1
fi

# Create Heroku app
echo "📱 Creating Heroku app: $APP_NAME"
heroku create $APP_NAME

# Set buildpack
echo "🔧 Setting Python buildpack..."
heroku buildpacks:set heroku/python --app $APP_NAME

# Get Twilio credentials
echo ""
echo "🔑 Now we need your Twilio credentials..."
echo "   Get them from: https://console.twilio.com"
echo ""

read -p "Enter your Twilio Account SID: " TWILIO_SID
read -p "Enter your Twilio Auth Token: " TWILIO_TOKEN

# Set environment variables
echo "⚙️ Setting environment variables..."
heroku config:set TWILIO_ACCOUNT_SID=$TWILIO_SID --app $APP_NAME
heroku config:set TWILIO_AUTH_TOKEN=$TWILIO_TOKEN --app $APP_NAME
heroku config:set TWILIO_PHONE_NUMBER=whatsapp:+14155238886 --app $APP_NAME

# Initialize git if needed
if [ ! -d ".git" ]; then
    echo "📝 Initializing git repository..."
    git init
fi

# Add Heroku remote
heroku git:remote -a $APP_NAME

# Prepare for deployment
echo "📦 Preparing files for deployment..."
git add .
git commit -m "Deploy WhatsApp Medical Chatbot"

# Deploy
echo "🚀 Deploying to Heroku..."
git push heroku main

# Get app URL
APP_URL="https://$APP_NAME.herokuapp.com"

echo ""
echo "✅ Deployment completed!"
echo ""
echo "📱 Your app is live at: $APP_URL"
echo ""
echo "🔧 Next steps:"
echo "1. Go to Twilio Console → WhatsApp Sandbox"
echo "2. Set webhook URL to: $APP_URL/webhook"
echo "3. Set HTTP method to: POST"
echo "4. Test by sending 'hi' to your Twilio WhatsApp number"
echo ""
echo "🧪 Test your deployment:"
echo "   curl $APP_URL/health"
echo ""

# Open browser to app
read -p "Open your app in browser? (y/n): " OPEN_BROWSER
if [ "$OPEN_BROWSER" = "y" ]; then
    heroku open --app $APP_NAME
fi

echo "🎉 All done! Your WhatsApp medical chatbot is ready!"