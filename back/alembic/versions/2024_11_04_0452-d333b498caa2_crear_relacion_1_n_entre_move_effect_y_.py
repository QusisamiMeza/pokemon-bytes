"""Crear relacion 1:N entre move_effect y move

Revision ID: d333b498caa2
Revises: a2c448ebe979
Create Date: 2024-11-04 04:52:07.403643

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "d333b498caa2"
down_revision: Union[str, None] = "a2c448ebe979"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("move") as batch_op:
        batch_op.create_foreign_key(
            "fk_move_effect_move", "move_effect", ["effect_id"], ["move_effect_id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("move") as batch_op:
        batch_op.drop_constraint("fk_move_effect_move", type_="foreignkey")
