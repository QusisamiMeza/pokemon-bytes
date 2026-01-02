from sqlmodel import Field, SQLModel, Relationship
from typing import Dict, List, Optional
from sqlalchemy import Column, Integer, ForeignKey


class TeamComplete(SQLModel, table=False):
    id: int
    name: str
    generation: int
    members_: list["TeamMember"]


class TeamDataPublic(SQLModel, table=False):
    id: int
    name: str
    members: list


class TeamCreate(SQLModel, table=False):
    name: str
    generation: int
    members: List["TeamMemberCreate"]


class TeamMemberCreate(SQLModel, table=False):
    pokemon_id: int
    nature: str
    moves: List[str]
    stats: Dict[str, int]


class TeamMemberUpdate(SQLModel, table=False):
    id: int
    nature: Optional[str] = None
    moves: Optional[list[str]] = None
    stats: Optional[dict[str, int]] = None


class TeamUpdate(SQLModel, table=False):
    name: Optional[str]
    generation: Optional[int]
    add_members: Optional[list[TeamMemberCreate]]
    update_members: Optional[list[TeamMemberUpdate]]
    delete_members: Optional[list[int]]


# Models with table=True
class Team(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    generation: int
    members: List["TeamMember"] = Relationship(
        back_populates="team",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )


class TeamMember(SQLModel, table=True):
    __tablename__ = "team_member"

    id: int = Field(default=None, primary_key=True)
    pokemon_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("pokemon.id", ondelete="CASCADE"), nullable=False
        )
    )
    team_id: int = Field(foreign_key="team.id", nullable=False)
    nature: str = Field(nullable=False)

    types: List["TeamMemberType"] = Relationship(
        back_populates="team_member",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )
    stats: List["TeamMemberStat"] = Relationship(
        back_populates="team_member",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )
    moves: List["TeamMemberMove"] = Relationship(
        back_populates="team_member",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
        },
    )
    team: Optional[Team] = Relationship(back_populates="members")


class TeamMemberType(SQLModel, table=True):
    __tablename__ = "team_member_type"

    team_member_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("team_member.id", ondelete="CASCADE"), primary_key=True
        )
    )
    type_id: int = Field(foreign_key="type.id", primary_key=True)

    team_member: Optional[TeamMember] = Relationship(back_populates="types")
    type: Optional["Type"] = Relationship(back_populates="team_member_types")


class TeamMemberMove(SQLModel, table=True):
    __tablename__ = "team_member_move"

    team_member_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("team_member.id", ondelete="CASCADE"), primary_key=True
        )
    )
    move_id: int = Field(foreign_key="move.id", primary_key=True)

    team_member: Optional[TeamMember] = Relationship(back_populates="moves")
    move: Optional["Move"] = Relationship(back_populates="team_member_moves")


class TeamMemberStat(SQLModel, table=True):
    __tablename__ = "team_member_stat"

    team_member_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("team_member.id", ondelete="CASCADE"), primary_key=True
        )
    )
    stat_id: int = Field(foreign_key="stat.id", primary_key=True)
    stat_value: int = Field(nullable=False)

    team_member: Optional[TeamMember] = Relationship(back_populates="stats")
    stat: Optional["Stat"] = Relationship(back_populates="team_member_stats")
