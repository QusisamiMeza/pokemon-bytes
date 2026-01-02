"""Crear relacion 1:N entre pokemon_type y type

Revision ID: f3fb7fa6d4fb
Revises: e8d607edfbd2
Create Date: 2024-11-02 17:58:11.218368

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "f3fb7fa6d4fb"
down_revision: Union[str, None] = "e8d607edfbd2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("pokemon_type") as batch_op:
        batch_op.create_foreign_key(
            "fk_pokemon_type_type_id", "type", ["type_id"], ["type_id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("pokemon_type") as batch_op:
        batch_op.drop_constraint("fk_pokemon_type_type_id", type_="foreignkey")
