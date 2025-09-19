#!/usr/bin/env python3
"""
Test script for the WhatsApp Medical Chatbot
"""

import requests
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_health_endpoint():
    """Test the health check endpoint"""
    try:
        response = requests.get('http://localhost:5000/health')
        if response.status_code == 200:
            data = response.json()
            logger.info("Health check passed!")
            logger.info(f"Status: {data['status']}")
            logger.info(f"Model loaded: {data['model_loaded']}")
            logger.info(f"Twilio configured: {data['twilio_configured']}")
            return True
        else:
            logger.error(f"Health check failed with status: {response.status_code}")
            return False
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return False

def test_chatbot_endpoint():
    """Test the chatbot functionality"""
    test_messages = [
        "Hi",
        "I have fever and headache",
        "My stomach hurts",
        "I have a skin rash",
        "Bye"
    ]
    
    try:
        for message in test_messages:
            logger.info(f"Testing message: '{message}'")
            
            response = requests.post(
                'http://localhost:5000/test',
                json={'message': message},
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                data = response.json()
                logger.info(f"Response: {data['response'][:100]}...")
                logger.info("-" * 50)
            else:
                logger.error(f"Test failed for message '{message}': {response.status_code}")
                logger.error(f"Error: {response.text}")
                return False
        
        logger.info("All chatbot tests passed!")
        return True
        
    except Exception as e:
        logger.error(f"Chatbot test error: {e}")
        return False

def main():
    """Run all tests"""
    logger.info("Starting chatbot tests...")
    
    # Test health endpoint
    if not test_health_endpoint():
        logger.error("Health check failed. Make sure the server is running.")
        return False
    
    # Test chatbot functionality
    if not test_chatbot_endpoint():
        logger.error("Chatbot tests failed.")
        return False
    
    logger.info("All tests passed! Your chatbot is working correctly.")
    return True

if __name__ == "__main__":
    main()