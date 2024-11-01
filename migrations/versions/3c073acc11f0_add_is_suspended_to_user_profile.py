"""Add is_suspended to user_profile

Revision ID: 3c073acc11f0
Revises: 
Create Date: 2024-10-19 12:39:44.750250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c073acc11f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_suspended', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profile', schema=None) as batch_op:
        batch_op.drop_column('is_suspended')

    # ### end Alembic commands ###