# Quick Start Guide

## Setup in 3 Easy Steps

### 1. Install Dependencies
```bash
cd /home/satyalakshmi/aiproj/fact-checker
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Add Your API Key
```bash
cp .env.example .env
nano .env  # or use any text editor
```

Add either:
- `OPENAI_API_KEY=sk-...` (for OpenAI)
- `ANTHROPIC_API_KEY=sk-ant-...` (for Anthropic)

### 3. Run the Fact Checker
```bash
python fact_checker.py
```

That's it! 🎉

## Getting API Keys

### OpenAI (Recommended for beginners)
1. Visit: https://platform.openai.com/api-keys
2. Sign up/Login
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Add $5-10 credits to your account

### Anthropic (Claude)
1. Visit: https://console.anthropic.com/
2. Sign up/Login
3. Go to API Keys
4. Generate a new key
5. Add credits to your account

## Example Usage

```
Enter a factual claim to verify: The Earth is flat

Verdict: ✗ FALSE
Confidence: 100%
Explanation: The Earth is an oblate spheroid, not flat. This has been proven through...
```

## Troubleshooting

**Problem:** "API key not found"
**Solution:** Make sure you created `.env` file and added your key

**Problem:** "Module not found"
**Solution:** Run `pip install -r requirements.txt`

**Problem:** Rate limit errors
**Solution:** Wait a few seconds between requests

## Need Help?

Check the full README.md for detailed documentation!
