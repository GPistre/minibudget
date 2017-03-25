from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
picture = Table('picture', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('image_main', TEXT),
    Column('image_sup1', TEXT),
    Column('image_sup2', TEXT),
    Column('image_sup3', TEXT),
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
    post_meta.tables['picture'].columns['image_main'].create()
    post_meta.tables['picture'].columns['image_sup1'].create()
    post_meta.tables['picture'].columns['image_sup2'].create()
    post_meta.tables['picture'].columns['image_sup3'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['picture'].columns['image_main'].drop()
    post_meta.tables['picture'].columns['image_sup1'].drop()
    post_meta.tables['picture'].columns['image_sup2'].drop()
    post_meta.tables['picture'].columns['image_sup3'].drop()
