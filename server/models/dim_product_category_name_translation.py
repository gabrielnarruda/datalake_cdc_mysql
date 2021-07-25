from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from server import Base


class DimProductCategoryNameTranslation(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_product_category_name_translation
    """
    __tablename__ = "tb_dim_product_category_name_translation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_category_name = Column(String)
    product_category_name_english = Column(String)

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
        self.product_category_name = event.get('product_category_name')
        self.product_category_name_english = event.get('product_category_name_english')
