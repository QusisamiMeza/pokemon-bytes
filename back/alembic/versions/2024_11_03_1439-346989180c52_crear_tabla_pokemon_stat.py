"""Crear tabla Pokemon Stat

Revision ID: 346989180c52
Revises: 59eaa107bd24
Create Date: 2024-11-03 14:39:46.180147

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "346989180c52"
down_revision: Union[str, None] = "59eaa107bd24"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pokemon_stat",
        sa.Column("pokemon_id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("stat_id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("base_stat", sa.Integer(), nullable=False),
        sa.Column("effort", sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("pokemon_stat")
