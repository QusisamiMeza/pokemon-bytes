"""fix: unique constraints in pokemon moves

Revision ID: c428a4064553
Revises: 293febe5bf8f
Create Date: 2024-11-05 22:29:21.060326

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c428a4064553"
down_revision: Union[str, None] = "293febe5bf8f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_table("pokemon_move")
    op.create_table(
        "pokemon_move",
        sa.Column("pokemon_id", sa.Integer(), nullable=False),
        sa.Column("version_group_id", sa.Integer(), nullable=False),
        sa.Column("move_id", sa.Integer(), nullable=False),
        sa.Column("pokemon_move_method_id", sa.Integer(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("order", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint(
            "pokemon_id",
            "version_group_id",
            "move_id",
            "pokemon_move_method_id",
            "level",
            name="pk_pokemon_move",
        ),
        sa.ForeignKeyConstraint(
            ["pokemon_id"], ["pokemon.id"], name="fk_pokemon_move_pokemon"
        ),
        sa.ForeignKeyConstraint(["move_id"], ["move.id"], name="fk_move_pokemon_move"),
        sa.ForeignKeyConstraint(
            ["pokemon_move_method_id"],
            ["pokemon_move_method.pokemon_move_method_id"],
            name="fk_move_method",
        ),
    )


def downgrade():
    op.drop_table("pokemon_move")
    op.create_table(
        "pokemon_move",
        sa.Column("pokemon_id", sa.Integer(), nullable=False),
        sa.Column("version_group_id", sa.Integer(), nullable=False),
        sa.Column("move_id", sa.Integer(), nullable=False),
        sa.Column("pokemon_move_method_id", sa.Integer(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=True),
        sa.Column("order", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint(
            "pokemon_id",
            "version_group_id",
            "move_id",
            "pokemon_move_method_id",
            name="pk_pokemon_move",
        ),
        sa.ForeignKeyConstraint(
            ["pokemon_id"], ["pokemon.id"], name="fk_pokemon_move_pokemon"
        ),
        sa.ForeignKeyConstraint(["move_id"], ["move.id"], name="fk_move_pokemon_move"),
        sa.ForeignKeyConstraint(
            ["pokemon_move_method_id"],
            ["pokemon_move_method.pokemon_move_method_id"],
            name="fk_move_method",
        ),
    )
