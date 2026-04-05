# ai-agent-starter

Minimal Python starter project for building a simple AI agent.

## Project structure

```text
ai-agent-starter/
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── models.py
│   └── config.py
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python -m app.main
```

Type prompts in the CLI. Ask for "time" to trigger a sample tool call.
