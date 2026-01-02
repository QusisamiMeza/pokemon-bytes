from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from sqlalchemy import Column, Integer, ForeignKey


class PokemonPublic(SQLModel, table=False):
    id: int
    identifier: str
    image: str
    types: list[str] | None


class PokemonCompletePublic(PokemonPublic):
    species_id: int
    height: int
    weight: int
    base_experience: int
    abilities: list[str]
    egg_groups: list[str]
    stats: dict
    moves_that_can_learn: list[str]


class Generation(SQLModel):
    id: int


# Models with table=True
class Pokemon(SQLModel, table=True):
    id: int = Field(primary_key=True)
    identifier: str
    species_id: int = Field(foreign_key="species.id", nullable=True)
    height: int
    weight: int
    base_experience: int
    order: int
    is_default: int

    pokemon_moves: list["PokemonMove"] = Relationship(
        back_populates="pokemon",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "passive_deletes": True,
        },
    )
    habilidades: list["PokemonAbility"] = Relationship(
        back_populates="pokemon_abilities",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "passive_deletes": True,
        },
    )
    estadisticas: List["PokemonStat"] = Relationship(
        back_populates="pokemon_stats",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "passive_deletes": True,
        },
    )
    grupos_huevo: list["PokemonEggGroup"] = Relationship(
        back_populates="pokemon_eg",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "passive_deletes": True,
        },
    )
    types: list["PokemonType"] | None = Relationship(
        back_populates="pokemon",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "passive_deletes": True,
        },
    )
    specie: Optional["Species"] = Relationship(
        back_populates="pokemon_specie",
        sa_relationship_kwargs={"passive_deletes": True},
    )


class Type(SQLModel, table=True):
    id: int = Field(primary_key=True)
    identifier: str
    generation_id: int
    damage_class_id: int

    pokemon_types: list["PokemonType"] | None = Relationship(back_populates="type")
    move: Optional[list["Move"]] = Relationship(back_populates="move_type")
    team_member_types: Optional[List["TeamMemberType"]] = Relationship(
        back_populates="type"
    )


class PokemonType(SQLModel, table=True):
    __tablename__ = "pokemon_type"

    pokemon_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("pokemon.id", ondelete="CASCADE"), primary_key=True
        )
    )
    type_id: int = Field(primary_key=True, foreign_key="type.id")
    slot: int

    pokemon: Optional[Pokemon] = Relationship(back_populates="types")
    type: Optional[Type] = Relationship(back_populates="pokemon_types")


class Ability(SQLModel, table=True):
    id: int = Field(primary_key=True)
    identifier: str
    generation: int
    is_main_series: int

    abilities: list["PokemonAbility"] = Relationship(back_populates="ability")


class PokemonAbility(SQLModel, table=True):
    __tablename__ = "pokemon_ability"

    pokemon_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("pokemon.id", ondelete="CASCADE"), primary_key=True
        )
    )
    ability_id: int = Field(foreign_key="ability.id", primary_key=True)
    is_hidden: int
    slot: int

    ability: Optional[Ability] = Relationship(back_populates="abilities")
    pokemon_abilities: Optional[Pokemon] = Relationship(back_populates="habilidades")


class PokemonStat(SQLModel, table=True):
    __tablename__ = "pokemon_stat"

    pokemon_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("pokemon.id", ondelete="CASCADE"), primary_key=True
        )
    )
    stat_id: int = Field(foreign_key="stat.id", primary_key=True)
    base_stat: int
    effort: int

    stat: Optional["Stat"] = Relationship(back_populates="stats")
    pokemon_stats: Optional[Pokemon] = Relationship(back_populates="estadisticas")


class Stat(SQLModel, table=True):
    id: int = Field(primary_key=True)
    damage_class_id: int | None
    identifier: str
    is_battle_only: int
    game_index: int

    stats: list[PokemonStat] = Relationship(back_populates="stat")
    team_member_stats: list["TeamMemberStat"] = Relationship(back_populates="stat")


class Species(SQLModel, table=True):
    id: int = Field(primary_key=True)
    generation_id: int

    pokemon_specie: list[Pokemon] = Relationship(back_populates="specie")


class EggGroup(SQLModel, table=True):
    __tablename__ = "egg_group"

    id: int = Field(primary_key=True)
    identifier: str

    pokemon_egg_groups: list["PokemonEggGroup"] = Relationship(
        back_populates="egg_group"
    )


class PokemonEggGroup(SQLModel, table=True):
    __tablename__ = "pokemon_egg_group"

    species_id: int = Field(foreign_key="pokemon.species_id", primary_key=True)
    egg_group_id: int = Field(foreign_key="egg_group.id", primary_key=True)

    egg_group: Optional[EggGroup] = Relationship(back_populates="pokemon_egg_groups")
    pokemon_eg: Optional[Pokemon] = Relationship(back_populates="grupos_huevo")


class Nature(SQLModel, table=True):
    id: int = Field(primary_key=True)
    identifier: str
    decreased_stat_id: int
    increased_stat_id: int
    hates_flavor_id: int
    likes_flavor_id: int
    game_index: int
