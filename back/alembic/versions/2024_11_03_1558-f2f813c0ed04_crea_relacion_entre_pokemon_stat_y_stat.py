"""Crea relacion entre pokemon_stat y stat

Revision ID: f2f813c0ed04
Revises: dde88d46d6b6
Create Date: 2024-11-03 15:58:22.074280

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "f2f813c0ed04"
down_revision: Union[str, None] = "dde88d46d6b6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_stat") as batch_op:
        batch_op.create_foreign_key("fk_stat", "stat", ["stat_id"], ["id"])


def downgrade() -> None:
    with op.batch_alter_table("pokemon_stat") as batch_op:
        batch_op.drop_constraint("fk_stat", type_="foreignkey")
