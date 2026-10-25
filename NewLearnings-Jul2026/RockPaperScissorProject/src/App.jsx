import { useCallback, useEffect, useMemo, useRef, useState } from "react";

const CHOICES = [
  { id: "rock", label: "Rock", symbol: "✊", detail: "Crushes scissors" },
  { id: "paper", label: "Paper", symbol: "✋", detail: "Covers rock" },
  { id: "scissors", label: "Scissors", symbol: "✌️", detail: "Cuts paper" },
];

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

function parseVoiceChoice(transcript) {
  const words = transcript.toLowerCase().match(/[a-z]+/g) || [];
  if (words.includes("scissor") || words.includes("scissors")) return "scissors";
  if (words.includes("paper")) return "paper";
  if (words.includes("rock")) return "rock";
  return null;
}

function ChoiceCard({ choice, selected, disabled, onSelect }) {
  return (
    <button
      className={`choice-card ${selected ? "selected" : ""}`}
      type="button"
      onClick={() => onSelect(choice.id)}
      disabled={disabled}
      aria-pressed={selected}
    >
      <span className="choice-symbol" aria-hidden="true">{choice.symbol}</span>
      <span className="choice-copy">
        <strong>{choice.label}</strong>
        <small>{choice.detail}</small>
      </span>
      <span className="choice-check" aria-hidden="true">✓</span>
    </button>
  );
}

function PlayerPanel({
  player,
  accent,
  choice,
  locked,
  listening,
  voiceBusy,
  voiceSupported,
  transcript,
  onChoose,
  onLock,
  onListen,
}) {
  return (
    <section className={`player-panel ${accent}`} aria-labelledby={`player-${player}`}>
      <div className="player-heading">
        <div>
          <span className="eyebrow">Player {player}</span>
          <h2 id={`player-${player}`}>{locked ? "Choice locked" : "Choose your move"}</h2>
        </div>
        <span className={`status-dot ${locked ? "ready" : ""}`}>
          {locked ? "Ready" : "Choosing"}
        </span>
      </div>

      <div className={`choice-list ${locked ? "is-locked" : ""}`}>
        {CHOICES.map((item) => (
          <ChoiceCard
            key={item.id}
            choice={item}
            selected={!locked && choice === item.id}
            disabled={locked}
            onSelect={onChoose}
          />
        ))}
        {locked && (
          <div className="locked-cover" aria-live="polite">
            <span className="lock-icon">✓</span>
            <strong>Move secured</strong>
            <small>Waiting for the other player</small>
          </div>
        )}
      </div>

      <div className="panel-actions">
        <button
          type="button"
          className={`voice-button ${listening ? "listening" : ""}`}
          onClick={onListen}
          disabled={locked || !voiceSupported || voiceBusy}
          aria-label={listening ? `Listening for Player ${player}` : `Use voice input for Player ${player}`}
          title={!voiceSupported ? "Voice recognition is not supported in this browser" : undefined}
        >
          <span className="mic-icon" aria-hidden="true">{listening ? "●" : "🎙"}</span>
          {listening ? "Listening…" : "Say your move"}
        </button>
        <button
          type="button"
          className="lock-button"
          disabled={!choice || locked || listening}
          onClick={onLock}
        >
          Lock choice
        </button>
      </div>

      <p className={`voice-feedback ${transcript ? "has-message" : ""}`} aria-live="polite">
        {transcript || (voiceSupported ? "Try saying “rock”, “paper”, or “scissors”." : "Voice needs Chrome or Edge; buttons still work.")}
      </p>
    </section>
  );
}

function ResultModal({ result, choices, onNextRound, onNewGame }) {
  const first = CHOICES.find((item) => item.id === choices.player1);
  const second = CHOICES.find((item) => item.id === choices.player2);

  return (
    <div className="modal-backdrop" role="presentation">
      <section className="result-modal" role="dialog" aria-modal="true" aria-labelledby="result-title">
        <span className="eyebrow">Round complete</span>
        <h2 id="result-title">{result.message}</h2>
        <div className="reveal-row">
          <div>
            <small>Player 1</small>
            <span>{first.symbol}</span>
            <strong>{first.label}</strong>
          </div>
          <b>VS</b>
          <div>
            <small>Player 2</small>
            <span>{second.symbol}</span>
            <strong>{second.label}</strong>
          </div>
        </div>
        <p className="reason">{result.reason}</p>
        <div className="modal-actions">
          <button type="button" className="secondary-button" onClick={onNewGame}>Reset score</button>
          <button type="button" className="primary-button" onClick={onNextRound} autoFocus>Next round →</button>
        </div>
      </section>
    </div>
  );
}

export default function App() {
  const [choices, setChoices] = useState({ player1: null, player2: null });
  const [locked, setLocked] = useState({ player1: false, player2: false });
  const [scores, setScores] = useState({ player1: 0, player2: 0, ties: 0 });
  const [round, setRound] = useState(1);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [listeningTo, setListeningTo] = useState(null);
  const [voiceText, setVoiceText] = useState({ player1: "", player2: "" });
  const recognitionRef = useRef(null);

  const SpeechRecognition = useMemo(
    () => window.SpeechRecognition || window.webkitSpeechRecognition,
    [],
  );
  const voiceSupported = Boolean(SpeechRecognition);

  const playRound = useCallback(async (roundChoices) => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch(`${API_URL}/api/play`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          player1_choice: roundChoices.player1,
          player2_choice: roundChoices.player2,
        }),
      });
      if (!response.ok) throw new Error("The game server returned an error.");
      const data = await response.json();
      setScores((current) => ({
        ...current,
        [data.winner === "tie" ? "ties" : data.winner]: current[data.winner === "tie" ? "ties" : data.winner] + 1,
      }));
      setResult(data);
    } catch (requestError) {
      setError(`${requestError.message} Check that FastAPI is running on port 8000.`);
      setLocked({ player1: false, player2: false });
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    if (locked.player1 && locked.player2 && !result && !loading) playRound(choices);
  }, [locked, choices, result, loading, playRound]);

  useEffect(() => () => recognitionRef.current?.abort(), []);

  const choose = (player, move) => {
    setChoices((current) => ({ ...current, [player]: move }));
    setVoiceText((current) => ({ ...current, [player]: "" }));
  };

  const lockChoice = (player) => {
    if (!choices[player]) return;
    setLocked((current) => ({ ...current, [player]: true }));
  };

  const listen = (player) => {
    if (!SpeechRecognition || listeningTo || recognitionRef.current) return;
    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.continuous = false;
    recognition.maxAlternatives = 3;
    recognitionRef.current = recognition;

    recognition.onstart = () => {
      setListeningTo(player);
      setVoiceText((current) => ({ ...current, [player]: "Listening now…" }));
    };
    recognition.onresult = (event) => {
      const transcripts = Array.from(event.results[0]).map((item) => item.transcript);
      const move = transcripts.map(parseVoiceChoice).find(Boolean);
      if (move) {
        setChoices((current) => ({ ...current, [player]: move }));
        setVoiceText((current) => ({
          ...current,
          [player]: `Heard “${transcripts[0]}” — ${move} selected. Lock it when ready.`,
        }));
      } else {
        setVoiceText((current) => ({
          ...current,
          [player]: `Heard “${transcripts[0]}”. Please try rock, paper, or scissors.`,
        }));
      }
    };
    recognition.onerror = (event) => {
      const message = event.error === "not-allowed"
        ? "Microphone access was blocked. Allow it in your browser settings."
        : "I couldn’t hear a move. Please try again.";
      setVoiceText((current) => ({ ...current, [player]: message }));
    };
    recognition.onend = () => {
      setListeningTo(null);
      recognitionRef.current = null;
    };
    recognition.start();
  };

  const nextRound = () => {
    setChoices({ player1: null, player2: null });
    setLocked({ player1: false, player2: false });
    setVoiceText({ player1: "", player2: "" });
    setResult(null);
    setError("");
    setRound((value) => value + 1);
  };

  const newGame = () => {
    setScores({ player1: 0, player2: 0, ties: 0 });
    setRound(1);
    setChoices({ player1: null, player2: null });
    setLocked({ player1: false, player2: false });
    setVoiceText({ player1: "", player2: "" });
    setResult(null);
    setError("");
  };

  return (
    <main className="app-shell">
      <header className="topbar">
        <a className="brand" href="#game" aria-label="Hand Game Arena home">
          <span className="brand-mark">✦</span>
          <span>HAND GAME <b>ARENA</b></span>
        </a>
        <div className="round-pill">Round {String(round).padStart(2, "0")}</div>
      </header>

      <section className="hero" id="game">
        <p className="eyebrow">Two players · One device · Best instincts win</p>
        <h1>Rock. Paper. <em>Scissors.</em></h1>
        <p>Pick with a tap or say your move out loud. Lock both choices to reveal the winner.</p>
      </section>

      <section className="scoreboard" aria-label="Current score">
        <div><span>Player 1</span><strong>{String(scores.player1).padStart(2, "0")}</strong></div>
        <div className="ties"><span>Ties</span><strong>{String(scores.ties).padStart(2, "0")}</strong></div>
        <div><span>Player 2</span><strong>{String(scores.player2).padStart(2, "0")}</strong></div>
      </section>

      {error && <div className="error-banner" role="alert">{error}</div>}

      <div className="game-grid">
        <PlayerPanel
          player="1"
          accent="orange"
          choice={choices.player1}
          locked={locked.player1}
          listening={listeningTo === "player1"}
          voiceBusy={Boolean(listeningTo)}
          voiceSupported={voiceSupported}
          transcript={voiceText.player1}
          onChoose={(move) => choose("player1", move)}
          onLock={() => lockChoice("player1")}
          onListen={() => listen("player1")}
        />
        <div className="versus" aria-hidden="true"><span>VS</span></div>
        <PlayerPanel
          player="2"
          accent="blue"
          choice={choices.player2}
          locked={locked.player2}
          listening={listeningTo === "player2"}
          voiceBusy={Boolean(listeningTo)}
          voiceSupported={voiceSupported}
          transcript={voiceText.player2}
          onChoose={(move) => choose("player2", move)}
          onLock={() => lockChoice("player2")}
          onListen={() => listen("player2")}
        />
      </div>

      {loading && <div className="loading-toast" role="status">Revealing the winner…</div>}
      {result && (
        <ResultModal result={result} choices={choices} onNextRound={nextRound} onNewGame={newGame} />
      )}

      <footer>Choose wisely. Keep it friendly. <span>✦</span> Built for two.</footer>
    </main>
  );
}
