# Azure AI Essay Correction & Translation

## Overview

This project demonstrates how to use Azure AI Foundry with a deployed GPT-5.4-mini model to:

- Correct grammar, spelling, and punctuation in an essay.
- Translate the corrected essay into French.
- Access the deployed model using Python and the OpenAI SDK.

## Technologies Used

- Python
- Azure AI Foundry
- OpenAI Python SDK
- python-dotenv

## Files

- `main.py` - Main application
- `essay.txt` - Essay with grammatical errors
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (not included)

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

## Output

The program displays:

- Original essay
- Corrected essay
- French translation