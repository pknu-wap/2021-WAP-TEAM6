"""empty message

Revision ID: 59306b23e856
Revises: 
Create Date: 2021-05-31 14:53:05.097725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59306b23e856'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transfer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('img1_name', sa.String(length=300), nullable=True),
    sa.Column('img1', sa.LargeBinary(), nullable=True),
    sa.Column('mimetype1', sa.String(length=100), nullable=True),
    sa.Column('img2_name', sa.String(length=300), nullable=True),
    sa.Column('img2', sa.LargeBinary(), nullable=True),
    sa.Column('mimetype2', sa.String(length=100), nullable=True),
    sa.Column('img3_name', sa.String(length=300), nullable=True),
    sa.Column('img3', sa.LargeBinary(), nullable=True),
    sa.Column('mimetype3', sa.String(length=100), nullable=True),
    sa.Column('img4_name', sa.String(length=300), nullable=True),
    sa.Column('img4', sa.LargeBinary(), nullable=True),
    sa.Column('mimetype4', sa.String(length=100), nullable=True),
    sa.Column('img5_name', sa.String(length=300), nullable=True),
    sa.Column('img5', sa.LargeBinary(), nullable=True),
    sa.Column('mimetype5', sa.String(length=100), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('nickname', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=64), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('stu_name', sa.String(length=300), nullable=True),
    sa.Column('stu', sa.LargeBinary(), nullable=True),
    sa.Column('mimetype', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname'),
    sa.UniqueConstraint('nickname'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('S__answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['search_id'], ['search.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('T__answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transfer_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['transfer_id'], ['transfer.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('T__answer')
    op.drop_table('S__answer')
    op.drop_table('user')
    op.drop_table('transfer')
    op.drop_table('search')
    # ### end Alembic commands ###
