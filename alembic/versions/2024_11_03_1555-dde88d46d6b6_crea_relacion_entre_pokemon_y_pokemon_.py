"""Crea relacion entre pokemon y pokemon_stat

Revision ID: dde88d46d6b6
Revises: 5e696897a7dc
Create Date: 2024-11-03 15:55:18.167864

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "dde88d46d6b6"
down_revision: Union[str, None] = "5e696897a7dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_stat") as batch_op:
        batch_op.create_foreign_key("fk_pok_stat", "pokemon", ["pokemon_id"], ["id"])


def downgrade() -> None:
    with op.batch_alter_table("pokemon_stat") as batch_op:
        batch_op.drop_constraint("fk_pok_stat", type_="foreignkey")
