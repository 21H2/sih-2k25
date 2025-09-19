#!/bin/bash

# Quick fix for Python 3.13 compatibility issues

echo "🔧 Fixing Python 3.13 compatibility issues..."

# Kill the virtual environment if it exists
if [ -d "venv" ]; then
    echo "🗑️ Removing old virtual environment..."
    rm -rf venv
fi

# Create new virtual environment
echo "📦 Creating new virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip first
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install packages one by one to avoid conflicts
echo "📥 Installing core packages..."
pip install Flask==2.3.3
pip install twilio==8.10.0
pip install python-dotenv==1.0.0
pip install gunicorn==21.2.0
pip install requests==2.31.0

# Install ML packages with compatible versions
echo "🤖 Installing ML packages..."
pip install "pandas>=2.2.0"
pip install "scikit-learn>=1.3.0" 
pip install "numpy>=1.24.0"

# Install LLM packages (optional)
echo "🧠 Installing LLM packages (optional)..."
pip install "openai>=1.3.0" || echo "⚠️ OpenAI install failed (optional)"
pip install "anthropic>=0.7.0" || echo "⚠️ Anthropic install failed (optional)"

echo "✅ Dependencies installed successfully!"

# Setup environment file
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env file..."
    cp .env.example .env
    echo ""
    echo "🔑 IMPORTANT: Edit .env file with your Twilio credentials!"
    echo "   Get them from: https://console.twilio.com"
    echo ""
fi

# Extract ML model
echo "🤖 Extracting ML model..."
python extract_model.py

echo ""
echo "🎉 Setup complete! Now run:"
echo "   python whatsapp_bot.py"