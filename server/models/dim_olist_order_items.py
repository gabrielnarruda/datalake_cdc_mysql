from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Numeric

from server import Base


class DimOlistOrderItems(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_olist_order_items
    """
    __tablename__ = "tb_dim_olist_order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String)
    order_item_id = Column(Integer)
    product_id = Column(String)
    seller_id = Column(String)
    price = Column(Numeric(precision=18, scale=8))
    freight_value = Column(Numeric(precision=18, scale=8))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_by = Column(String)
    updated_by = Column(String)

    def to_dict(self):
        return {
            "id": str(self.id),
            "order_id": str(self.order_id),
            "order_item_id": str(self.order_item_id),
            "product_id": str(self.product_id),
            "seller_id": str(self.seller_id),
            "price": str(self.price),
            "freight_value": str(self.freight_value),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "created_by": str(self.created_by),
            "updated_by": str(self.updated_by),
        }

    def fill_orm_with_event(self, event):
        self.order_id = event.get('order_id')
        self.order_item_id = event.get('order_item_id')
        self.product_id = event.get('product_id')
        self.seller_id = event.get('seller_id')
        self.price = event.get('price')
        self.freight_value = event.get('freight_value')
