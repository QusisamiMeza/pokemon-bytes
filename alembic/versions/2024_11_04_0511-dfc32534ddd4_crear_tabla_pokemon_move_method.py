"""Crear tabla pokemon_move_method

Revision ID: dfc32534ddd4
Revises: d6b108a9b642
Create Date: 2024-11-04 05:11:20.431732

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dfc32534ddd4"
down_revision: Union[str, None] = "d6b108a9b642"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pokemon_move_method",
        sa.Column("pokemon_move_method_id", sa.Integer(), nullable=False),
        sa.Column("local_language_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("pokemon_move_method_id", "local_language_id"),
    )


def downgrade() -> None:
    op.drop_table("pokemon_move_method")
