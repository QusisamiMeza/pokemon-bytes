from app.database.data_loader import normalizar_move_name
from fastapi import HTTPException, status, APIRouter
from app.database.models import Pokemon, PokemonCompletePublic, PokemonPublic, PokemonMoveMethod
from app.database.db import SessionDep
from sqlmodel import select


router = APIRouter(prefix="/pokemons")


@router.get("/")
def get_pokemon_list(session: SessionDep) -> list[PokemonPublic]:
    pokemon_list = []
    pokemons_db = session.exec(select(Pokemon)).all()
    for pokemon in pokemons_db:
        types = []
        for type_name in pokemon.types:
            types.append(type_name.type.identifier)
        image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon.id}.png"
        pokemon_data = PokemonPublic(
            id=pokemon.id, identifier=pokemon.identifier, image=image, types=types
        )
        pokemon_list.append(pokemon_data)

    return pokemon_list


@router.get("/{id}")
def get_pokemon_id(id: int, session: SessionDep):
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == id)).first()

    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pokemon not found.",
        )

    abilities = [
        pokemon_ability.ability.identifier for pokemon_ability in pokemon.habilidades
    ]

    types = [pokemon_type.type.identifier for pokemon_type in pokemon.types]

    egg_groups = [
        pokemon_egg_group.egg_group.identifier
        for pokemon_egg_group in pokemon.grupos_huevo
    ]

    pokemon_stats = [pokemon_stat.stat for pokemon_stat in pokemon.estadisticas]
    stats_nombres = [stat.identifier for stat in pokemon_stats]
    stats_valores = [pokemon_stat.base_stat for pokemon_stat in pokemon.estadisticas]
    stats = {}
    for i in range(len(pokemon_stats)):
        valor = (stats_valores)[i]
        clave = (stats_nombres)[i]
        stats[clave] = valor
    total = 0
    for pokemon_stat in pokemon.estadisticas:
        total += pokemon_stat.base_stat
    stats["total"] = total

    pokemon_moves_ = [pokemon_moves.move for pokemon_moves in pokemon.pokemon_moves]
    move_names = [movimiento.identifier for movimiento in pokemon_moves_]

    return PokemonCompletePublic(
        id=pokemon.id,
        identifier=pokemon.identifier,
        image=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png",
        types=types,
        species_id=pokemon.species_id,
        height=pokemon.height,
        weight=pokemon.weight,
        base_experience=pokemon.base_experience,
        abilities=abilities,
        egg_groups=egg_groups,
        stats=stats,
        moves_that_can_learn=move_names,
    )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pokemons(session: SessionDep, id: int):
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == id)).first()
    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found."
        )

    session.delete(pokemon)
    session.commit()


@router.get("/{pokemon_id}/moves")
def get_pokemon_id_moves(session: SessionDep, pokemon_id: int) -> dict:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == pokemon_id)).first()

    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found."
        )

    # id de cada método mediante el cual un pokemon puede aprender movimientos
    level_method_id = session.exec(select(PokemonMoveMethod.pokemon_move_method_id).where(PokemonMoveMethod.name == "Nivel")).first()
    tm_method_id = session.exec(select(PokemonMoveMethod.pokemon_move_method_id).where(PokemonMoveMethod.name == "Máquina")).first()
    egg_method_id = session.exec(select(PokemonMoveMethod.pokemon_move_method_id).where(PokemonMoveMethod.name == "Huevo")).first()

    moves_by_level_method, moves_by_tm_method, moves_by_egg_method = [], [], []
    level_id_added_moves, tm_id_added_moves, egg_id_added_moves = [], [], []
    # listas para guardar los ids de movimientos ya guardados para que no hayan repeticiones

    pok_moves = pokemon.pokemon_moves
    for pok_move in pok_moves:
        if pok_move.pokemon_move_method_id == level_method_id and pok_move.move_id not in level_id_added_moves:
            name = pok_move.move.identifier
            moves_by_level_method.append(normalizar_move_name(name))
            level_id_added_moves.append(pok_move.move_id)

        elif pok_move.pokemon_move_method_id == tm_method_id and pok_move.move_id not in tm_id_added_moves:
            name = pok_move.move.identifier
            moves_by_tm_method.append(normalizar_move_name(name))
            tm_id_added_moves.append(pok_move.move_id)

        elif pok_move.pokemon_move_method_id == egg_method_id and pok_move.move_id not in egg_id_added_moves:
            name = pok_move.move.identifier
            moves_by_egg_method.append(normalizar_move_name(name))
            egg_id_added_moves.append(pok_move.move_id)

    all_pokemon_moves = {
        "MOVES LEARNT BY LEVEL UP" : moves_by_level_method,
        "MOVES LEARNT BY TIME MACHINES" : moves_by_tm_method,
        "MOVES LEARNT ACCORDING TO EGG GROUP" : moves_by_egg_method
    }

    return all_pokemon_moves