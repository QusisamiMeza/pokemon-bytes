"""Crear relacion 1:N entre type y move

Revision ID: 06ba8ecf64b1
Revises: 772c85ae2f16
Create Date: 2024-11-06 13:18:53.142524

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '06ba8ecf64b1'
down_revision: Union[str, None] = '772c85ae2f16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("move") as batch_op:
        batch_op.create_foreign_key("fk_move_type", "type", ["type_id"], ["id"])

def downgrade() -> None:
    with op.batch_alter_table("move") as batch_op:
        batch_op.drop_constraint("fk_move_type", type_="foreignkey")
