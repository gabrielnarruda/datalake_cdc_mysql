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
        """
        Código responsavel por retornar o objeto ORM em formato de dicionario. Pode ser utilizado para propagar a
        mensagem para algum outro canal ou broadcast
        """
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

    def fill_orm_with_event(self, event):
        self.seller_id = event.get('seller_id')
        self.seller_state = event.get('seller_state')
        self.seller_city = event.get('seller_city')
        self.seller_zip_code_prefix = event.get('seller_zip_code_prefix')

    def unique_filter(self, event):
        """
        Função destinada a filtrar registro da tabela dimensão para saber se é um registro novo ou já algum registro antigo
        na tabela. Se todas os atributos forem adicionados ao filtro, a tabela passará ter todos os dados históricos de uma mesma PK.
        Caso apenas a PK seja utilizada como filtro, exestirá apenas um registro para a mesma, que será sobrescrito a cada novo evento

        """
        filter_list = []
        filter_list.append(DimOlistSellers.seller_id == event.get('seller_id'))
        # filter_list.append(DimOlistSellers.seller_state == event.get('seller_state'))
        # filter_list.append(DimOlistSellers.seller_city == event.get('seller_city'))
        # filter_list.append(DimOlistSellers.seller_zip_code_prefix == event.get('seller_zip_code_prefix'))
        return filter_list
