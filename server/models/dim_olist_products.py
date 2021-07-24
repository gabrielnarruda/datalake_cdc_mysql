from server import Base
from sqlalchemy import Column, DateTime, Date, Numeric, Integer, create_engine, Boolean, String, UniqueConstraint
from datetime import datetime

class DimOlistProducts(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_olist_products

    """
    __tablename__ = "tb_dim_olist_products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(String)
    product_category_name = Column(String)
    product_name_lenght=Column(Numeric(precision=18, scale=8))
    product_description_lenght = Column(Numeric(precision=18, scale=8))
    product_photos_qty = Column(Numeric(precision=18, scale=8))
    product_weight_g = Column(Numeric(precision=18, scale=8))
    product_length_cm = Column(Numeric(precision=18, scale=8))
    product_height_cm = Column(Numeric(precision=18, scale=8))
    product_width_cm = Column(Numeric(precision=18, scale=8))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_by = Column(String)
    updated_by = Column(String)

    def to_dict(self):
        return {
            "id": str(self.id),
            "product_id": str(self.product_id),
            "product_category_name": str(self.product_category_name),
            "product_name_lenght": str(self.id),
            "product_description_lenght": str(self.product_id),
            "product_photos_qty": str(self.product_category_name),
            "product_weight_g": str(self.product_category_name),
            "product_length_cm": str(self.id),
            "product_height_cm": str(self.product_id),
            "product_width_cm": str(self.product_category_name),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "created_by": str(self.created_by),
            "updated_by": str(self.updated_by),
        }