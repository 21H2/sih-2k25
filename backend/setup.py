#!/usr/bin/env python3
"""
Setup script for WhatsApp Medical Chatbot
"""

import os
import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def install_requirements():
    """Install required Python packages"""
    try:
        logger.info("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        logger.info("Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to install requirements: {e}")
        return False

def setup_environment():
    """Setup environment variables"""
    if not os.path.exists('.env'):
        logger.info("Creating .env file from template...")
        with open('.env.example', 'r') as template:
            content = template.read()
        
        with open('.env', 'w') as env_file:
            env_file.write(content)
        
        logger.info("Created .env file. Please update it with your Twilio credentials.")
    else:
        logger.info(".env file already exists.")

def extract_model():
    """Extract and train the model"""
    try:
        logger.info("Extracting and training the model...")
        subprocess.check_call([sys.executable, "extract_model.py"])
        logger.info("Model extraction completed!")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to extract model: {e}")
        return False

def main():
    """Main setup function"""
    logger.info("Setting up WhatsApp Medical Chatbot...")
    
    # Install requirements
    if not install_requirements():
        logger.error("Setup failed at requirements installation.")
        return False
    
    # Setup environment
    setup_environment()
    
    # Extract model
    if not extract_model():
        logger.error("Setup failed at model extraction.")
        return False
    
    logger.info("Setup completed successfully!")
    logger.info("\nNext steps:")
    logger.info("1. Update .env file with your Twilio credentials")
    logger.info("2. Run: python whatsapp_bot.py")
    logger.info("3. Set up ngrok for webhook URL (for development)")
    logger.info("4. Configure Twilio webhook URL")
    
    return True

if __name__ == "__main__":
    main()