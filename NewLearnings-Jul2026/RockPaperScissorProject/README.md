# Hand Game Arena

A same-device, two-player Rock Paper Scissors game built with React, JavaScript, CSS, FastAPI, and Python. Players can choose with buttons or the browser's speech-recognition feature. Each move stays hidden after it is locked until both players are ready.

## Features

- Two private, independently locked player choices
- Voice selection for both players (say “rock”, “paper”, or “scissors”)
- FastAPI endpoint that validates choices and decides every round
- Score tracking for Player 1, Player 2, and ties
- Responsive and keyboard-friendly interface
- Automated backend tests for every possible outcome

## Run locally

You need Node.js 18+ and Python 3.10+.

### 1. Start the backend

From this project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
```

The API is available at `http://localhost:8000`. Interactive API docs are at `http://localhost:8000/docs`.

### 2. Start the frontend

In a second terminal, from this project directory:

```bash
npm install
npm run dev
```

Open `http://localhost:5173`.

## Voice mode

Use Chrome or Edge for the broadest Web Speech API support. Click **Say your move**, allow microphone access, and say one of the three moves. Voice recognition generally needs `localhost` or an HTTPS deployment. If it is unavailable, all button controls continue to work.

The recognized move is selected but is not locked automatically, so each player can confirm that the browser heard the intended word before hiding it.

## Test and build

```bash
pytest backend/test_main.py
npm run build
```

To use a backend at another address, copy `.env.example` to `.env` and change `VITE_API_URL`.

