"""Crea relacion entre pokemon y pokemon_egg_group

Revision ID: 102ece4438ec
Revises: f2f813c0ed04
Create Date: 2024-11-03 16:00:19.714225

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "102ece4438ec"
down_revision: Union[str, None] = "f2f813c0ed04"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon") as batch_op:
        batch_op.create_foreign_key(
            "fk_pok_egg_group", "pokemon_egg_group", ["species_id"], ["species_id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("pokemon") as batch_op:
        batch_op.drop_constraint("fk_pok_egg_group", type_="foreignkey")
