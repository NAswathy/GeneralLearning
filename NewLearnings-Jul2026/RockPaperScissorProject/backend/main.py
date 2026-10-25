from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Choice(str, Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"


class RoundRequest(BaseModel):
    player1_choice: Choice
    player2_choice: Choice


class RoundResult(BaseModel):
    winner: str
    message: str
    reason: str


app = FastAPI(
    title="Hand Game Arena API",
    description="Determines the winner of a two-player Rock Paper Scissors round.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

WINNING_MOVES = {
    Choice.rock: Choice.scissors,
    Choice.paper: Choice.rock,
    Choice.scissors: Choice.paper,
}


def decide_winner(player1: Choice, player2: Choice) -> RoundResult:
    """Return the outcome for one validated round."""
    if player1 == player2:
        return RoundResult(
            winner="tie",
            message="It’s a tie!",
            reason=f"You both chose {player1.value}.",
        )

    if WINNING_MOVES[player1] == player2:
        winner = "player1"
        message = "Player 1 wins!"
    else:
        winner = "player2"
        message = "Player 2 wins!"

    winning_choice = player1 if winner == "player1" else player2
    losing_choice = player2 if winner == "player1" else player1
    verbs = {Choice.rock: "crushes", Choice.paper: "covers", Choice.scissors: "cuts"}

    return RoundResult(
        winner=winner,
        message=message,
        reason=f"{winning_choice.value.title()} {verbs[winning_choice]} {losing_choice.value}.",
    )


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/play", response_model=RoundResult)
def play_round(round_request: RoundRequest) -> RoundResult:
    return decide_winner(round_request.player1_choice, round_request.player2_choice)

