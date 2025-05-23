"""initial commit

Revision ID: 85715930d790
Revises: 
Create Date: 2025-04-14 18:19:16.410261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85715930d790'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('topic', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_subject')),
    sa.UniqueConstraint('name', name=op.f('uq_subject_name')),
    sa.UniqueConstraint('topic', name=op.f('uq_subject_topic'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('umb_id', sa.String(length=8), nullable=False),
    sa.Column('role', sa.Enum('STUDENT', 'TUTOR', name='userrole'), nullable=False),
    sa.Column('last_message_read_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('umb_id', name=op.f('uq_user_umb_id'))
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('alert',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=140), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('source', sa.String(length=140), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], name=op.f('fk_alert_recipient_id_user')),
    sa.ForeignKeyConstraint(['subject'], ['user.id'], name=op.f('fk_alert_subject_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_alert'))
    )
    with op.batch_alter_table('alert', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_alert_category'), ['category'], unique=False)
        batch_op.create_index(batch_op.f('ix_alert_recipient_id'), ['recipient_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_alert_subject'), ['subject'], unique=False)
        batch_op.create_index(batch_op.f('ix_alert_timestamp'), ['timestamp'], unique=False)

    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('tutor_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('booking_date', sa.Date(), nullable=False),
    sa.Column('booking_time', sa.Time(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('last_updated_by', sa.Enum('STUDENT', 'TUTOR', name='userrole'), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], name=op.f('fk_appointment_student_id_user')),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk_appointment_subject_id_subject')),
    sa.ForeignKeyConstraint(['tutor_id'], ['user.id'], name=op.f('fk_appointment_tutor_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_appointment'))
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], name=op.f('fk_message_recipient_id_user')),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], name=op.f('fk_message_sender_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_message'))
    )
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_message_recipient_id'), ['recipient_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_message_sender_id'), ['sender_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_message_timestamp'), ['timestamp'], unique=False)

    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.Float(), nullable=False),
    sa.Column('payload_json', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_notification_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_notification'))
    )
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_notification_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_notification_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_notification_user_id'), ['user_id'], unique=False)

    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_post_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_post'))
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_user_id'), ['user_id'], unique=False)

    op.create_table('requested_subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], name=op.f('fk_requested_subject_student_id_user')),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk_requested_subject_subject_id_subject')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_requested_subject'))
    )
    op.create_table('user_subject',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], name=op.f('fk_user_subject_subject_id_subject')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_subject_user_id_user'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_subject')
    op.drop_table('requested_subject')
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_user_id'))
        batch_op.drop_index(batch_op.f('ix_post_timestamp'))

    op.drop_table('post')
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_notification_user_id'))
        batch_op.drop_index(batch_op.f('ix_notification_timestamp'))
        batch_op.drop_index(batch_op.f('ix_notification_name'))

    op.drop_table('notification')
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_message_timestamp'))
        batch_op.drop_index(batch_op.f('ix_message_sender_id'))
        batch_op.drop_index(batch_op.f('ix_message_recipient_id'))

    op.drop_table('message')
    op.drop_table('appointment')
    with op.batch_alter_table('alert', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_alert_timestamp'))
        batch_op.drop_index(batch_op.f('ix_alert_subject'))
        batch_op.drop_index(batch_op.f('ix_alert_recipient_id'))
        batch_op.drop_index(batch_op.f('ix_alert_category'))

    op.drop_table('alert')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('subject')
    # ### end Alembic commands ###
