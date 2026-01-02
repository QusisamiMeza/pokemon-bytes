from fastapi import HTTPException, status, APIRouter
from app.database.models import MoveBase, MovePublic, Move, PokemonMove, Pokemon, PokemonPublic
from app.database.db import SessionDep
from sqlmodel import select


router = APIRouter(prefix="/moves")


@router.get("/")
def get_moves(session: SessionDep) -> list[MoveBase]:
    moves_list = []
    moves = session.exec(select(Move)).all()

    for move in moves:
        for move_name in move.move_names:
            if move_name.local_language_id == 9:
                full_name = move_name.name

        move_data = MoveBase(
            id=move.id,
            name=full_name,
            power=move.power,
            accuracy=move.accuracy,
            power_points=move.pp
        )
        moves_list.append(move_data)

    return moves_list


@router.get("/{id_move}")
def show_data_move(session: SessionDep, id_move: int) -> MovePublic:
    move = session.exec(select(Move).where(Move.id == id_move)).first()

    if not move:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Move not found."
        )

    name = None
    for move_name in move.move_names:
        if move_name.local_language_id == 9:
            name = move_name.name

    type_name = move.move_type.identifier
    category = move.move_damage_class.identifier
    effect = move.effect.short_effect

    data_move = MovePublic(
        id=id_move,
        name=name,
        move_type=type_name.capitalize() if type_name else None,
        power=move.power,
        accuracy=move.accuracy,
        power_points=move.pp,
        generation=move.generation_id,
        category=category.capitalize() if category else None,
        effect=effect
    )

    return data_move


@router.get("/{id_move}/pokemons")
def pokemons_by_move(session: SessionDep, id_move: int) -> list[PokemonPublic]:
    list_pokemons_by_move = []
    pokemon_moves_db = session.exec(
        select(PokemonMove).where(PokemonMove.move_id == id_move)
    ).all()

    if not pokemon_moves_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Move not found."
        )

    pokemon_id_actual = None
    for pokemon in pokemon_moves_db:
        if pokemon.pokemon_id != pokemon_id_actual:
            types = []
            for type_name in pokemon.pokemon.types:
                types.append(type_name.type.identifier)
            image = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon.pokemon_id}.png"

            pokemon_db = session.exec(
                select(Pokemon).where(Pokemon.id == pokemon.pokemon_id)
            ).first()
            name_pokemon = pokemon_db.identifier

            pokemon_data_by_move = PokemonPublic(
                id=pokemon.pokemon_id,
                identifier=name_pokemon,
                image=image,
                types=types,
            )
            list_pokemons_by_move.append(pokemon_data_by_move)
            pokemon_id_actual = pokemon.pokemon_id

    return list_pokemons_by_move
