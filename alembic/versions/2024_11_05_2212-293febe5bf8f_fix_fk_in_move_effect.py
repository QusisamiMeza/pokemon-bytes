"""fix: fk in move effect

Revision ID: 293febe5bf8f
Revises: aa986e8614c5
Create Date: 2024-11-05 22:12:05.490968

"""

from typing import Sequence, Union

from alembic import op


revision: str = "293febe5bf8f"
down_revision: Union[str, None] = "aa986e8614c5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table("move", schema=None) as batch_op:
        batch_op.create_foreign_key(
            "fk_move_effect",
            "move_effect",
            ["effect_id"],
            ["move_effect_id"],
        )


def downgrade():
    with op.batch_alter_table("move", schema=None) as batch_op:
        batch_op.drop_constraint("fk_move_effect", type_="foreignkey")
