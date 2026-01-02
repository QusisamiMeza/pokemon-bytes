"""Crea relacion entre egg_group y pokemon_egg_group

Revision ID: 465ca43fd7b1
Revises: 102ece4438ec
Create Date: 2024-11-03 16:02:27.449717

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "465ca43fd7b1"
down_revision: Union[str, None] = "102ece4438ec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_egg_group") as batch_op:
        batch_op.create_foreign_key(
            "fk_egg_group", "egg_group", ["egg_group_id"], ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("pokemon_egg_group") as batch_op:
        batch_op.drop_constraint("fk_egg_group", type_="foreignkey")
