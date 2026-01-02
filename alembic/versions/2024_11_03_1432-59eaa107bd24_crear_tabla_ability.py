"""Crear tabla Ability

Revision ID: 59eaa107bd24
Revises: cb5272dc7c4a
Create Date: 2024-11-03 14:32:36.709198

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "59eaa107bd24"
down_revision: Union[str, None] = "cb5272dc7c4a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ability",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("identifier", sa.Text(), nullable=False),
        sa.Column("generation", sa.Integer(), nullable=False),
        sa.Column("is_main_series", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("ability")
