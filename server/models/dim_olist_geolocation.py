from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Numeric

from server import Base


class DimOlistGeolocation(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_olist_geolocation


    """
    __tablename__ = "tb_dim_olist_geolocation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    geolocation_zip_code_prefix = Column(Numeric(precision=18, scale=8))
    geolocation_lat = Column(Numeric(precision=18, scale=8))
    geolocation_lng = Column(Numeric(precision=18, scale=8))
    geolocation_city = Column(String)
    geolocation_state = Column(String)
    freight_value = Column(Numeric(precision=18, scale=8))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    created_by = Column(String)
    updated_by = Column(String)

    def to_dict(self):
        return {
            "id": str(self.id),
            "geolocation_zip_code_prefix": str(self.geolocation_zip_code_prefix),
            "geolocation_lat": str(self.geolocation_lat),
            "geolocation_lng": str(self.geolocation_lng),
            "geolocation_city": str(self.geolocation_city),
            "geolocation_state": str(self.geolocation_state),
            "freight_value": str(self.freight_value),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "created_by": str(self.created_by),
            "updated_by": str(self.updated_by),
        }

    def fill_orm_with_event(self, event):
        self.geolocation_zip_code_prefix = event.get('geolocation_zip_code_prefix')
        self.geolocation_lat = event.get('geolocation_lat')
        self.geolocation_lng = event.get('geolocation_lng')
        self.geolocation_city = event.get('geolocation_city')
        self.geolocation_state = event.get('geolocation_state')
        self.freight_value = event.get('freight_value')
