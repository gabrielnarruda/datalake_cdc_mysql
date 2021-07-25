from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent

from server.configurations import environments_variables as env
from server.configurations.environments_variables import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_CONN
from server.configurations.logger import factory_logger
from server.services import utils

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


from sqlalchemy import Column, DateTime, Date, Numeric, Integer, create_engine, Boolean, String, UniqueConstraint

logger = factory_logger()

mysql_settings = {'host': DB_HOST, 'port': DB_PORT, 'user': DB_USER, 'passwd': DB_PASS}
stream = BinLogStreamReader(
    connection_settings=mysql_settings,
    server_id=3,
    only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent],
    only_schemas=['datasets_outsource'],
    resume_stream=True)

engine = create_engine(
    DB_CONN,
    max_overflow=5,
    pool_size=30,
    pool_timeout=60
)

Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()