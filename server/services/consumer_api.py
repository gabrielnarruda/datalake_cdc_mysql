import json
import sys

from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent

from server import logger
from server.services.dimension_tables_api import DimensionTables


class Consumer(DimensionTables):
    """Classe responsável por coletar e tracionar os eventos de transações do banco de dados onde os dados serão
    incrementados diariamente. Esta classe recebe eventos Replication do banco de dados em tempo real """

    def __init__(self, stream):
        self.stream = stream
        DimensionTables.__init__(self)

    def consume_stream(self):
        """
        Função responsavel por consumir os eventos disparados pelo Replication do banco de dados
        """
        for binlogevent in self.stream:
            for row in binlogevent.rows:
                event = {"schema": binlogevent.schema,
                         "table": binlogevent.table,
                         "timestamp": binlogevent.timestamp}
                event = self.event_structor(event, binlogevent, row)
                self.handle_transactions_dimension_tables(event)

    def event_structor(self, event, binlogevent, row):
        """
        Função responsavel por estruturar evento Log Replication para que se possa transaciona-lo na aplicação
        ::params::
        event: Dicionario base para estruturação de evento para a aplicação
        binlogevent: Objeto de Log Binário do banco de dados
        row: linha com os dados do evento  do banco de dados
        """
        if isinstance(binlogevent, DeleteRowsEvent):
            event["action"] = "delete"
            event.update({'values': [row["values"]]})
        elif isinstance(binlogevent, UpdateRowsEvent):
            event["action"] = "update"
            event.update({'values': [row["after_values"]]})
        elif isinstance(binlogevent, WriteRowsEvent):
            event["action"] = "insert"
            event.update({'values': [row["values"]]})
        logger.info(f'{event}')
        sys.stdout.flush()
        return event
