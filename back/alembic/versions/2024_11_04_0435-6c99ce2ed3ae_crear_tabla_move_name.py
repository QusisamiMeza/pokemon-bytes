"""Crear tabla move_name

Revision ID: 6c99ce2ed3ae
Revises: c3c602841002
Create Date: 2024-11-04 04:35:40.751114

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6c99ce2ed3ae"
down_revision: Union[str, None] = "c3c602841002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "move_name",
        sa.Column("move_id", sa.Integer(), nullable=False),
        sa.Column("local_language_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text()),
        sa.PrimaryKeyConstraint("move_id", "local_language_id"),
    )


def downgrade() -> None:
    op.drop_table("move_name")
