#!/usr/bin/env python3
"""
Main entry point for the Fact Checker application
"""

import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Run the CLI
from src.cli import main

if __name__ == "__main__":
    main()
