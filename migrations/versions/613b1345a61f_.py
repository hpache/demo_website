"""empty message

Revision ID: 613b1345a61f
Revises: 
Create Date: 2021-11-13 12:56:30.382302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '613b1345a61f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('info_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('priority', sa.String(), nullable=True),
    sa.Column('tag', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('info_table')
    # ### end Alembic commands ###