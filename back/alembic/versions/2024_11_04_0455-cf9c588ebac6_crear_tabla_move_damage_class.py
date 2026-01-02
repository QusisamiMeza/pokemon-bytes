"""Crear tabla move_damage_class

Revision ID: cf9c588ebac6
Revises: d333b498caa2
Create Date: 2024-11-04 04:55:49.707820

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cf9c588ebac6"
down_revision: Union[str, None] = "d333b498caa2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "move_damage_class",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("identifier", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("move_damage_class")
