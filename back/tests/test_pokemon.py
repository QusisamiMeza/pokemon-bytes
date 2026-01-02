import pytest
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel
from app.database.models import Pokemon
from app.database.db import get_db
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)
engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})


@pytest.fixture
def test_session():
    """Db en memoria para pruebas."""
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
def test_client(test_session):
    def override_get_db():
        yield test_session
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


def test_delete_pokemon(test_client, test_session):
    test_pokemon = Pokemon(
        id=99999,
        identifier="Digimon",
        species_id=1,
        height=7,
        weight=69,
        base_experience=64,
        order=1,
        is_default=1,
    )
    test_session.add(test_pokemon)
    test_session.commit()

    response = test_client.delete(f"/pokemons/{test_pokemon.id}/")
    assert response.status_code == 204


def test_delete_pokemon_no_existente():
    response = client.delete("/pokemons/99999")
    assert response.status_code == 404


def test_get_pokemon_id_no_encontrado():
    invalid_id = 99999
    response = client.get(f"/pokemons/{invalid_id}")

    assert response.status_code == 404
    content = response.json()
    assert "detail" in content
    assert content["detail"] == "Pokemon not found."


def test_get_pokemon_list():
    response = client.get("/pokemons/")
    assert response.status_code == 200


def test_get_pokemons_id_moves_id_found():
    response = client.get("/pokemons/1/moves")
    assert response.status_code == 200


def test_get_pokemons_id_moves_id_not_found():
    response = client.get("/pokemons/99999/moves")
    assert response.status_code == 404
