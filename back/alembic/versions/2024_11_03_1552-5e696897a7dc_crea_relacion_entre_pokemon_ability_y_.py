"""Crea relacion entre pokemon_ability y ability

Revision ID: 5e696897a7dc
Revises: 60acfb5c6f61
Create Date: 2024-11-03 15:52:06.380189

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "5e696897a7dc"
down_revision: Union[str, None] = "60acfb5c6f61"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_ability") as batch_op:
        batch_op.create_foreign_key("fk_ability", "ability", ["ability_id"], ["id"])


def downgrade() -> None:
    with op.batch_alter_table("pokemon_ability") as batch_op:
        batch_op.drop_constraint("fk_ability", type_="foreignkey")
