import os

KIBANA_SERVER = os.getenv("LOGSERVER")
ENVIRONMENT = os.getenv("ENVIRONMENT")
KINESIS_NAME = os.getenv("KINESIS_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT"))
DB_CONN = os.getenv("DB_CONN")

LOG_LEVEL = int(os.getenv("LOG_LEVEL", 10))
NOME_PROJETO_LOGGER = os.getenv("NOME_PROJETO_LOGGER")
THRESHOLD = os.getenv("THRESHOLD")
NUM_THREADS = os.getenv("NUM_THREADS")
TIME_SLEEP = os.getenv("TIME_SLEEP")
REPORTS_DBCONN = os.getenv("REPORTS_DBCONN")
