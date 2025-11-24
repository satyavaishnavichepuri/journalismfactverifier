# Journalism Fact Verification System

An AI-powered command-line tool for verifying factual claims using machine learning.

## Overview

This project uses a trained Naive Bayes classifier to analyze news claims and determine whether they are likely true or false. The model is trained on a dataset of 45,000 real and fake news articles, using TF-IDF vectorization for text feature extraction.

## Features

- Real-time fact verification using trained ML model
- Beautiful CLI interface with color-coded results
- Confidence scores for each verification
- Detailed explanations with reasoning
- Works completely offline (no API keys required)
- Fast predictions (under 1 second)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Navigate to the project directory:**
```bash
cd /home/satyalakshmi/aiproj/fact-checker
```

2. **Create a virtual environment (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Ensure dataset files are present:**
   from https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets?resource=download (a kaggle dataset)
The following CSV files should be in the project root:
- `True.csv` - Real news articles (21,417 articles)
- `Fake.csv` - Fake news articles (23,481 articles)

These files are used to train the model on first run.

## Usage

### Running the Fact Checker

```bash
python fact_checker.py
```

### How to Use

1. Run the application
2. Wait for the model to load (takes 2-5 seconds on first run)
3. Enter a factual claim when prompted
4. Review the verdict, confidence score, and explanation
5. Continue checking more facts or exit

### Example Claims

The model works best with political and news-related claims:
- "Trump was the president of America"
- "Democrats opposed Republican budget plan"
- "Hillary Clinton is going to prison"
- "Trump met world leaders at the UN"

## Project Structure

```
fact-checker/
├── fact_checker.py          # Main entry point
├── src/
│   ├── __init__.py         # Package initialization
│   ├── simple_model.py     # ML model training and prediction
│   └── cli.py              # Command-line interface
├── True.csv                 # Real news dataset
├── Fake.csv                 # Fake news dataset
├── requirements.txt         # Python dependencies
└── README.md               # Documentation
```

## How It Works

### Machine Learning Pipeline

1. **Data Loading**: The model loads 45,000 labeled news articles (real and fake)
2. **Feature Extraction**: TF-IDF vectorization converts text into numerical features
3. **Training**: Naive Bayes classifier learns patterns from the training data
4. **Prediction**: New claims are vectorized and classified as TRUE or FALSE
5. **Confidence**: Probability scores are converted to confidence percentages

### Technical Details

- **Algorithm**: Multinomial Naive Bayes
- **Vectorization**: TF-IDF with 5,000 features
- **Training Data**: 21,417 real + 23,481 fake news articles
- **Training Time**: 2-5 seconds
- **Prediction Time**: <0.1 seconds per claim

### Verdict Types

- **TRUE**: The claim matches patterns of real news (confidence >65%)
- **FALSE**: The claim matches patterns of fake news (confidence >65%)
- **UNVERIFIABLE**: Low confidence (<65%) - model is uncertain

## Troubleshooting

**"Module not found" error:**
- Ensure you installed dependencies: `pip install -r requirements.txt`
- Verify your virtual environment is activated

**"File not found" error (True.csv or Fake.csv):**
- Make sure the dataset CSV files are in the project root directory
- Check file names and permissions

**Model takes long to load:**
- First run loads and trains on 45,000 articles (takes 2-5 seconds)
- This is normal and only happens once per session

## Limitations

- **Dataset Bias**: Model is trained primarily on political news (2015-2017)
- **Not Real-Time**: Cannot verify breaking news or recent events
- **Pattern-Based**: Learns patterns, not facts - may make mistakes
- **Best Domain**: Political news and journalism claims
- **Limited Context**: No access to external sources or databases

## Future Enhancements

- Web scraping for real-time source verification
- Expand training data with more diverse topics
- Add caching for verified claims
- Web interface using Flask or FastAPI
- Integration with news APIs
- Export verification reports to PDF/CSV

## Technologies Used

- **Python 3.x**: Core programming language
- **scikit-learn**: Machine learning framework
- **pandas**: Data processing and CSV handling
- **rich**: Terminal UI formatting
- **TF-IDF**: Text vectorization technique
- **Naive Bayes**: Classification algorithm

## License

Educational AI project. Free to use and modify.

## Disclaimer

This tool is for educational purposes. The model learns patterns from training data and may make mistakes. Always verify important claims through multiple authoritative sources. Use this as a starting point for fact-checking, not as a definitive source of truth.
