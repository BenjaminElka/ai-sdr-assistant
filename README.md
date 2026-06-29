# AI SDR Assistant

AI SDR Assistant is a portfolio project that demonstrates how generative AI can support Sales Development Representative workflows.

The app turns prospect and company details into a structured SDR package: prospect snapshot, likely pain points, lead qualification, cold email, LinkedIn message, cold call opener, follow-up sequence, and CRM note.

## Demo

Run locally with Streamlit:

```bash
streamlit run app.py
```

## Features

- Prospect and company input form
- Custom product/value proposition input
- Adjustable outreach tone and buyer stage
- AI-generated prospect snapshot
- Hypothesis-based pain points
- Lead qualification score
- Personalized cold email
- LinkedIn connection message
- Cold call opener
- Three-email follow-up sequence
- CRM-ready note
- Markdown download for generated output
- Ethical guardrails to avoid invented claims

## Tech Stack

- Python
- Streamlit
- OpenAI API
- Prompt engineering

## Project Structure

```text
ai-sdr-assistant/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-sdr-assistant.git
cd ai-sdr-assistant
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key.

Mac/Linux:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

4. Start the app:

```bash
streamlit run app.py
```

## Deployment

You can deploy this app with Streamlit Community Cloud:

1. Push this repository to GitHub.
2. Go to Streamlit Community Cloud.
3. Create a new app from the GitHub repository.
4. Set `app.py` as the entry file.
5. Add `OPENAI_API_KEY` as a secret.
6. Deploy the app and add the public link to your CV.

## CV Description

**AI SDR Assistant**  
Built an AI-powered SDR assistant using Python, Streamlit, and the OpenAI API to generate prospect snapshots, lead qualification notes, personalized cold emails, LinkedIn messages, cold call openers, follow-up sequences, and CRM-ready summaries.

## Ethical Note

This project is designed to assist sales teams with first drafts. Users should verify prospect information before sending outreach and avoid unsupported claims.
