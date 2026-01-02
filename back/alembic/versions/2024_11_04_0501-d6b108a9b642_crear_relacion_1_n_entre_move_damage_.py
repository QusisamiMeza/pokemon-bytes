"""Crear relacion 1:N entre move_damage_class y move

Revision ID: d6b108a9b642
Revises: cf9c588ebac6
Create Date: 2024-11-04 05:01:58.182067

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "d6b108a9b642"
down_revision: Union[str, None] = "cf9c588ebac6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("move") as batch_op:
        batch_op.create_foreign_key(
            "fk_damage_class_move", "move_damage_class", ["damage_class_id"], ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("move") as batch_op:
        batch_op.drop_constraint("fk_damage_class_move", type_="foreignkey")
