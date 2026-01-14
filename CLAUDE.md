# Email Sorter

## Overview
An intelligent email sorting application that uses OpenAI GPT-4o-mini to classify emails and ElevenLabs for voice summaries.

## Architecture

```
email_sorter/
├── config/
│   └── config.py          # Environment variable loading
├── emailer/
│   ├── client.py          # EmailClient class (IMAP operations)
│   └── email_utils.py     # Email parsing & decoding utilities
├── LLM/
│   ├── LLM.py             # OpenAI API wrapper (gpt-4o-mini)
│   └── prompt.md          # Classification prompt template
├── voice/
│   └── voice.py           # ElevenLabs text-to-speech
├── tests/
│   └── voice_test.py      # Voice service tests
├── main.py                # Application entry point
└── requirements.txt       # Python dependencies
```

## Key Components

### config/config.py - Configuration
Loads environment variables via python-dotenv:
- `EMAIL_HOST`, `EMAIL_USER`, `EMAIL_PASSWORD`, `EMAIL_ADDRESS`
- `OPENAI_API_KEY`
- `ELEVENLABS_API_KEY`

### emailer/client.py - Email Client
- `EmailClient` class using IMAPClient
- Methods: `fetch_emails()`, `file_email()`, `mark_as_read()`
- Folders: Newsletters, Personal, Receipts, Adverts

### LLM/LLM.py - Classification
- Uses OpenAI gpt-4o-mini model
- Classifies emails into categories
- Generates summaries for newsletters and personal emails

### voice/voice.py - Voice Synthesis
- ElevenLabs API integration
- Streams audio summary to user

## Main Workflow (main.py)
1. Initialize EmailClient with IMAP credentials
2. Fetch emails from INBOX
3. Parse & convert emails to dictionary format
4. Send to LLM for classification
5. File emails into appropriate folders
6. Summarize newsletters and personal emails
7. Generate audio summary via ElevenLabs
8. Stream audio to user

## Secrets Management
- All secrets in `.env` file (gitignored)
- Required variables:
  - `EMAIL_HOST`, `EMAIL_USER`, `EMAIL_PASSWORD`, `EMAIL_ADDRESS`
  - `OPENAI_API_KEY`
  - `ELEVENLABS_API_KEY`

## Running
```bash
# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

## Dependencies
- `IMAPClient==3.0.1` - IMAP server communication
- `openai==1.37.0` - OpenAI API client
- `elevenlabs==1.5.0` - ElevenLabs TTS
- `beautifulsoup4==4.12.3` - HTML parsing
- `python-dotenv==1.0.1` - Environment variable management
- `pydantic==2.8.2` - Data validation
