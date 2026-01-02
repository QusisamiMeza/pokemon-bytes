"""fix: pk in egg group

Revision ID: 216d8376764f
Revises: 443306a4f5a5
Create Date: 2024-11-05 23:54:58.095764

"""

from typing import Sequence, Union

from alembic import op


revision: str = "216d8376764f"
down_revision: Union[str, None] = "443306a4f5a5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table("pokemon_egg_group", recreate="always") as batch_op:
        batch_op.drop_constraint("fk_egg_group", type_="foreignkey")
        batch_op.create_foreign_key(
            "fk_egg_group",
            "egg_group",
            ["egg_group_id"],
            ["id"],
        )


def downgrade():
    with op.batch_alter_table("pokemon_egg_group", recreate="always") as batch_op:
        batch_op.drop_constraint("fk_egg_group", type_="foreignkey")
        batch_op.create_foreign_key(
            "fk_egg_group",
            "egggroup",
            ["egg_group_id"],
            ["id"],
        )
