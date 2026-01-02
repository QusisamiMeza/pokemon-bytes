"""Crear tabla pokemon_move

Revision ID: 46a48b10142b
Revises: 95b14c22e6fb
Create Date: 2024-11-04 03:43:22.160845

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "46a48b10142b"
down_revision: Union[str, None] = "95b14c22e6fb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pokemon_move",
        sa.Column("pokemon_id", sa.Integer(), nullable=False),
        sa.Column("version_group_id", sa.Integer(), nullable=False),
        sa.Column("move_id", sa.Integer(), nullable=False),
        sa.Column("pokemon_move_method_id", sa.Integer(), nullable=False),
        sa.Column("level", sa.Integer()),
        sa.Column("order", sa.Integer()),
        sa.PrimaryKeyConstraint(
            "pokemon_id", "version_group_id", "move_id", "pokemon_move_method_id"
        ),
    )


def downgrade() -> None:
    op.drop_table("pokemon_move")
