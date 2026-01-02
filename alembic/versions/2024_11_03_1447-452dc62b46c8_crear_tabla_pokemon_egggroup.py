"""Crear tabla Pokemon EggGroup

Revision ID: 452dc62b46c8
Revises: 2188b1619313
Create Date: 2024-11-03 14:47:00.051630

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "452dc62b46c8"
down_revision: Union[str, None] = "2188b1619313"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pokemon_egg_group",
        sa.Column("species_id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("egg_group_id", sa.Integer(), primary_key=True, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("pokemon_egg_group")
