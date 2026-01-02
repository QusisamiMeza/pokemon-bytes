"""Add ondelete cascade to foreign keys

Revision ID: 2dddc7d48232
Revises: 06ba8ecf64b1
Create Date: 2024-11-27 22:53:47.763891

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2dddc7d48232"
down_revision: Union[str, None] = "06ba8ecf64b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop existing tables
    op.drop_table('team_member_type')
    op.drop_table('team_member_move')
    op.drop_table('team_member_stat')

    # Recreate team_member_type table with cascading foreign keys
    op.create_table(
        'team_member_type',
        sa.Column('team_member_id', sa.Integer, nullable=False),
        sa.Column('type_id', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('team_member_id', 'type_id'),
        sa.ForeignKeyConstraint(['team_member_id'], ['team_member.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['type_id'], ['type.id'], ondelete='CASCADE'),
    )

    # Recreate team_member_move table with cascading foreign keys
    op.create_table(
        'team_member_move',
        sa.Column('team_member_id', sa.Integer, nullable=False),
        sa.Column('move_id', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('team_member_id', 'move_id'),
        sa.ForeignKeyConstraint(['team_member_id'], ['team_member.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['move_id'], ['move.id'], ondelete='CASCADE'),
    )

    # Recreate team_member_stat table with cascading foreign keys
    op.create_table(
        'team_member_stat',
        sa.Column('team_member_id', sa.Integer, nullable=False),
        sa.Column('stat_id', sa.Integer, nullable=False),
        sa.Column('stat_value', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('team_member_id', 'stat_id'),
        sa.ForeignKeyConstraint(['team_member_id'], ['team_member.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['stat_id'], ['stat.id'], ondelete='CASCADE'),
    )


def downgrade() -> None:
    # Drop newly created tables
    op.drop_table('team_member_type')
    op.drop_table('team_member_move')
    op.drop_table('team_member_stat')

    # Recreate the original team_member_type table without cascading foreign keys
    op.create_table(
        'team_member_type',
        sa.Column('team_member_id', sa.Integer, nullable=False),
        sa.Column('type_id', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('team_member_id', 'type_id'),
        sa.ForeignKeyConstraint(['team_member_id'], ['team_member.id']),
        sa.ForeignKeyConstraint(['type_id'], ['type.id']),
    )

    # Recreate the original team_member_move table without cascading foreign keys
    op.create_table(
        'team_member_move',
        sa.Column('team_member_id', sa.Integer, nullable=False),
        sa.Column('move_id', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('team_member_id', 'move_id'),
        sa.ForeignKeyConstraint(['team_member_id'], ['team_member.id']),
        sa.ForeignKeyConstraint(['move_id'], ['move.id']),
    )

    # Recreate the original team_member_stat table without cascading foreign keys
    op.create_table(
        'team_member_stat',
        sa.Column('team_member_id', sa.Integer, nullable=False),
        sa.Column('stat_id', sa.Integer, nullable=False),
        sa.Column('stat_value', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('team_member_id', 'stat_id'),
        sa.ForeignKeyConstraint(['team_member_id'], ['team_member.id']),
        sa.ForeignKeyConstraint(['stat_id'], ['stat.id']),
    )
    