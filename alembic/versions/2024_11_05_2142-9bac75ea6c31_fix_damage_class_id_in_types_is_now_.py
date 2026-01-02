"""fix: damage class id in types is now nullable

Revision ID: 9bac75ea6c31
Revises: 07cab2579c24
Create Date: 2024-11-05 21:42:07.051237

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "9bac75ea6c31"
down_revision: Union[str, None] = "07cab2579c24"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table("type", schema=None) as batch_op:
        batch_op.alter_column("damage_class_id", nullable=True)


def downgrade():
    with op.batch_alter_table("type", schema=None) as batch_op:
        batch_op.alter_column("damage_class_id", nullable=False)
