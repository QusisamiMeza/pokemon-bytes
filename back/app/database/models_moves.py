from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from sqlalchemy import Column, Integer, ForeignKey


class MoveBase(SQLModel):
    id: int
    name: str | None = Field(default=None)
    power: int | None = Field(default=None)
    accuracy: int | None = Field(default=None)
    power_points: int | None = Field(default=None)


class MovePublic(MoveBase):
    move_type: str | None = Field(default=None)
    generation: int | None = Field(default=None)
    category: str | None = Field(default=None)
    effect: str | None = Field(default=None)


# Models with table=True
class PokemonMove(SQLModel, table=True):
    __tablename__ = "pokemon_move"

    pokemon_id: int = Field(
        sa_column=Column(
            Integer, ForeignKey("pokemon.id", ondelete="CASCADE"), primary_key=True
        )
    )
    version_group_id: int = Field(primary_key=True)
    move_id: int = Field(primary_key=True, foreign_key="move.id")
    pokemon_move_method_id: int = Field(
        foreign_key="pokemon_move_method.pokemon_move_method_id", primary_key=True
    )
    level: int | None = Field(default=None, primary_key=True)
    order: int | None = Field(default=None)

    pokemon: Optional["Pokemon"] = Relationship(back_populates="pokemon_moves")
    move: Optional["Move"] = Relationship(back_populates="pokemon_moves")
    pokemon_move_method: Optional["PokemonMoveMethod"] = Relationship(
        back_populates="pokemon_moves"
    )


class Move(SQLModel, table=True):
    id: int = Field(primary_key=True)
    identifier: str | None = Field(default=None)
    generation_id: int | None = Field(default=None)
    type_id: int | None = Field(default=None, foreign_key="type.id")
    power: int | None = Field(default=None)
    pp: int | None = Field(default=None)
    accuracy: int | None = Field(default=None)
    priority: int | None = Field(default=None)
    target_id: int | None = Field(default=None)
    damage_class_id: int | None = Field(
        default=None, foreign_key="move_damage_class.id"
    )
    effect_id: int | None = Field(
        default=None, foreign_key="move_effect.move_effect_id"
    )
    effect_chance: int | None = Field(default=None)
    contest_type_id: int | None = Field(default=None)
    contest_effect_id: int | None = Field(default=None)
    super_contest_effect_id: int | None = Field(default=None)

    pokemon_moves: Optional[list[PokemonMove]] = Relationship(back_populates="move")
    move_names: Optional[list["MoveName"]] = Relationship(back_populates="move")
    effect: Optional["MoveEffect"] = Relationship(back_populates="moves")
    move_damage_class: Optional["MoveDamageClass"] = Relationship(
        back_populates="moves"
    )
    move_type: Optional["Type"] = Relationship(back_populates="move")
    team_member_moves: Optional[List["TeamMemberMove"]] = Relationship(
        back_populates="move"
    )


class MoveName(SQLModel, table=True):
    __tablename__ = "move_name"

    move_id: int = Field(primary_key=True, foreign_key="move.id")
    local_language_id: int = Field(primary_key=True)
    name: str

    move: Optional[Move] = Relationship(back_populates="move_names")


class MoveEffect(SQLModel, table=True):
    __tablename__ = "move_effect"

    move_effect_id: int = Field(primary_key=True)
    local_language_id: int
    short_effect: str
    effect: str

    moves: Optional[list[Move]] = Relationship(back_populates="effect")


class MoveDamageClass(SQLModel, table=True):  # Category
    __tablename__ = "move_damage_class"

    id: int = Field(primary_key=True)
    identifier: str

    moves: Optional[list[Move]] = Relationship(back_populates="move_damage_class")


class PokemonMoveMethod(SQLModel, table=True):
    __tablename__ = "pokemon_move_method"

    pokemon_move_method_id: int = Field(primary_key=True)
    local_language_id: int = Field(primary_key=True)
    name: str
    description: str

    pokemon_moves: Optional[list[PokemonMove]] = Relationship(
        back_populates="pokemon_move_method"
    )
