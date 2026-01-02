"""Crear tabla EggGroup

Revision ID: 14ea090e18d3
Revises: 452dc62b46c8
Create Date: 2024-11-03 14:49:18.241363

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "14ea090e18d3"
down_revision: Union[str, None] = "452dc62b46c8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "egg_group",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("identifier", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("egg_group")
