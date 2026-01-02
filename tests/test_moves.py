from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_get_moves_ok():
    response = client.get("/moves/")
    assert response.status_code == 200


def test_id_move_found_full_data():
    response = client.get("/moves/1")
    assert response.json() == {
        "id": 1,
        "name": "Pound",
        "move_type": "Normal",
        "power": 40,
        "accuracy": 100,
        "power_points": 35,
        "generation": 1,
        "category": "Physical",
        "effect": "Inflicts regular damage with no additional effect.",
    }


def test_id_move_found_missing_data():
    response = client.get("/moves/602")
    assert response.json() == {
        "id": 602,
        "name": "Magnetic Flux",
        "move_type": "Electric",
        "power": None,
        "accuracy": None,
        "power_points": 20,
        "generation": 6,
        "category": "Status",
        "effect": "Raises the Defense and Special Defense of all friendly Pokémon with []{ability:plus} or []{ability:minus} by one stage.",
    }


def test_status_code_move():
    response = client.get("/moves/1")
    assert response.status_code == 200


def test_status_code_move_id_not_found():
    response = client.get("/moves/99999")
    assert response.status_code == 404


def test_pokemons_by_move_not_found():
    response = client.get("/moves/99999/pokemons")

    assert response.status_code == 404


def test_pokemons_by_move_found():
    response = client.get("/moves/1/pokemons")

    assert response.status_code == 200
