from server import session
from server.models.dim_olist_customers import DimOlistCustomers
from server.models.dim_olist_geolocation import DimOlistGeolocation
from server.models.dim_olist_order_items import DimOlistOrderItems
from server.models.dim_olist_order_payments import DimOlistOrderPayments
from server.models.dim_olist_order_reviews import DimOlistOrderReviews
from server.models.dim_olist_orders import DimOlistOrders
from server.models.dim_olist_products import DimOlistProducts
from server.models.dim_olist_sellers import DimOlistSellers
from server.models.dim_product_category_name_translation import DimProductCategoryNameTranslation


class DimensionTables():
    """
    Classe responsavel por mapear as tabelas dimensão que se desejam trafegar atratravés dos ReplicationLogs.

    """
    def __init__(self):
        self.dimension_tables_mapping = {
            "product_category_name_translation": DimProductCategoryNameTranslation,
            'olist_sellers': DimOlistSellers,
            'olist_products': DimOlistProducts,
            'olist_orders': DimOlistOrders,
            'olist_order_reviews': DimOlistOrderReviews,
            'olist_order_payments': DimOlistOrderPayments,
            'olist_order_items': DimOlistOrderItems,
            'olist_geolocation': DimOlistGeolocation,
            'olist_customers': DimOlistCustomers
        }

    def handle_transactions_dimension_tables(self, event):
        """
        Função responsavel por gerenciar e endereçar os logs dos eventos Replication
        ::params::
        event: Evento Log disparado pelo banco de dados através do canal de Replication
        """
        table = event['table']
        table_orm = self.dimension_tables_mapping.get(table)
        table_dto = table_orm()
        event_values = event['values'][0]
        unique_filter = table_dto.unique_filter(event_values)
        query = session.query(table_orm).filter(*unique_filter)
        self.handle_event_action(event_values, query, table_dto, event['action'])

    def handle_event_action(self, event_values, query, table_dto, action):
        """
        Função responsável por transacionar o evento de Log baseado no tipo de ação executada (UPDATE,INSERT,DELETE)
        para a tabela dimensão alvo
        ::params::
        event_values: valores da transação do evento
        query: Objeto ORM referente ao evento em questão
        table_dto: Instancia ORM do tipo da tabela transacionada no evento
        action: tipo da ação executada na transação

        """
        db_dto = query.first()
        if action in ('update', 'insert'):
            if db_dto == None:
                table_dto.fill_orm_with_event(event_values)
                session.add(table_dto)
            else:
                db_dto.fill_orm_with_event(event_values)
                session.add(db_dto)
        if action == 'delete':
            query.delete()
        session.commit()
