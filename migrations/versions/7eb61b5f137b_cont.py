"""'Cont'

Revision ID: 7eb61b5f137b
Revises: e0ae0e6a1b12
Create Date: 2023-03-20 21:30:05.977946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eb61b5f137b'
down_revision = 'e0ae0e6a1b12'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('additional_info', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=False)
    op.create_index(op.f('ix_contacts_first_name'), 'contacts', ['first_name'], unique=False)
    op.create_index(op.f('ix_contacts_id'), 'contacts', ['id'], unique=False)
    op.create_index(op.f('ix_contacts_last_name'), 'contacts', ['last_name'], unique=False)
    op.drop_index('ix_cats_description', table_name='cats')
    op.drop_index('ix_cats_id', table_name='cats')
    op.drop_index('ix_cats_nickname', table_name='cats')
    op.drop_table('cats')
    op.drop_index('ix_owners_email', table_name='owners')
    op.drop_index('ix_owners_id', table_name='owners')
    op.drop_table('owners')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('owners_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='owners_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_owners_id', 'owners', ['id'], unique=False)
    op.create_index('ix_owners_email', 'owners', ['email'], unique=False)
    op.create_table('cats',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nickname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vaccinated', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name='cats_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='cats_pkey')
    )
    op.create_index('ix_cats_nickname', 'cats', ['nickname'], unique=False)
    op.create_index('ix_cats_id', 'cats', ['id'], unique=False)
    op.create_index('ix_cats_description', 'cats', ['description'], unique=False)
    op.drop_index(op.f('ix_contacts_last_name'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_id'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_first_name'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.drop_table('contacts')
    # ### end Alembic commands ###
