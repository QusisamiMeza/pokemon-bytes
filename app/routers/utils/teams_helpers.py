from sqlalchemy import delete, select
from sqlmodel import Session
from app.database.data_loader import (
    generations,
    MIN_MOVES_PER_MEMBER,
    MAX_MOVES_PER_MEMBER,
    MIN_TEAM_MEMBERS,
    MAX_TEAM_MEMBERS,
    MAX_STAT_VALUE,
    MAX_STATS_TOTAL,
)
from app.database.models import (
    Move,
    Nature,
    Pokemon,
    PokemonMove,
    PokemonType,
    Species,
    Stat,
    Team,
    TeamMember,
    TeamMemberMove,
    TeamMemberStat,
    TeamMemberType,
)
from fastapi import HTTPException, status


# Queries
def get_pokemon_by_id(id: int, session: Session):
    """Devuelve el Pokémon con el ID dado, o None si no existe."""
    return session.exec(select(Pokemon.id).where(Pokemon.id == id)).scalar_one_or_none()


def get_move_by_id(move_id: int, session: Session):
    """Devuelve el movimiento con el ID dado, o None si no existe."""
    return session.exec(select(Move).where(Move.id == move_id)).first()


def get_move_by_identifier(identifier: str, session: Session):
    """Devuelve el movimiento con el identificador dado, o None si no existe."""
    return session.exec(
        select(Move).where(Move.identifier == identifier)
    ).scalar_one_or_none()


def get_team_by_id(id: int, session: Session):
    """Devuelve el equipo con el ID dado, o None si no existe."""
    return session.exec(select(Team).where(Team.id == id)).scalar_one_or_none()


def get_member_by_id(id: int, session: Session):
    """Devuelve un miembro de equipo con el ID dado, o None si no existe."""
    statement = select(TeamMember).where(TeamMember.id == id)
    return session.exec(statement).scalar_one_or_none()


# Condiciones
def pokemon_exists(id: int, session: Session):
    """Devuelve True si el pokemon existe en la base de datos."""
    return session.exec(select(Pokemon.id).where(Pokemon.id == id)).first() is not None


def move_exists(identifier: str, session: Session):
    """Devuelve True si el movimiento existe en la base de datos."""
    return (
        session.exec(select(Move).where(Move.identifier == identifier)).first()
        is not None
    )


def team_size_is_valid(size: int):
    """Devuelve True si el equipo tiene entre 1 y 6 miembros."""
    return MIN_TEAM_MEMBERS <= size <= MAX_TEAM_MEMBERS


# TODO esto sigue usando una lista de generaciones en memoria, debería usar la db.
def team_generation_is_valid(team):
    """Devuelve True si la generación del equipo es válida."""
    return any(gen.id == team.generation for gen in generations)


def name_available(name: str, session: Session) -> bool:
    """Devuelve True si el nombre de equipo no está en uso."""
    return session.exec(select(Team).where(Team.name == name)).first() is None


def has_valid_number_of_moves(moves):
    """Devuelve True si el miembro tiene entre 1 y 4 movimientos."""
    return MIN_MOVES_PER_MEMBER <= len(moves) <= MAX_MOVES_PER_MEMBER


def has_required_stats(pokemon_stats: dict[int, int], session: Session) -> bool:
    """Verifica si el miembro tiene todas las estadísticas requeridas basadas en la base de datos."""
    required_stats = session.exec(select(Stat.identifier)).scalars().all()
    return set(pokemon_stats.keys()) == set(required_stats)


def are_stats_valid(stats):
    """Returns True if all stats are between 0 and 255."""
    return all(0 <= value <= MAX_STAT_VALUE for value in stats.values())


def move_can_be_learned_by_pokemon(move_id: int, pokemon_id: int, session: Session):
    """Devuelve True si el movimiento puede ser aprendido por el pokemon base."""
    statement = select(PokemonMove).where(
        PokemonMove.move_id == move_id, PokemonMove.pokemon_id == pokemon_id
    )
    return session.exec(statement).first() is not None


# Validaciones
def validate_team_size(team):
    """Lanza errores de validación si la cantidad de miembros del equipo es incorrecta."""
    if not team_size_is_valid(len(team.members)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid number of members, must be between 1 and 6.",
        )


def validate_team_name(team, session: Session):
    """Lanza errores de validación si el nombre del equipo está en uso."""
    if not name_available(team.name, session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Team name already in use."
        )


def validate_team_generation(team):
    """Lanza errores de validación si la generación del equipo es incorrecta."""
    if not team_generation_is_valid(team):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid generation."
        )


def validate_team_data(team, session: Session):
    """Lanza errores de validación si el team tiene datos incorrectos."""
    validate_team_size(team)
    validate_team_name(team, session)
    validate_team_generation(team)


def validate_team_member_moves(member_moves, pokemon_id, session: Session):
    """Lanza errores de validación si la información de los movimientos es incorrecta."""
    if not has_valid_number_of_moves(member_moves):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid number of moves, must be between 1 and 4.",
        )

    for move in member_moves:
        move = get_move_by_identifier(move, session)
        if not move:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Move not found."
            )

        if not move_can_be_learned_by_pokemon(move.id, pokemon_id, session):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one move cannot be learned by the pokemon.",
            )


def validate_team_member_stats(stats, session: Session):
    """Lanza errores de validación si la información de las stats es incorrecta."""
    if not has_required_stats(stats, session):
        raise HTTPException(status_code=400, detail="Invalid stats.")

    if sum(stats.values()) > MAX_STATS_TOTAL:
        raise HTTPException(
            status_code=400,
            detail="Total stats of each team member cannot exceed 510.",
        )

    if not are_stats_valid(stats):
        raise HTTPException(
            status_code=400,
            detail="Team member stats must be between 0 and 255.",
        )


def validate_team_member_generation(team, pokemon_id, session: Session):
    """Lanza errores de validación si el miembro no pertenece a la generacion del equipo."""
    species_id = (
        session.exec(select(Pokemon.species_id).where(Pokemon.id == pokemon_id))
        .scalars()
        .first()
    )
    statement = select(Species.generation_id).where(Species.id == species_id)
    pokemon_generation = session.exec(statement).scalars().first()

    if pokemon_generation is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Species not found for pokemon.",
        )

    if pokemon_generation != team.generation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"At least one member is not from generation {team.generation}.",
        )


def validate_team_member_nature(member, session: Session):
    """Lanza un error de validación si la naturaleza del miembro no es válida."""
    nature = session.exec(
        select(Nature).where(Nature.identifier == member.nature)
    ).first()
    if not nature:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nature not found.",
        )


def validate_team_member_data(member, team, session: Session):
    """Lanza errores de validación si Pokémon, naturaleza, stats o moves son inválidos."""
    if not pokemon_exists(member.pokemon_id, session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pokemon not found.",
        )
    # TODO check the nature validation
    # validate_team_member_nature(member, session)
    validate_team_member_moves(member.moves, member.pokemon_id, session)
    validate_team_member_stats(member.stats, session)
    validate_team_member_generation(team, member.pokemon_id, session)


def validate_team_size_plus_one(team):
    """Lanza errores de validación si el equipo no puede tener un miembro adicional."""
    if not team_size_is_valid(len(team.members) + 1):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The team cannot have more than 6 members.",
        )


# Operaciones
def create_team_member(member, team, session: Session):
    """Crea un nuevo miembro en el equipo dado."""
    new_member = TeamMember(
        pokemon_id=member.pokemon_id,
        team_id=team.id,
        nature=member.nature,
    )
    session.add(new_member)
    session.commit()
    session.refresh(new_member)

    # Create types
    statement = select(PokemonType.type_id).where(
        PokemonType.pokemon_id == member.pokemon_id
    )
    type_ids = session.exec(statement).scalars().all()

    for id in type_ids:
        session.add(TeamMemberType(team_member_id=new_member.id, type_id=id))
    session.commit()

    # Create Stats
    for identifier, value in member.stats.items():
        stat_id = session.exec(
            select(Stat.id).where(Stat.identifier == identifier)
        ).scalar_one_or_none()
        session.add(
            TeamMemberStat(
                team_member_id=new_member.id, stat_id=stat_id, stat_value=value
            )
        )

    # Create Moves
    for move in member.moves:
        move = get_move_by_identifier(move, session)
        session.add(TeamMemberMove(team_member_id=new_member.id, move_id=move.id))


def update_team_member_types(new_types, member_id: int, session: Session):
    """Actualiza los tipos del miembro del equipo."""
    statement = delete(TeamMemberType).where(TeamMemberType.team_member_id == member_id)
    session.exec(statement)
    for type_id in new_types:
        session.add(TeamMemberType(team_member_id=member_id, type_id=type_id))


def update_team_member_moves(new_moves, member_id: int, session: Session):
    """Actualiza los movimientos del miembro del equipo."""
    statement = delete(TeamMemberMove).where(TeamMemberMove.team_member_id == member_id)
    session.exec(statement)
    for move_id in new_moves:
        session.add(TeamMemberMove(team_member_id=member_id, move_id=move_id))


def update_team_member_stats(new_stats, member_id: int, session: Session):
    """Actualiza las estadísticas del miembro del equipo."""
    statement = delete(TeamMemberStat).where(TeamMemberStat.team_member_id == member_id)
    session.exec(statement)
    for identifier, value in new_stats.items():
        statement = select(Stat.id).where(Stat.identifier == identifier)
        stat_id = session.exec(statement).scalar_one_or_none()
        session.add(
            TeamMemberStat(team_member_id=member_id, stat_id=stat_id, stat_value=value)
        )


def update_team_member(member, session: Session):
    """Actualiza el miembro con el id dado, si no existe lanza un error de validacion."""
    existing_member = get_member_by_id(member.id, session)
    if not existing_member:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Team member not found.",
        )

    if member.nature is not None:
        # validate_team_member_nature(member)
        existing_member.nature = member.nature

    if member.moves is not None:
        base_pokemon = get_pokemon_by_id(existing_member.pokemon_id, session)
        validate_team_member_moves(member.moves, base_pokemon, session)
        update_team_member_moves(member.moves, existing_member.id, session)

    if member.stats is not None:
        validate_team_member_stats(member.stats, session)
        update_team_member_stats(member.stats, existing_member.id, session)

    session.commit()
    session.refresh(existing_member)


def delete_team_member(id, team, session: Session):
    """Elimina el miembro con el id dado."""
    if not team_size_is_valid(len(team.members) - 1):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The team cannot have less than 1 member.",
        )

    session.exec(delete(TeamMember).where(TeamMember.id == id))
    session.exec(delete(TeamMemberType).where(TeamMemberType.team_member_id == id))
    session.exec(delete(TeamMemberMove).where(TeamMemberMove.team_member_id == id))
    session.exec(delete(TeamMemberStat).where(TeamMemberStat.team_member_id == id))
    session.commit()
    team.members = [member for member in team.members if member.id != id]
