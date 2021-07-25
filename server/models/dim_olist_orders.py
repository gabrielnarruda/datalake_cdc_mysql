from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from server import Base


class DimOlistOrders(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_olist_orders_dataset
    """
    __tablename__ = "tb_dim_olist_orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String)
    customer_id = Column(String)
    order_status = Column(String)
    order_purchase_timestamp = Column(DateTime)
    order_approved_at = Column(DateTime)
    order_delivered_carrier_date = Column(DateTime)
    order_delivered_customer_date = Column(DateTime)
    order_estimated_delivery_date = Column(DateTime)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_by = Column(String)
    updated_by = Column(String)

    def to_dict(self):
        """
        Código responsavel por retornar o objeto ORM em formato de dicionario. Pode ser utilizado para propagar a
        mensagem para algum outro canal ou broadcast
        """
        return {
            "id": str(self.id),
            "order_id": str(self.order_id),
            "customer_id": str(self.customer_id),
            "order_status": str(self.order_status),
            "order_purchase_timestamp": str(self.order_purchase_timestamp),
            "order_approved_at": str(self.order_approved_at),
            "order_delivered_carrier_date": str(self.order_delivered_carrier_date),
            "order_delivered_customer_date": str(self.order_delivered_customer_date),
            "order_estimated_delivery_date": str(self.order_estimated_delivery_date),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "created_by": str(self.created_by),
            "updated_by": str(self.updated_by),
        }

    def fill_orm_with_event(self, event):
        self.order_id = event.get('order_id')
        self.customer_id = event.get('customer_id')
        self.order_status = event.get('order_status')
        self.order_purchase_timestamp = event.get('order_purchase_timestamp')
        self.order_approved_at = event.get('order_approved_at')
        self.order_delivered_carrier_date = event.get('order_delivered_carrier_date')
        self.order_delivered_customer_date = event.get('order_delivered_customer_date')
        self.order_estimated_delivery_date = event.get('order_estimated_delivery_date')
