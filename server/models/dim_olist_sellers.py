from datetime import datetime

from sqlalchemy import Column, DateTime, Numeric, Integer, String, UniqueConstraint

from server import Base


class DimOlistSellers(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_olist_sellers
    """
    __tablename__ = "tb_dim_olist_sellers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    seller_id = Column(String)
    seller_zip_code_prefix = Column(Numeric(precision=18, scale=8))
    seller_city = Column(String)
    seller_state = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_by = Column(String)
    updated_by = Column(String)


    def to_dict(self):
        return {
            "id": str(self.id),
            "seller_id": str(self.seller_id),
            "seller_zip_code_prefix": str(self.seller_zip_code_prefix),
            "seller_city": str(self.seller_city),
            "seller_state": str(self.seller_state),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "created_by": str(self.created_by),
            "updated_by": str(self.updated_by),
        }