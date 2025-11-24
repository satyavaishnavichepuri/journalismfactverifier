# 🔍 Journalism Fact Verification System

An AI-powered command-line tool for verifying factual claims using advanced language models (OpenAI GPT or Anthropic Claude).

## Features

- ✅ **Real-time fact verification** using state-of-the-art LLMs
- 🎨 **Beautiful CLI interface** with color-coded results
- 🔄 **Multiple LLM providers** (OpenAI GPT-4 or Anthropic Claude)
- 📊 **Confidence scores** for each verification
- 📝 **Detailed explanations** with reasoning
- 🔍 **Source suggestions** for further investigation

## Installation

### Prerequisites

- Python 3.8 or higher
- An API key from either OpenAI or Anthropic

### Quick Setup

1. **Clone or navigate to the project directory:**
```bash
cd /home/satyalakshmi/aiproj/fact-checker
```

2. **Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up your API key:**
```bash
cp .env.example .env
```

Then edit `.env` and add your API key:
- For OpenAI: Add your `OPENAI_API_KEY`
- For Anthropic: Add your `ANTHROPIC_API_KEY`

You only need ONE API key (choose your preferred provider).

### Getting API Keys

**OpenAI (GPT):**
1. Go to https://platform.openai.com/api-keys
2. Create an account or sign in
3. Generate a new API key
4. Add credits to your account (pay-as-you-go)

**Anthropic (Claude):**
1. Go to https://console.anthropic.com/
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key
5. Add credits to your account

## Usage

### Running the Fact Checker

Simply run:
```bash
python fact_checker.py
```

Or make it executable:
```bash
chmod +x fact_checker.py
./fact_checker.py
```

### How to Use

1. **Start the application** - Run the command above
2. **Choose your LLM provider** - Select OpenAI or Anthropic
3. **Enter a factual claim** - Type any claim you want to verify
4. **Review the results** - See the verdict, confidence score, and explanation
5. **Continue or exit** - Check more facts or quit the application

### Example Claims to Test

Try these examples:
- "The Great Wall of China is visible from space"
- "Water boils at 100 degrees Celsius at sea level"
- "Albert Einstein won the Nobel Prize in Physics"
- "Humans use only 10% of their brain"
- "Mount Everest is the tallest mountain on Earth"

## Project Structure

```
fact-checker/
├── fact_checker.py          # Main entry point (run this!)
├── src/
│   ├── __init__.py         # Package initialization
│   ├── fact_checker.py     # Core verification logic
│   └── cli.py              # Command-line interface
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Your API keys (create this)
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## How It Works

1. **User Input**: You enter a factual claim through the CLI
2. **LLM Processing**: The claim is sent to your chosen LLM (OpenAI or Anthropic)
3. **Analysis**: The LLM analyzes the claim's accuracy using its knowledge base
4. **Results**: You get:
   - **Verdict**: TRUE, FALSE, PARTIALLY_TRUE, or UNVERIFIABLE
   - **Confidence**: 0-100% confidence score
   - **Explanation**: Detailed reasoning
   - **Sources**: Key areas for further research

## Verdicts Explained

- 🟢 **TRUE**: The claim is factually accurate
- 🔴 **FALSE**: The claim is demonstrably false
- 🟡 **PARTIALLY_TRUE**: The claim has some truth but is misleading or incomplete
- 🔵 **UNVERIFIABLE**: Cannot be verified with available information

## Configuration

You can customize the LLM models in your `.env` file:

```env
# For OpenAI
OPENAI_MODEL=gpt-4o-mini  # or gpt-4, gpt-4-turbo

# For Anthropic
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022  # or other Claude models
```

## Troubleshooting

**"API key not found" error:**
- Make sure you created the `.env` file from `.env.example`
- Verify your API key is correctly pasted (no extra spaces)
- Check that your virtual environment is activated

**"Module not found" error:**
- Ensure you installed dependencies: `pip install -r requirements.txt`
- Verify your virtual environment is activated

**API rate limits:**
- OpenAI/Anthropic have rate limits for free/low-tier accounts
- Wait a few moments between requests if you hit limits
- Consider upgrading your API plan for higher limits

## Cost Considerations

- Both OpenAI and Anthropic charge per token (input + output)
- GPT-4o-mini: ~$0.15 per 1M input tokens, ~$0.60 per 1M output tokens
- Claude Sonnet: ~$3 per 1M input tokens, ~$15 per 1M output tokens
- Each fact check costs approximately $0.001-0.01 depending on complexity
- Monitor your usage in your provider's dashboard

## Future Enhancements

Potential improvements for your AI project:
- 📰 Web scraping for real-time source verification
- 💾 Local database to cache verified claims
- 📊 Statistics dashboard for verification history
- 🌐 Web interface using Flask or FastAPI
- 🔗 Integration with news APIs for context
- 📱 Mobile app version

## License

This is an educational AI project. Use responsibly and verify critical information through multiple sources.

## Contributing

This is a personal AI project, but feel free to:
- Report bugs or issues
- Suggest improvements
- Fork and customize for your needs

## Disclaimer

This tool uses AI models for educational purposes. While LLMs are knowledgeable, they can make mistakes. Always:
- Cross-reference important facts with authoritative sources
- Use this as a starting point for fact-checking, not the final word
- Be aware of the limitations of AI-generated information

---

**Built with ❤️ for journalism and truth-seeking**
