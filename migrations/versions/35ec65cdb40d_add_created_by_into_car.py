"""add created_by into car

Revision ID: 35ec65cdb40d
Revises: a4d357c66e65
Create Date: 2024-11-11 17:39:22.145711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ec65cdb40d'
down_revision = 'a4d357c66e65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('used_car_listing', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_by', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user_account', ['created_by'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('used_car_listing', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('created_by')

    # ### end Alembic commands ###
