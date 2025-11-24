# Project Explanation: Journalism Fact Verification System

## Project Structure

```
fact-checker/
├── fact_checker.py          # Main entry point
├── src/
│   ├── __init__.py         # Package initialization
│   ├── simple_model.py     # ML model training and prediction
│   ├── cli.py              # User interface
│   └── fact_checker.py     # Original API-based checker (not used)
├── requirements.txt         # Python dependencies
├── .env.example            # API key template (not needed)
├── .gitignore              # Git ignore rules
├── README.md               # User documentation
├── QUICKSTART.md           # Quick setup guide
└── venv/                   # Virtual environment (auto-generated)
```

---

## Detailed File Explanations

### **1. fact_checker.py** (Main Entry Point)
**Purpose:** This is the file you run to start the application.

**What it does:**
- Sets up the Python path so the `src` folder can be found
- Loads environment variables from `.env` file (though we don't use them anymore)
- Imports and runs the `main()` function from `src/cli.py`

**Code Flow:**
```python
1. Add project root to Python path
2. Load .env file (for API keys - not used in our case)
3. Import main() from src/cli.py
4. Execute main() to start the CLI
```

**When to use:** Run this file to start the fact checker:
```bash
python fact_checker.py
```

---

### **2. src/simple_model.py** (The Brain - ML Model)
**Purpose:** Contains the machine learning model that actually verifies facts.

**What it does:**

#### **Class: SimpleFactChecker**
- **`__init__()`:** Creates the fact checker and trains the model immediately
- **`train_model()`:** Trains the ML model on real news data
- **`verify_fact(claim)`:** Takes a claim and returns whether it's TRUE/FALSE

#### **How Training Works:**
```python
1. Load True.csv (real news articles) → Label as 1
2. Load Fake.csv (fake news articles) → Label as 0
3. Combine both datasets
4. Extract text features using TF-IDF (Term Frequency-Inverse Document Frequency)
5. Train Naive Bayes classifier
6. Model is ready to predict!
```

#### **TF-IDF Explained:**
- Converts text into numbers the model can understand
- Common words (the, a, is) get low scores
- Important unique words get high scores
- Example: "Trump" in political news gets a high score

#### **Naive Bayes Classifier:**
- Simple but effective ML algorithm
- Calculates probability that text is TRUE or FALSE
- Based on word patterns learned from training data
- Fast and works well with text

#### **Prediction Process:**
```python
Input: "Trump's son was questioned"
↓
TF-IDF converts to numbers: [0.2, 0.8, 0.1, ...]
↓
Model calculates probabilities:
  - P(TRUE) = 77%
  - P(FALSE) = 23%
↓
Output: TRUE with 77% confidence
```

#### **Dataset Used:**
- **True.csv:** ~21,417 real news articles (Reuters, verified sources)
- **Fake.csv:** ~23,481 fake news articles (propaganda, satire, false claims)
- **Total:** ~45,000 articles for training

---

### **3. src/cli.py** (User Interface)
**Purpose:** Handles all user interaction and displays results beautifully.

**What it does:**

#### **Class: FactCheckerCLI**

**`display_welcome()`**
- Shows the fancy welcome banner with box border
- Uses the `rich` library for beautiful formatting

**`setup_provider()`**
- Creates an instance of `SimpleFactChecker`
- Shows "Loading model..." message
- Trains the model (takes ~2-5 seconds)
- Shows "✓ Model loaded successfully!"

**`display_result(result, claim)`**
- Takes the model's output and makes it pretty
- Color codes the verdict:
  - 🟢 TRUE = Green
  - 🔴 FALSE = Red
  - 🔵 UNVERIFIABLE = Blue
- Shows confidence percentage
- Displays explanation and key areas

**`run()`** - Main Loop
```python
1. Display welcome message
2. Load the model
3. Loop:
   a. Ask user for a claim
   b. Send to model for verification
   c. Show beautiful results
   d. Ask if user wants to continue
4. Exit with goodbye message
```

**Libraries Used:**
- **rich:** Makes the CLI beautiful with colors, tables, panels
- **Console:** Handles colored output
- **Panel:** Creates bordered boxes
- **Table:** Organizes data in tables
- **Prompt:** Gets user input with validation

---

### **4. src/fact_checker.py** (Not Used Anymore)
**Purpose:** Originally for API-based fact checking (OpenAI, Anthropic, Gemini)

**Status:** Not used in current version

**Why not used:**
- APIs require paid keys ($$$)
- API rate limits
- Need internet connection
- Complex error handling

**Our solution:** We trained our own model instead.

---

### **5. requirements.txt**
**Purpose:** Lists all Python packages needed for the project.

**Packages:**
```
openai==1.57.0           # OpenAI API (not used, but kept)
anthropic==0.39.0        # Anthropic API (not used)
rich==13.9.4             # Beautiful CLI formatting (USED)
python-dotenv==1.0.1     # Load .env files (not needed)
google-generativeai      # Gemini API (not used)
scikit-learn             # Machine Learning library (USED)
pandas                   # Data processing (USED)
```

**Actually Used:**
- **rich:** UI/UX
- **scikit-learn:** Machine learning model
- **pandas:** Reading CSV files

---

### **6. .env.example**
**Purpose:** Template for API keys (not needed for our trained model)

**Status:** Not required for the trained model version

**Content:**
```bash
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

Since we use a trained model, you don't need any API keys.

---

### **7. README.md**
**Purpose:** User-facing documentation with setup instructions.

**Sections:**
- Features overview
- Installation steps
- API key setup (outdated)
- Usage examples
- How it works
- Troubleshooting

---

### **8. QUICKSTART.md**
**Purpose:** Fast 3-step setup guide for beginners.

**Content:**
1. Install dependencies
2. Add API key (no longer needed)
3. Run the fact checker

---

## How Everything Works Together

### **Complete Flow:**

```
┌─────────────────────────────────────────────────┐
│ User runs: python fact_checker.py              │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ fact_checker.py loads and calls:                │
│ src/cli.py → main()                            │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ cli.py creates FactCheckerCLI                   │
│ - Shows welcome banner                          │
│ - Calls setup_provider()                        │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ setup_provider() creates SimpleFactChecker      │
│ from src/simple_model.py                       │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ SimpleFactChecker.__init__() calls:            │
│ train_model()                                   │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ train_model():                                  │
│ 1. Loads True.csv (21,417 real articles)       │
│ 2. Loads Fake.csv (23,481 fake articles)       │
│ 3. Creates TF-IDF vectorizer                   │
│ 4. Trains Naive Bayes classifier               │
│ 5. Model ready! ✓                              │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ cli.py shows: ✓ Model loaded successfully!     │
│ Enters main loop                                │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ User enters claim: "Trump is president"         │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ cli.py calls:                                   │
│ fact_checker.verify_fact(claim)                │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ verify_fact():                                  │
│ 1. Converts claim to TF-IDF numbers            │
│ 2. Model predicts: TRUE/FALSE                  │
│ 3. Gets probability (confidence)                │
│ 4. Returns {verdict, confidence, explanation}   │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ cli.py calls:                                   │
│ display_result(result, claim)                  │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ Shows beautiful formatted result:               │
│ ╭─────────────────────────────────────╮        │
│ │ Verdict: ✓ TRUE                     │        │
│ │ Confidence: 85%                      │        │
│ │ Explanation: ...                     │        │
│ ╰─────────────────────────────────────╯        │
└─────────────────┬───────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────────┐
│ Ask: Check another fact? [y/n]                  │
│ If yes → loop back                              │
│ If no → Exit with goodbye message               │
└─────────────────────────────────────────────────┘
```

---

## Key Concepts

### **Machine Learning Pipeline:**
1. **Data Collection:** 45,000 real + fake news articles
2. **Feature Extraction:** TF-IDF converts text → numbers
3. **Model Training:** Naive Bayes learns patterns
4. **Prediction:** New claims classified as TRUE/FALSE
5. **Evaluation:** Confidence score based on probability

### **Why This Approach Works:**
- No API keys needed (free!)
- Works offline
- Fast predictions (<1 second)
- Good accuracy on political news
- Simple to understand and modify

### **Limitations:**
- Only knows patterns from training data
- Best for political news (that's what dataset has)
- General facts (sun rises east) not in dataset
- Doesn't access real-time information
- Can't explain reasoning like LLMs

---

## How to Run

```bash
# Navigate to project
cd /home/satyalakshmi/aiproj/fact-checker

# Activate virtual environment
source venv/bin/activate

# Run the fact checker
python fact_checker.py
```

---

## Customization Ideas

### **Improve Accuracy:**
```python
# In src/simple_model.py, change:
TfidfVectorizer(max_features=5000)  # Increase to 10000
# Or use different classifier:
from sklearn.ensemble import RandomForestClassifier
```

### **Add More Data:**
```python
# Add your own CSV files in train_model():
my_data = pd.read_csv("my_news.csv")
df = pd.concat([true_df, fake_df, my_data])
```

### **Change Confidence Threshold:**
```python
# In verify_fact():
if confidence < 70:  # Change from 65 to 70
    verdict = "UNVERIFIABLE"
```

---

## 📊 Model Performance

**Dataset Split:**
- True News: 21,417 articles (47.7%)
- Fake News: 23,481 articles (52.3%)

**Model Type:** Multinomial Naive Bayes
**Features:** 5,000 TF-IDF features
**Training Time:** ~2-5 seconds
**Prediction Time:** <0.1 seconds

**Best For:**
- Political news claims
- Trump-related claims
- Election/government news
- Media/journalism claims

**Not Great For:**
- Scientific facts
- General knowledge
- Recent events (after 2017)
- Non-political topics

---

## Learning Resources

**Machine Learning:**
- TF-IDF: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
- Naive Bayes: https://scikit-learn.org/stable/modules/naive_bayes.html

**Python Libraries:**
- scikit-learn: https://scikit-learn.org/
- pandas: https://pandas.pydata.org/
- rich: https://rich.readthedocs.io/

---

## Project Summary

**Built:**
A real AI-powered fake news detector that:
- Trains on 45,000 real articles
- Uses machine learning (not just API calls)
- Has a beautiful command-line interface
- Works completely offline and free
- Perfect for an AI project demonstration!

**Technologies Used:**
- Python 3.14
- scikit-learn (ML)
- pandas (data processing)
- rich (beautiful CLI)
- Naive Bayes classifier
- TF-IDF vectorization

**Skills Demonstrated:**
- Machine Learning
- Natural Language Processing
- Data preprocessing
- Model training & evaluation
- CLI development
- Software architecture

---

**Created by:** Satyalakshmi
**Project:** AI-Powered Journalism Fact Verification System
**Date:** November 2025
