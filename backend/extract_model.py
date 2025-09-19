#!/usr/bin/env python3
"""
Extract and save the trained model from the Jupyter notebook
"""

import pandas as pd
import numpy as np
import pickle
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_notebook_data():
    """Load data from the notebook - you'll need to adapt this based on your data source"""
    # This is a placeholder - you'll need to replace this with your actual data loading logic
    # from your notebook. It could be from CSV, database, or other sources.
    
    # Example structure based on what I saw in your notebook output
    # You should replace this with your actual data loading code
    
    logger.info("Loading medical data...")
    
    # Placeholder data structure - replace with your actual data
    # This should match the format from your notebook
    sample_data = {
        'symptoms': [
            "fever and headache",
            "stomach pain and nausea", 
            "skin rash and itching",
            "bad breath and tooth pain",
            "back pain and stiffness"
        ],
        'advice': [
            "Most fever encountered in general practice are viral, self limiting and require only symptomatic treatment, but as compulsory routine consult a Pediatrician who will look for pallor, jaundice, neck stiffness, abdomen for liver & spleen and auscultate the chest to find the cause of the fever by evaluating the associated symptoms. bed rest with blankets. semi solid or liquid diet.",
            "children at this age mostly get loose motion due to viral infection, and if he is passing watery loose motion, then the severity does not depend on the frequency but on the amount of fluid loss /day. If baby passes urine less than 5 times a day, is drowsy & refuses feed, along with dry tongue and high fever, consult your Doctor or Pediatrician immediately.",
            "get yourself examined with relevant investigation, because appropriate treatment demands accurate diagnosis and diagnosis needs physician consultation. stay away from the sun during peak hours [11 AM to 4 PM] or ensure a good sunscreen applied on the area to limit damages.",
            "Thanks for your query, I have gone through your query. The bad breath could be because of the deposits over the teeth causing gum infection. Or it can be because of the pus discharge secondary to gum or tooth infection or any respiratory tract infection like sinusitis or gastrointestinal disorders.",
            "Hello, Thank you for using Healthcaremagic. I read your question and understood your concern. I think you may have disc problem so meet a spine surgeon get examination done followed by x ray and if nothing found get mri of whole spine to see disc and spine status."
        ]
    }
    
    return pd.DataFrame(sample_data)

def preprocess_text(text):
    """Clean and preprocess text data"""
    if pd.isna(text):
        return ""
    
    # Convert to lowercase
    text = str(text).lower()
    
    # Remove special characters but keep medical terms
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

def train_and_save_model():
    """Train the model and save it for the chatbot"""
    try:
        # Load data
        df = load_notebook_data()
        logger.info(f"Loaded {len(df)} medical records")
        
        # Preprocess the data
        df['symptoms_clean'] = df['symptoms'].apply(preprocess_text)
        df['advice_clean'] = df['advice'].apply(preprocess_text)
        
        # Prepare features and labels
        X = df['symptoms_clean'].values
        y = df['advice'].values  # Keep original advice for responses
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Create and train the vectorizer
        logger.info("Training TF-IDF vectorizer...")
        vectorizer = TfidfVectorizer(
            max_features=5000,
            stop_words='english',
            ngram_range=(1, 2),
            min_df=1,
            max_df=0.95
        )
        
        X_train_vectorized = vectorizer.fit_transform(X_train)
        X_test_vectorized = vectorizer.transform(X_test)
        
        # Train the model
        logger.info("Training RandomForest model...")
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=10,
            min_samples_split=2,
            min_samples_leaf=1
        )
        
        model.fit(X_train_vectorized, y_train)
        
        # Evaluate the model
        y_pred = model.predict(X_test_vectorized)
        accuracy = accuracy_score(y_test, y_pred)
        logger.info(f"Model accuracy: {accuracy:.4f}")
        
        # Save the model and vectorizer
        logger.info("Saving model and vectorizer...")
        
        with open('medical_model.pkl', 'wb') as f:
            pickle.dump(model, f)
        
        with open('vectorizer.pkl', 'wb') as f:
            pickle.dump(vectorizer, f)
        
        # Save model metadata
        metadata = {
            'accuracy': accuracy,
            'n_features': X_train_vectorized.shape[1],
            'n_samples': len(X_train),
            'model_type': 'RandomForestClassifier'
        }
        
        with open('model_metadata.json', 'w') as f:
            json.dump(metadata, f, indent=2)
        
        logger.info("Model and vectorizer saved successfully!")
        logger.info(f"Model metadata: {metadata}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error training model: {e}")
        return False

def test_model():
    """Test the saved model"""
    try:
        # Load the saved model
        with open('medical_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        with open('vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
        
        # Test with sample inputs
        test_symptoms = [
            "I have fever and headache",
            "My stomach hurts and I feel nauseous",
            "I have a skin rash that itches"
        ]
        
        logger.info("Testing the model...")
        for symptom in test_symptoms:
            processed = preprocess_text(symptom)
            vectorized = vectorizer.transform([processed])
            prediction = model.predict(vectorized)[0]
            
            logger.info(f"Input: {symptom}")
            logger.info(f"Prediction: {prediction[:100]}...")
            logger.info("-" * 50)
        
        return True
        
    except Exception as e:
        logger.error(f"Error testing model: {e}")
        return False

if __name__ == "__main__":
    logger.info("Starting model extraction and training...")
    
    if train_and_save_model():
        logger.info("Model training completed successfully!")
        
        if test_model():
            logger.info("Model testing completed successfully!")
        else:
            logger.error("Model testing failed!")
    else:
        logger.error("Model training failed!")