"""Crear relacion 1:N entre pokemon_move_method y pokemon_move

Revision ID: ac4c29c7a115
Revises: dfc32534ddd4
Create Date: 2024-11-04 05:27:26.155282

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "ac4c29c7a115"
down_revision: Union[str, None] = "dfc32534ddd4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_move") as batch_op:
        batch_op.create_foreign_key(
            "fk_move_method",
            "pokemon_move_method",
            ["pokemon_move_method_id"],
            ["pokemon_move_method_id"],
        )


def downgrade() -> None:
    with op.batch_alter_table("pokemon_move") as batch_op:
        batch_op.drop_constraint("fk_move_method", type_="foreignkey")
