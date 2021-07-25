import json
import sys

from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent

from server.services.dimension_tables_api import DimensionTables


class Consumer(DimensionTables):
    """Classe responsável por coletar e tracionar os eventos de transações do banco de dados onde os dados serão
    incrementados diariamente. Esta classe recebe """

    def __init__(self, stream):
        self.stream = stream
        DimensionTables.__init__(self)

    def consume_stream(self):
        for binlogevent in self.stream:
            for row in binlogevent.rows:
                event = {"schema": binlogevent.schema,
                         "table": binlogevent.table,
                         "timestamp": binlogevent.timestamp}
                event = self.event_structor(event, binlogevent, row)
                self.populate_dimension_tables(event)

    def event_structor(self, event, binlogevent, row):
        if isinstance(binlogevent, DeleteRowsEvent):
            event["action"] = "delete"
            event.update({'values': [row["values"]]})
        elif isinstance(binlogevent, UpdateRowsEvent):
            event["action"] = "update"
            event.update({'values': [row["values"]]})
        elif isinstance(binlogevent, WriteRowsEvent):
            event["action"] = "insert"
            event.update({'values': [row["values"]]})
        # print(json.dumps(event))
        sys.stdout.flush()
        return event
