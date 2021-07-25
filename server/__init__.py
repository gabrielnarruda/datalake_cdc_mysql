from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from server.configurations import environments_variables as env
from server.configurations.environments_variables import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_CONN
from server.configurations.logger import factory_logger
from server.services import utils

# Suite de Logging para envio de logs a servidor Elasticsearch.
# É importante que a aplicação seja logada para que um monitoramento efeciente possa ser efetuado
logger = factory_logger()

# Configuração Canal de eventos replication.
# Através do parametro 'only_schemas' da classe BinLogStreamReader é possível filtrar quais schemas serão considerados
# para transação de seus Logs. Considerou-se que os dados do datasets do Kaggle advém de um schema diferente de onde estão
# alocadas as tabelas dimensão.
mysql_settings = {'host': DB_HOST, 'port': DB_PORT, 'user': DB_USER, 'passwd': DB_PASS}
stream = BinLogStreamReader(
    connection_settings=mysql_settings,
    server_id=3,
    only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent],
    only_schemas=['datasets_outsource'],
    resume_stream=True)

# Configuração Engine de banco de dados para interface de ORM
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
