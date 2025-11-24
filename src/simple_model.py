"""
Simple fact checker using a trained model (no API needed!)
This uses a ML model trained on real news dataset
"""

import pickle
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import numpy as np


class SimpleFactChecker:
    """Simple fact checker using trained ML model"""
    
    def __init__(self):
        """Initialize and train the model"""
        self.model = None
        self.train_model()
    
    def train_model(self):
        """Train fact checking model on real news dataset"""
        try:
            # Load the real dataset
            true_df = pd.read_csv("/home/satyalakshmi/aiproj/archive/News _dataset/True.csv")
            fake_df = pd.read_csv("/home/satyalakshmi/aiproj/archive/News _dataset/Fake.csv")
            
            # Add labels
            true_df['label'] = 1  # True news
            fake_df['label'] = 0  # Fake news
            
            # Combine datasets
            df = pd.concat([true_df, fake_df], ignore_index=True)
            
            # Use title + text for better accuracy
            df['content'] = df['title'].fillna('') + ' ' + df['text'].fillna('')
            
            # Prepare data
            X = df['content'].values
            y = df['label'].values
            
            # Train the model
            self.model = Pipeline([
                ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english')),
                ('clf', MultinomialNB())
            ])
            
            self.model.fit(X, y)
            
        except Exception as e:
            # Fallback to simple training data if dataset not found
            print(f"Note: Using fallback training data ({e})")
            training_data = [
            # TRUE claims
            ("The Earth revolves around the Sun", 1),
            ("Water boils at 100 degrees Celsius at sea level", 1),
            ("The sky is blue", 1),
            ("Humans need oxygen to breathe", 1),
            ("The Moon orbits Earth", 1),
            ("Paris is the capital of France", 1),
            ("Fire is hot", 1),
            ("Ice is cold", 1),
            ("Gravity pulls objects down", 1),
            ("The sun rises in the east", 1),
            ("The sun sets in the west", 1),
            ("Plants need sunlight for photosynthesis", 1),
            ("Mount Everest is the tallest mountain on Earth", 1),
            ("The Pacific Ocean is the largest ocean", 1),
            ("Albert Einstein was a physicist", 1),
            ("DNA carries genetic information", 1),
            ("Gold is a metal", 1),
            ("Diamonds are hard", 1),
            ("Rain falls from clouds", 1),
            ("Snow is frozen water", 1),
            
            # FALSE claims
            ("The Earth is flat", 0),
            ("The sun revolves around the Earth", 0),
            ("The Moon is made of cheese", 0),
            ("Humans can breathe underwater without equipment", 0),
            ("Fire is cold", 0),
            ("The sky is green", 0),
            ("Gravity pushes objects up", 0),
            ("The sun rises in the west", 0),
            ("The sun sets in the east", 0),
            ("Plants don't need sunlight", 0),
            ("The Earth is only 6000 years old", 0),
            ("Vaccines cause autism", 0),
            ("The Great Wall of China is visible from space with naked eye", 0),
            ("Humans only use 10% of their brain", 0),
            ("Lightning never strikes the same place twice", 0),
            ("Goldfish have a 3-second memory", 0),
            ("Bulls are enraged by the color red", 0),
            ("Bats are blind", 0),
            ("Sugar makes children hyperactive", 0),
            ("We have only five senses", 0),
            ]
            
            # Split into texts and labels
            texts = [item[0] for item in training_data]
            labels = [item[1] for item in training_data]
            
            # Create and train pipeline
            self.model = Pipeline([
                ('tfidf', TfidfVectorizer(max_features=100)),
                ('clf', MultinomialNB())
            ])
            
            self.model.fit(texts, labels)
    
    def verify_fact(self, claim: str):
        """
        Verify a factual claim
        
        Args:
            claim: The factual claim to verify
            
        Returns:
            Dictionary containing verdict, confidence, and explanation
        """
        # Get prediction
        prediction = self.model.predict([claim])[0]
        
        # Get probability
        probabilities = self.model.predict_proba([claim])[0]
        confidence = int(max(probabilities) * 100)
        
        # Determine verdict
        if prediction == 1:
            verdict = "TRUE"
            explanation = "Based on the model's analysis, this claim appears to be factually accurate."
        else:
            verdict = "FALSE"
            explanation = "Based on the model's analysis, this claim appears to be false or misleading."
        
        # Check for uncertain predictions
        if confidence < 65:
            verdict = "UNVERIFIABLE"
            explanation = "The model is not confident about this claim. Further research is recommended."
        
        # Generate some reasoning
        claim_lower = claim.lower()
        keywords = {
            'earth': 'planetary facts',
            'sun': 'astronomy',
            'water': 'chemistry',
            'human': 'biology',
            'fire': 'physics',
            'sky': 'atmospheric science',
            'gravity': 'physics',
            'moon': 'astronomy',
        }
        
        sources = []
        for keyword, topic in keywords.items():
            if keyword in claim_lower:
                sources.append(topic)
        
        if not sources:
            sources = ['general knowledge', 'scientific consensus']
        
        return {
            'verdict': verdict,
            'confidence': confidence,
            'explanation': explanation,
            'sources': sources[:3]  # Limit to 3 sources
        }
