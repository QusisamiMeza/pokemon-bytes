"""Crear tabla move_effect

Revision ID: a2c448ebe979
Revises: e0086bbac85a
Create Date: 2024-11-04 04:48:09.419709

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a2c448ebe979"
down_revision: Union[str, None] = "e0086bbac85a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "move_effect",
        sa.Column("move_effect_id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("local_language_id", sa.Integer()),
        sa.Column("short_effect", sa.Text()),
        sa.Column("effect", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("move_effect")
