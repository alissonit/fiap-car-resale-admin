"""init migr

Revision ID: 760431803706
Revises: 
Create Date: 2024-05-29 22:45:15.924784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '760431803706'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('car_user_id', sa.Integer(), nullable=True),
    sa.Column('car_brand', sa.String(), nullable=True),
    sa.Column('car_model', sa.String(), nullable=True),
    sa.Column('car_year', sa.Integer(), nullable=True),
    sa.Column('car_color', sa.String(), nullable=True),
    sa.Column('car_price', sa.Float(), nullable=True),
    sa.Column('car_type', sa.String(), nullable=True),
    sa.Column('car_condition', sa.String(), nullable=True),
    sa.Column('car_transmission', sa.String(), nullable=True),
    sa.Column('car_mileage', sa.Float(), nullable=True),
    sa.Column('car_engine', sa.Float(), nullable=True),
    sa.Column('car_fuel', sa.String(), nullable=True),
    sa.Column('car_description', sa.String(), nullable=True),
    sa.Column('car_armored', sa.Boolean(), nullable=True),
    sa.Column('car_sold', sa.Boolean(), nullable=True),
    sa.Column('car_created_at', sa.DateTime(), nullable=True),
    sa.Column('car_updated_at', sa.DateTime(), nullable=True),
    sa.Column('car_deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('car_id')
    )
    op.create_index(op.f('ix_cars_car_id'), 'cars', ['car_id'], unique=False)
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('user_email', sa.String(), nullable=True),
    sa.Column('user_password', sa.String(), nullable=True),
    sa.Column('user_phone', sa.String(), nullable=True),
    sa.Column('access_token', sa.String(), nullable=True),
    sa.Column('user_created_at', sa.DateTime(), nullable=True),
    sa.Column('user_updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_user_email'), 'users', ['user_email'], unique=False)
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=False)
    op.create_index(op.f('ix_users_user_name'), 'users', ['user_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_name'), table_name='users')
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_index(op.f('ix_users_user_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_cars_car_id'), table_name='cars')
    op.drop_table('cars')
    # ### end Alembic commands ###
