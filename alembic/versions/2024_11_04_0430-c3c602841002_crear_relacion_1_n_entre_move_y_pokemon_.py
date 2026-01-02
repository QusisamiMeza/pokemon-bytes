"""Crear relacion 1:N entre move y pokemon_move

Revision ID: c3c602841002
Revises: 1e1687eb1e13
Create Date: 2024-11-04 04:30:43.901517

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "c3c602841002"
down_revision: Union[str, None] = "1e1687eb1e13"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_move") as batch_op:
        batch_op.create_foreign_key("fk_move_pokemon_move", "move", ["move_id"], ["id"])


def downgrade() -> None:
    with op.batch_alter_table("pokemon_move") as batch_op:
        batch_op.drop_constraint("fk_move_pokemon_move", type_="foreignkey")
