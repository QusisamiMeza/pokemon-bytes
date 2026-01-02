"""fix: fk in pokemon to move method

Revision ID: 443306a4f5a5
Revises: c428a4064553
Create Date: 2024-11-05 23:36:34.419648

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "443306a4f5a5"
down_revision: Union[str, None] = "c428a4064553"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table("pokemon_move", recreate="always") as batch_op:
        batch_op.drop_constraint("fk_move_method", type_="foreignkey")
        batch_op.create_foreign_key(
            "fk_move_method",
            "pokemon_move_method",
            ["pokemon_move_method_id"],
            ["pokemon_move_method_id"],
        )


def downgrade():
    with op.batch_alter_table("pokemon_move", recreate="always") as batch_op:
        batch_op.drop_constraint("fk_move_method", type_="foreignkey")
        batch_op.create_foreign_key(
            "fk_move_method",
            "pokemonmovemethod",
            ["pokemon_move_method_id"],
            ["pokemon_move_method_id"],
        )
