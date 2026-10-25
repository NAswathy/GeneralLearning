import pytest
from fastapi.testclient import TestClient

from backend.main import Choice, app, decide_winner


client = TestClient(app)


@pytest.mark.parametrize(
    ("player1", "player2", "winner"),
    [
        (Choice.rock, Choice.scissors, "player1"),
        (Choice.paper, Choice.rock, "player1"),
        (Choice.scissors, Choice.paper, "player1"),
        (Choice.scissors, Choice.rock, "player2"),
        (Choice.rock, Choice.paper, "player2"),
        (Choice.paper, Choice.scissors, "player2"),
        (Choice.rock, Choice.rock, "tie"),
        (Choice.paper, Choice.paper, "tie"),
        (Choice.scissors, Choice.scissors, "tie"),
    ],
)
def test_decide_winner(player1: Choice, player2: Choice, winner: str) -> None:
    assert decide_winner(player1, player2).winner == winner


def test_play_endpoint() -> None:
    response = client.post(
        "/api/play",
        json={"player1_choice": "paper", "player2_choice": "rock"},
    )
    assert response.status_code == 200
    assert response.json()["winner"] == "player1"


def test_play_endpoint_rejects_an_invalid_choice() -> None:
    response = client.post(
        "/api/play",
        json={"player1_choice": "water", "player2_choice": "rock"},
    )
    assert response.status_code == 422
