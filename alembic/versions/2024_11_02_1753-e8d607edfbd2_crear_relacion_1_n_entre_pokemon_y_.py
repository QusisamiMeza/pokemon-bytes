"""Crear relacion 1:N entre pokemon y pokemon_type

Revision ID: e8d607edfbd2
Revises: 80d8e33cf1d7
Create Date: 2024-11-02 17:53:06.498747

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "e8d607edfbd2"
down_revision: Union[str, None] = "80d8e33cf1d7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_type") as batch_op:
        batch_op.create_foreign_key(
            "fk_pokemon_type_pokemon", "pokemon", ["pokemon_id"], ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("pokemon_type") as batch_op:
        batch_op.drop_constraint("fk_pokemon_type_pokemon", type_="foreignkey")
