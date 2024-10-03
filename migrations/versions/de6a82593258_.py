"""empty message

Revision ID: de6a82593258
Revises: 7fda1d0d066f
Create Date: 2024-10-03 09:53:16.863249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de6a82593258'
down_revision = '7fda1d0d066f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('postulados', schema=None) as batch_op:
        batch_op.add_column(sa.Column('estado', sa.String(length=20), nullable=False))

    with op.batch_alter_table('programador', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating_value', sa.Float(precision=2), nullable=True))

    with op.batch_alter_table('proyectos', schema=None) as batch_op:
        batch_op.drop_constraint('proyectos_name_key', type_='unique')

    with op.batch_alter_table('ratings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('programador_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('empleador_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('ratings_to_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('ratings_from_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'programador', ['programador_id'], ['id'])
        batch_op.create_foreign_key(None, 'empleador', ['empleador_id'], ['id'])
        batch_op.drop_column('from_id')
        batch_op.drop_column('to_id')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone', sa.String(length=30), nullable=True))
        batch_op.create_unique_constraint(None, ['phone'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('phone')

    with op.batch_alter_table('ratings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('to_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('from_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('ratings_from_id_fkey', 'empleador', ['from_id'], ['id'])
        batch_op.create_foreign_key('ratings_to_id_fkey', 'programador', ['to_id'], ['id'])
        batch_op.drop_column('empleador_id')
        batch_op.drop_column('programador_id')

    with op.batch_alter_table('proyectos', schema=None) as batch_op:
        batch_op.create_unique_constraint('proyectos_name_key', ['name'])

    with op.batch_alter_table('programador', schema=None) as batch_op:
        batch_op.drop_column('rating_value')

    with op.batch_alter_table('postulados', schema=None) as batch_op:
        batch_op.drop_column('estado')

    # ### end Alembic commands ###
