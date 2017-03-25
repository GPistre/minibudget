from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
picture = Table('picture', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('pred_label', VARCHAR(length=140)),
    Column('confidence', FLOAT),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
    Column('image_main', TEXT),
    Column('image_sup1', TEXT),
    Column('image_sup2', TEXT),
    Column('image_sup3', TEXT),
)

picture = Table('picture', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('upload_id', Integer),
    Column('image', TEXT),
    Column('pred_label', String(length=140)),
    Column('confidence', Float),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['picture'].columns['image_main'].drop()
    pre_meta.tables['picture'].columns['image_sup1'].drop()
    pre_meta.tables['picture'].columns['image_sup2'].drop()
    pre_meta.tables['picture'].columns['image_sup3'].drop()
    post_meta.tables['picture'].columns['image'].create()
    post_meta.tables['picture'].columns['upload_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['picture'].columns['image_main'].create()
    pre_meta.tables['picture'].columns['image_sup1'].create()
    pre_meta.tables['picture'].columns['image_sup2'].create()
    pre_meta.tables['picture'].columns['image_sup3'].create()
    post_meta.tables['picture'].columns['image'].drop()
    post_meta.tables['picture'].columns['upload_id'].drop()
