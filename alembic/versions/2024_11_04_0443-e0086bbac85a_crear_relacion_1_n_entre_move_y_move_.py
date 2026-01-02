"""Crear relacion 1:N entre move y move_name

Revision ID: e0086bbac85a
Revises: 6c99ce2ed3ae
Create Date: 2024-11-04 04:43:43.360883

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "e0086bbac85a"
down_revision: Union[str, None] = "6c99ce2ed3ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("move_name") as batch_op:
        batch_op.create_foreign_key("fk_move_name_move", "move", ["move_id"], ["id"])


def downgrade() -> None:
    with op.batch_alter_table("move_name") as batch_op:
        batch_op.drop_constraint("fk_move_name_move", type_="foreignkey")
