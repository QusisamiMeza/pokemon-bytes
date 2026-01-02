"""Crear tabla move

Revision ID: 1e1687eb1e13
Revises: b6ccee6fb2c9
Create Date: 2024-11-04 04:21:22.769712

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1e1687eb1e13"
down_revision: Union[str, None] = "b6ccee6fb2c9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "move",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("identifier", sa.Text()),
        sa.Column("generation_id", sa.Integer()),
        sa.Column("type_id", sa.Integer()),
        sa.Column("power", sa.Integer()),
        sa.Column("pp", sa.Integer()),
        sa.Column("accuracy", sa.Integer()),
        sa.Column("priority", sa.Integer()),
        sa.Column("target_id", sa.Integer()),
        sa.Column("damage_class_id", sa.Integer()),
        sa.Column("effect_id", sa.Integer()),
        sa.Column("effect_chance", sa.Integer()),
        sa.Column("contest_type_id", sa.Integer()),
        sa.Column("contest_effect_id", sa.Integer()),
        sa.Column("super_contest_effect_id", sa.Integer()),
    )


def downgrade() -> None:
    op.drop_table("move")
