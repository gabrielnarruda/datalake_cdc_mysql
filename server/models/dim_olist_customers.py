from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Numeric

from server import Base


class DimOlistCustomers(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_olist_customers
    """
    __tablename__ = "tb_dim_olist_customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String)
    customer_unique_id = Column(Integer)
    customer_zip_code_prefix = Column(Integer)
    customer_city = Column(String)
    customer_state = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_by = Column(String)
    updated_by = Column(String)

    def to_dict(self):
        return {
            "id": str(self.id),
            "customer_id": str(self.customer_id),
            "customer_unique_id": str(self.customer_unique_id),
            "customer_zip_code_prefix": str(self.customer_zip_code_prefix),
            "customer_city": str(self.customer_city),
            "customer_state": str(self.customer_state),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "created_by": str(self.created_by),
            "updated_by": str(self.updated_by),
        }