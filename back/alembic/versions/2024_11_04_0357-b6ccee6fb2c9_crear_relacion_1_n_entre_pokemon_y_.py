"""Crear relacion 1:N entre pokemon y pokemon_move

Revision ID: b6ccee6fb2c9
Revises: 46a48b10142b
Create Date: 2024-11-04 03:57:19.972172

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "b6ccee6fb2c9"
down_revision: Union[str, None] = "46a48b10142b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_move") as batch_op:
        batch_op.create_foreign_key(
            "fk_pokemon_move_pokemon", "pokemon", ["pokemon_id"], ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("pokemon_move") as batch_op:
        batch_op.drop_constraint("fk_pokemon_move_pokemon", type_="foreignkey")
