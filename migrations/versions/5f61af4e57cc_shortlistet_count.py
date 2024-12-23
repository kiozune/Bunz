"""shortlistet_count

Revision ID: 5f61af4e57cc
Revises: 68de87ab432d
Create Date: 2024-11-13 18:48:16.045923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f61af4e57cc'
down_revision = '68de87ab432d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('used_car_listing', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shortlisted_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('used_car_listing', schema=None) as batch_op:
        batch_op.drop_column('shortlisted_count')

    # ### end Alembic commands ###
