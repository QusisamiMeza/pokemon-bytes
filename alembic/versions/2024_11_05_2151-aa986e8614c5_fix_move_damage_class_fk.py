"""fix: move damage class fk

Revision ID: aa986e8614c5
Revises: 9bac75ea6c31
Create Date: 2024-11-05 21:51:29.318123

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "aa986e8614c5"
down_revision: Union[str, None] = "9bac75ea6c31"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table("move", schema=None) as batch_op:
        batch_op.drop_constraint("fk_damage_class_move", type_="foreignkey")
        batch_op.create_foreign_key(
            "fk_move_damage_class_corrected",
            "move_damage_class",
            ["damage_class_id"],
            ["id"],
        )


def downgrade():
    with op.batch_alter_table("move", schema=None) as batch_op:
        batch_op.drop_constraint("fk_move_damage_class_corrected", type_="foreignkey")
        batch_op.create_foreign_key(
            "fk_damage_class_move",
            "move_damage_class",
            ["damage_class_id"],
            ["id"],
        )
