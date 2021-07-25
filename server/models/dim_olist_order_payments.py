from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Numeric

from server import Base


class DimOlistOrderPayments(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_olist_order_payments
    """
    __tablename__ = "tb_dim_olist_order_payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String)
    payment_sequential = Column(Numeric(precision=18, scale=8))
    payment_type = Column(Integer)
    payment_installments = Column(Integer)
    payment_value = Column(Numeric(precision=18, scale=8))

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
            "product_category_name": str(self.product_category_name),
            "product_category_name_english": str(self.product_category_name_english),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "created_by": str(self.created_by),
            "updated_by": str(self.updated_by),
        }

    def fill_orm_with_event(self, event):
        self.order_id = event.get('order_id')
        self.payment_sequential = event.get('payment_sequential')
        self.payment_type = event.get('payment_type')
        self.payment_installments = event.get('payment_installments')
        self.payment_value = event.get('payment_value')
