"""fix: pk compuesta en pokemon types

Revision ID: 07cab2579c24
Revises: 465ca43fd7b1
Create Date: 2024-11-05 19:56:52.095479

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "07cab2579c24"
down_revision: Union[str, None] = "465ca43fd7b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_table("pokemon_type")
    op.create_table(
        "pokemon_type",
        sa.Column("pokemon_id", sa.Integer, nullable=False),
        sa.Column("type_id", sa.Integer, nullable=False),
        sa.Column("slot", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(["pokemon_id"], ["pokemon.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["type_id"], ["type.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("pokemon_id", "type_id"),
    )


def downgrade():
    op.drop_table("pokemon_type")
