# ai-agent-starter

Minimal Python starter project for building a simple AI agent.

## Project structure

```text
ai-agent-starter/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── models.py
│   └── config.py
├── tests/
│   └── test_agent.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> `requirements.txt` is intentionally empty of third-party packages for this scaffold.

## Run

```bash
python -m app.main
```

Type prompts in the CLI. Ask for `time` to trigger a sample tool call.

## Test

```bash
python -m unittest discover -s tests -v
```
