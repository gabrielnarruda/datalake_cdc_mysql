import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from cmreslogging.handlers import CMRESHandler

from server.configurations.environments_variables import ENVIRONMENT, KIBANA_SERVER, LOG_LEVEL, KINESIS_NAME, NOME_PROJETO_LOGGER

LOGGER_NAME = KINESIS_NAME


class UsernameFilter(logging.Filter):
    def filter(self, record):
        record.username = LOGGER_NAME
        return True


def factory_logger():
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.addFilter(UsernameFilter())
    file_logger(logger)
    stdout_logger(logger)
    elasticsearch_logger(logger)

    return logger


def get_logger():
    logger = logging.getLogger(LOGGER_NAME)
    return logger


def file_logger(logger):
    # Se o projeto estiver rodando no ambiente de desenvolvimento, os logs serão gerados locais
    if ENVIRONMENT == "DEV":
        if not os.path.exists("./logs"):
            os.makedirs("./logs")
        handler = RotatingFileHandler(
            f"./logs/{LOGGER_NAME}.log", mode="a", maxBytes=50000, backupCount=10, encoding="UTF-8"
        )
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s %(funcName)s [%(username)s] -> %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)


def stdout_logger(logger):
    # Os logs na saída do console sempre serão gerados
    logging_level = int(LOG_LEVEL)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging_level)
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s %(funcName)s [%(username)s] -> %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def elasticsearch_logger(logger):
    # Se o projeto estiver rodando no ambiente de UAT ou PROD, os logs serão gerados no elastic search
    if ENVIRONMENT in ['PRD', 'PROD', 'UAT']:
        nome_projeto = NOME_PROJETO_LOGGER

        handler = CMRESHandler(
            hosts=[{"host": KIBANA_SERVER, "port": 443}],
            auth_type=CMRESHandler.AuthType.NO_AUTH,
            use_ssl=True,
            es_index_name=nome_projeto,
            index_name_frequency=CMRESHandler.IndexNameFrequency.MONTHLY,
            es_additional_fields={"project": nome_projeto, "environment": ENVIRONMENT},
        )
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "[%(levelname)s] %(asctime)s %(funcName)s [%(username)s] -> %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)