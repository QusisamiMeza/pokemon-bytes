from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import Session, create_engine
from sqlalchemy import select
from app.database.models import (
    Pokemon,
    PokemonType,
    Type,
    Move,
    MoveName,
    MoveDamageClass,
    MoveEffect,
    PokemonMove,
    PokemonMoveMethod,
    PokemonAbility,
    Ability,
    PokemonStat,
    Stat,
    PokemonEggGroup,
    EggGroup,
    Nature,
    Species,
)
from app.database.data_loader import (
    get_pokemon_data,
    get_pokemon_types_id,
    get_types,
    get_moves_data,
    get_move_names_data,
    get_move_categories_data,
    get_move_effects_data,
    get_pokemon_moves_data,
    get_pokemon_move_methods_data,
    get_pokemon_abilities,
    get_abilities,
    get_pokemon_stats,
    get_stats,
    get_pokemon_egg_group,
    get_egg_groups,
    get_nature,
    get_species_data,
    POKEMON_FILE_PATH,
    POKEMON_TYPES_FILE_PATH,
    TYPES_FILE_PATH,
    MOVES_FILE_PATH,
    MOVE_NAMES_FILE_PATH,
    MOVE_DAMAGE_CLASSES_FILE_PATH,
    MOVE_EFFECT_FILE_PATH,
    POKEMON_MOVES_FILE_PATH,
    POKEMON_MOVE_METHODS_FILE_PATH,
    POKEMON_ABILITIES_FILE_PATH,
    ABILITIES_FILE_PATH,
    POKEMON_STATS_FILE_PATH,
    STATS_FILE_PATH,
    POKEMON_EGG_GROUP_FILE_PATH,
    EGG_GROUP_FILE_PATH,
    NATURE_FILE_PATH,
    SPECIES_FILE_PATH,
)
import logging


SQLITE_FILE_PATH = "pokemon-bytes.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def seed_aux(session: Session, data: list, model):
    """Carga semillas en la base de datos para el modelo especificado si la tabla está vacía."""
    if session.exec(select(model)).first():
        logger.info(f"NOT {model.__name__} loading seeds")
        return

    logger.info(f"Loading {model.__name__} seeds...")
    session.add_all(data)
    session.commit()
    logger.info(f"{model.__name__} seeds loaded on Db")


def seed():
    with Session(engine) as session:
        # Do not seed if there's data present in the DB
        seed_aux(session, get_pokemon_data(POKEMON_FILE_PATH), Pokemon)
        seed_aux(session, get_pokemon_types_id(POKEMON_TYPES_FILE_PATH), PokemonType)
        seed_aux(session, get_types(TYPES_FILE_PATH), Type)
        seed_aux(session, get_moves_data(MOVES_FILE_PATH), Move)
        seed_aux(session, get_move_names_data(MOVE_NAMES_FILE_PATH), MoveName)
        seed_aux(
            session,
            get_move_categories_data(MOVE_DAMAGE_CLASSES_FILE_PATH),
            MoveDamageClass,
        )
        seed_aux(session, get_move_effects_data(MOVE_EFFECT_FILE_PATH), MoveEffect)
        seed_aux(session, get_pokemon_moves_data(POKEMON_MOVES_FILE_PATH), PokemonMove)
        seed_aux(
            session,
            get_pokemon_move_methods_data(POKEMON_MOVE_METHODS_FILE_PATH),
            PokemonMoveMethod,
        )
        seed_aux(
            session, get_pokemon_abilities(POKEMON_ABILITIES_FILE_PATH), PokemonAbility
        )
        seed_aux(session, get_abilities(ABILITIES_FILE_PATH), Ability)
        seed_aux(session, get_pokemon_stats(POKEMON_STATS_FILE_PATH), PokemonStat)
        seed_aux(session, get_stats(STATS_FILE_PATH), Stat)
        seed_aux(
            session, get_pokemon_egg_group(POKEMON_EGG_GROUP_FILE_PATH), PokemonEggGroup
        )
        seed_aux(session, get_egg_groups(EGG_GROUP_FILE_PATH), EggGroup)
        seed_aux(session, get_nature(NATURE_FILE_PATH), Nature)
        seed_aux(session, get_species_data(SPECIES_FILE_PATH), Species)
