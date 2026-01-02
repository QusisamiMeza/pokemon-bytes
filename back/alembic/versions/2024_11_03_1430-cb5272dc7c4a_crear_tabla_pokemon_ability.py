"""Crear tabla Pokemon Ability

Revision ID: cb5272dc7c4a
Revises: 95b14c22e6fb
Create Date: 2024-11-03 14:30:12.138943

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cb5272dc7c4a"
down_revision: Union[str, None] = "d8308119d0dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pokemon_ability",
        sa.Column("pokemon_id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("ability_id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("is_hidden", sa.Integer(), nullable=False),
        sa.Column("slot", sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("pokemon_ability")
