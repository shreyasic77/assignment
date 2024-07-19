from __future__ import with_statement

import sys
import os
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection
from sqlalchemy.orm import sessionmaker
from alembic import context

from main import Base  # Import Base from your FastAPI app

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    engine = create_engine(config.get_main_option("sqlalchemy.url"))
    connection = engine.connect()
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
