from app.database.models import (
    Team,
    TeamCreate,
    TeamUpdate,
    Nature,
    TeamComplete,
    Pokemon,
    TeamDataPublic,
)

from app.routers.utils.teams_helpers import (
    validate_team_data,
    validate_team_member_data,
    validate_team_name,
    create_team_member,
    get_team_by_id,
    validate_team_size_plus_one,
    update_team_member,
    delete_team_member,
)
from fastapi import HTTPException, status, APIRouter, Query
from app.database.db import SessionDep
from sqlmodel import select

router = APIRouter(prefix="/teams")


@router.get("/natures")
def get_nature(session: SessionDep):
    natures = list(session.exec(select(Nature)).all())
    return natures


@router.get("/")
def get_teams_data(
    session: SessionDep, page: int = Query(0, ge=0), page_size: int = Query(10, gt=0)
) -> list[TeamDataPublic]:
    team_list = []
    teams_db = session.exec(select(Team)).all()
    for team in teams_db:
        members_names_list = []
        for member in team.members:
            pokemons_db = session.exec(select(Pokemon)).all()
            for pok in pokemons_db:
                if pok.id == member.pokemon_id:
                    members_names_list.append(pok.identifier)
        team_data = TeamDataPublic(
            id=team.id,
            name=team.name,
            members=members_names_list,
        )
        team_list.append(team_data)

    start = page * page_size
    end = min(start + page_size, len(team_list))

    return team_list[start:end]


@router.get("/{id}")
def get_teams_id(id: int, session: SessionDep):
    team = session.exec(select(Team).where(Team.id == id)).first()

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found.",
        )

    team_members = [member for member in team.members]

    return TeamComplete(
        id=team.id, name=team.name, generation=team.generation, members_=team_members
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_team(session: SessionDep, team_create: TeamCreate):
    validate_team_data(team_create, session)
    for member in team_create.members:
        validate_team_member_data(member, team_create, session)

    team = Team(name=team_create.name, generation=team_create.generation)
    session.add(team)
    session.commit()
    session.refresh(team)

    for member_create in team_create.members:
        create_team_member(member_create, team, session)

    session.commit()
    session.refresh(team)
    return team


@router.patch("/{id}")
def update_team(id: int, team_update: TeamUpdate, session: SessionDep):
    existing_team = get_team_by_id(id, session)
    if not existing_team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Team not found.",
        )

    if existing_team.name != team_update.name:
        validate_team_name(team_update, session)
        existing_team.name = team_update.name
        session.commit()

    if team_update.add_members:
        for member in team_update.add_members:
            validate_team_size_plus_one(existing_team)
            validate_team_member_data(member, team_update, session)
            create_team_member(member, existing_team, session)

    if team_update.update_members:
        for member in team_update.update_members:
            update_team_member(member, session)

    if team_update.delete_members:
        for member_id in team_update.delete_members:
            delete_team_member(member_id, existing_team, session)

    return existing_team


@router.delete("/{team_id}")
def delete_team(session: SessionDep, team_id: int):
    team = session.exec(select(Team).where(Team.id == team_id)).first()

    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Team not found."
        )

    session.delete(team)
    session.commit()
