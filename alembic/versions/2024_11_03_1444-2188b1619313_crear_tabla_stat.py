"""Crear tabla Stat

Revision ID: 2188b1619313
Revises: 346989180c52
Create Date: 2024-11-03 14:44:32.236501

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "2188b1619313"
down_revision: Union[str, None] = "346989180c52"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "stat",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("damage_class_id", sa.Integer()),
        sa.Column("identifier", sa.Text(), nullable=False),
        sa.Column("is_battle_only", sa.Integer(), nullable=False),
        sa.Column("game_index", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("stat")
