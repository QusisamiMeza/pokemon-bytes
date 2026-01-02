from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def get_mock_team():
    return {
        "name": "Los vengadores",
        "generation": 1,
        "members": [
            {
                "pokemon_id": 25,
                "nature": "Modest",
                "stats": {
                    "hp": 100,
                    "attack": 100,
                    "defense": 50,
                    "special-attack": 30,
                    "special-defense": 40,
                    "speed": 50,
                    "accuracy": 50,
                    "evasion": 50,
                },
                "moves": ["mega-punch", "pay-day"],
            },
        ],
    }


def get_update_mock_team():
    return {
        "name": "Brigada B",
        "generation": 1,
        "add_members": [
            {
                "pokemon_id": 2,
                "stats": {
                    "hp": 100,
                    "attack": 100,
                    "defense": 50,
                    "special-attack": 30,
                    "special-defense": 40,
                    "speed": 50,
                    "accuracy": 50,
                    "evasion": 50,
                },
                "moves": ["swords-dance", "cut", "vine-whip"],
                "nature": "Fuerte",
            }
        ],
        "update_members": [
            {
                "id": 1,
                "stats": {
                    "hp": 20,
                    "attack": 110,
                    "defense": 60,
                    "special-attack": 40,
                    "special-defense": 50,
                    "speed": 60,
                    "accuracy": 60,
                    "evasion": 60,
                },
                "moves": ["growl", "surf"],
                "nature": "Audaz",
            }
        ],
        "delete_members": [2],
    }


def test_get_nature():
    response = client.get("/teams/natures")
    assert response.status_code == 200


def test_get_teams_data():
    response = client.post("/teams", json=get_mock_team())
    response = client.get("/teams/", params={"page": 0, "page_size": 10})
    assert response.status_code == 200
    client.delete(f"/teams/{response.json()[0]['id']}")


def test_get_teams_max_10():
    response = client.post("/teams", json=get_mock_team())
    response = client.get("/teams/", params={"page": 0, "page_size": 10})
    data = response.json()
    assert len(data) <= 10
    client.delete(f"/teams/{response.json()[0]['id']}")


def test_get_teams_content():
    team = get_mock_team()
    response = client.post("/teams", json=team)
    team["name"] = "Brigada B"
    response = client.post("/teams", json=team)

    mock_team = [
        {"id": 1, "name": "Los vengadores", "members": ["pikachu"]},
        {"id": 2, "name": "Brigada B", "members": ["pikachu"]},
    ]

    response = client.get("/teams/", params={"page": 0, "page_size": 10})
    data = response.json()

    assert data == mock_team
    client.delete(f"/teams/{response.json()[0]['id']}")
    client.delete(f"/teams/{response.json()[1]['id']}")


def test_get_teams_id():
    invalid_id = 99999
    response = client.get(f"/teams/{invalid_id}")
    assert response.status_code == 404


def test_post_team():
    response = client.post("/teams", json=get_mock_team())
    assert response.status_code == 201
    id = response.json()["id"]
    client.delete(f"/teams/{id}")


def test_post_teams_invalid_size():
    team = get_mock_team()
    team["members"] = []
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_post_teams_invalid_name():
    response_team_a = client.post("/teams", json=get_mock_team())
    response_team_b = client.post("/teams", json=get_mock_team())
    assert response_team_b.status_code == 400
    client.delete(f"/teams/{response_team_a.json()['id']}")


def test_post_teams_invalid_generation():
    team = get_mock_team()
    team["generation"] = 99999
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_post_teams_invalid_member_pokemon_id():
    team = get_mock_team()
    team["members"][0]["pokemon_id"] = 99999
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_post_teams_invalid_member_move_count():
    team = get_mock_team()
    team["members"][0]["moves"] = []
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_post_teams_invalid_member_move():
    team = get_mock_team()
    team["members"][0]["moves"] = ["invalid"]
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_post_teams_inavlid_member_learnable_move():
    team = get_mock_team()
    team["members"][0]["moves"] = ["swords-dance"]
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_post_teams_invalid_member_requred_stats():
    team = get_mock_team()
    team["members"][0]["stats"] = {}
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_post_teams_invalid_member_stat_value():
    team = get_mock_team()
    team["members"][0]["stats"][1] = 99999
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_post_teams_invalid_member_stat_count():
    team = get_mock_team()
    team["members"][0]["stats"] = {
        "hp": 100,
        "attack": 100,
        "defense": 50,
        "special-attack": 30,
        "special-defense": 100,
        "speed": 50,
        "accuracy": 50,
        "evasion": 50,
    }
    response = client.post("/teams", json=team)
    assert response.status_code == 400


def test_update_team():
    response = client.post("/teams", json=get_mock_team())
    id = response.json()["id"]
    response = client.patch(f"/teams/{id}", json=get_update_mock_team())
    assert response.status_code == 200
    client.delete(f"/teams/{id}")


def test_update_team_invalid_id():
    response = client.patch("/teams/0", json=get_update_mock_team())
    assert response.status_code == 404


def test_delete_teams():
    team = get_mock_team()
    team["name"] = "ELECCEED"
    response = client.post("/teams", json=team)
    id = response.json()["id"]
    response = client.delete(f"/teams/{id}")
    assert response.status_code == 200


def test_delete_teams_id_not_found():
    response = client.delete("/teams/0")
    assert response.status_code == 404
