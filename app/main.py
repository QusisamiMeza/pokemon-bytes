from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.pokemon import router as pokemon_router
from app.routers.moves import router as moves_router
from app.routers.teams import router as teams_router
from app.database.db import seed


app = FastAPI()


@app.get("/")
def read_root():
    return {
        "mensaje": "Bienvenido a la API de Pokemon Bytes",
        "docs_url": "/docs",
        "endpoints_disponibles": [
            {"metodo": "GET", "ruta": "/pokemons/"},
            {"metodo": "GET", "ruta": "/pokemons/{id}"},
            {"metodo": "DELETE", "ruta": "/pokemons/{id}"},
            {"metodo": "GET", "ruta": "/pokemons/{pokemon_id}/moves"},
            {"metodo": "GET", "ruta": "/moves/"},
            {"metodo": "GET", "ruta": "/moves/{id_move}"},
            {"metodo": "GET", "ruta": "/moves/{id_move}/pokemons"},
            {"metodo": "GET", "ruta": "/teams/natures"},
            {"metodo": "GET", "ruta": "/teams/"},
            {"metodo": "GET", "ruta": "/teams/{id}"},
            {"metodo": "PATCH", "ruta": "/teams/{id}"},
            {"metodo": "DELETE", "ruta": "/teams/{id}"},
        ],
    }


app.include_router(pokemon_router)
app.include_router(moves_router)
app.include_router(teams_router)


origins = [
   "http://localhost:5173",
]

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

seed()
