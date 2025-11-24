"""
Core fact checking logic using LLM APIs
"""

import os
from typing import Dict, Optional
from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai


class FactChecker:
    """Main fact checking class that uses LLM APIs to verify claims"""
    
    # API Key hardcoded for easy setup
    GEMINI_API_KEY = "AIzaSyCslulA3lGU4DXWk4_6lN_QBl0g49KimY4"
    
    def __init__(self, provider: str = "gemini"):
        """
        Initialize the fact checker with Gemini
        
        Args:
            provider: Only 'gemini' is supported
        """
        self.provider = "gemini"
        api_key = os.getenv("GEMINI_API_KEY") or self.GEMINI_API_KEY
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=api_key)
        self.model = "gemini-1.5-flash-latest"
        self.client = genai.GenerativeModel(self.model)
        
        if False:  # Disabled providers
            pass
        elif self.provider == "anthropic":
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
            self.client = Anthropic(api_key=api_key)
            self.model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
    
    def verify_fact(self, claim: str) -> Dict[str, any]:
        """
        Verify a factual claim using the configured LLM
        
        Args:
            claim: The factual claim to verify
            
        Returns:
            Dictionary containing verdict, confidence, explanation, and sources
        """
        prompt = self._build_verification_prompt(claim)
        
        try:
            if self.provider == "openai":
                response = self._query_openai(prompt)
            else:
                response = self._query_anthropic(prompt)
            
            return self._parse_response(response)
            
        except Exception as e:
            return {
                "verdict": "ERROR",
                "confidence": 0,
                "explanation": f"Error during verification: {str(e)}",
                "sources": []
            }
    
    def verify_fact(self, claim: str) -> Dict[str, any]:
        """
        Verify a factual claim using the configured LLM
        
        Args:
            claim: The factual claim to verify
            
        Returns:
            Dictionary containing verdict, confidence, explanation, and sources
        """
        prompt = self._build_verification_prompt(claim)
        
        try:
            response = self._query_gemini(prompt)
            return self._parse_response(response)
            
        except Exception as e:
            return {
                "verdict": "ERROR",
                "confidence": 0,
                "explanation": f"Error during verification: {str(e)}",
                "sources": []
            }
    
    def _build_verification_prompt(self, claim: str) -> str:
        """Build the prompt for fact verification"""
        return f"""You are a professional fact-checker for journalism. Analyze the following claim and determine its accuracy.

Claim: "{claim}"

Provide your response in the following format:

VERDICT: [TRUE/FALSE/PARTIALLY_TRUE/UNVERIFIABLE]
CONFIDENCE: [0-100]%
EXPLANATION: [Detailed explanation of why this claim is true, false, partially true, or unverifiable. Include relevant context and reasoning.]
SOURCES: [List key areas or types of information that would support this verification, separated by semicolons]

Be thorough, objective, and cite your reasoning clearly."""
    
    def _query_openai(self, prompt: str) -> str:
        """Query OpenAI API"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert fact-checker and journalist with deep knowledge across many domains."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        return response.choices[0].message.content
    
    def _query_anthropic(self, prompt: str) -> str:
        """Query Anthropic API"""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=0.3,
            system="You are an expert fact-checker and journalist with deep knowledge across many domains.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    
    def _query_gemini(self, prompt: str) -> str:
        """Query Google Gemini API"""
        full_prompt = "You are an expert fact-checker and journalist with deep knowledge across many domains.\n\n" + prompt
        response = self.client.generate_content(
            full_prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.3,
                max_output_tokens=1000,
            )
        )
        return response.text
    
    def _parse_response(self, response: str) -> Dict[str, any]:
        """Parse the LLM response into structured data"""
        lines = response.strip().split('\n')
        result = {
            "verdict": "UNVERIFIABLE",
            "confidence": 0,
            "explanation": "",
            "sources": []
        }
        
        current_section = None
        explanation_lines = []
        
        for line in lines:
            line = line.strip()
            if line.startswith("VERDICT:"):
                result["verdict"] = line.replace("VERDICT:", "").strip()
            elif line.startswith("CONFIDENCE:"):
                confidence_str = line.replace("CONFIDENCE:", "").strip().replace("%", "")
                try:
                    result["confidence"] = int(confidence_str)
                except ValueError:
                    result["confidence"] = 0
            elif line.startswith("EXPLANATION:"):
                current_section = "explanation"
                explanation_text = line.replace("EXPLANATION:", "").strip()
                if explanation_text:
                    explanation_lines.append(explanation_text)
            elif line.startswith("SOURCES:"):
                current_section = "sources"
                sources_text = line.replace("SOURCES:", "").strip()
                if sources_text:
                    result["sources"] = [s.strip() for s in sources_text.split(';') if s.strip()]
            elif current_section == "explanation" and line and not line.startswith("SOURCES:"):
                explanation_lines.append(line)
            elif current_section == "sources" and line:
                result["sources"].extend([s.strip() for s in line.split(';') if s.strip()])
        
        result["explanation"] = ' '.join(explanation_lines)
        
        return result
