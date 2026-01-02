"""se crea el modelo pokemon_type

Revision ID: 1f610b98b4a6
Revises: 728e631c4dd9
Create Date: 2024-11-02 17:32:34.859234

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1f610b98b4a6"
down_revision: Union[str, None] = "728e631c4dd9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "pokemon_type",
        sa.Column("pokemon_id", sa.Integer(), nullable=False),
        sa.Column("type_id", sa.Integer(), nullable=False),
        sa.Column("slot", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pokemon_id"],
            ["pokemon.id"],
        ),
        sa.ForeignKeyConstraint(
            ["type_id"],
            ["type.id"],
        ),
        sa.PrimaryKeyConstraint("pokemon_id"),
    )


def downgrade() -> None:
    op.drop_table("pokemon_type")
