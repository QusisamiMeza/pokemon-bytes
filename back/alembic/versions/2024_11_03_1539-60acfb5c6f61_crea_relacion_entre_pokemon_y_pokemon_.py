"""Crea relacion entre pokemon y pokemon_ability

Revision ID: 60acfb5c6f61
Revises: 14ea090e18d3
Create Date: 2024-11-03 15:39:48.925401

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "60acfb5c6f61"
down_revision: Union[str, None] = "14ea090e18d3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_ability") as batch_op:
        batch_op.create_foreign_key("fk_pok_ability", "pokemon", ["pokemon_id"], ["id"])


def downgrade() -> None:
    with op.batch_alter_table("pokemon_ability") as batch_op:
        batch_op.drop_constraint("fk_pok_ability", type_="foreignkey")
