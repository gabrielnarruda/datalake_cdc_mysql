from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Numeric

from server import Base


class DimOlistOrderReviews(Base):
    """
    Classe ORM responsável pela interface da tabela dimensão tb_dim_olist_order_reviews

    """
    __tablename__ = "tb_dim_olist_order_reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    review_id = Column(String)
    order_id = Column(String)
    review_score = Column(Numeric(precision=18, scale=8))
    review_comment_title = Column(String)
    review_comment_message = Column(String)
    review_creation_date = Column(DateTime)
    review_answer_timestamp = Column(DateTime)

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
            "review_id": str(self.review_id),
            "order_id": str(self.order_id),
            "review_score": str(self.review_score),
            "review_comment_title": str(self.review_comment_title),
            "review_comment_message": str(self.review_id),
            "review_creation_date": str(self.order_id),
            "review_answer_timestamp": str(self.review_score),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "created_by": str(self.created_by),
            "updated_by": str(self.updated_by),
        }

    def fill_orm_with_event(self, event):
        self.review_id = event.get('review_id')
        self.order_id = event.get('order_id')
        self.review_score = event.get('review_score')
        self.review_comment_title = event.get('review_comment_title')
        self.review_comment_message = event.get('review_comment_message')
        self.review_creation_date = event.get('review_creation_date')
        self.review_answer_timestamp = event.get('review_answer_timestamp')

    def unique_filter(self, event):
        """
        Função destinada a filtrar registro da tabela dimensão para saber se é um registro novo ou já algum registro antigo
        na tabela. Se todas os atributos forem adicionados ao filtro, a tabela passará ter todos os dados históricos de uma mesma PK.
        Caso apenas a PK seja utilizada como filtro, exestirá apenas um registro para a mesma, que será sobrescrito a cada novo evento

        """
        filter_list = []
        filter_list.append(DimOlistOrderReviews.review_id == event.get('review_id'))
        # filter_list.append(DimOlistOrderReviews.order_id == event.get('order_id'))
        # filter_list.append(DimOlistOrderReviews.review_score == event.get('review_score'))
        # filter_list.append(DimOlistOrderReviews.review_comment_title == event.get('review_comment_title'))
        # filter_list.append(DimOlistOrderReviews.review_comment_message == event.get('review_comment_message'))
        # filter_list.append(DimOlistOrderReviews.review_creation_date == event.get('review_creation_date'))
        # filter_list.append(DimOlistOrderReviews.review_answer_timestamp == event.get('review_answer_timestamp'))

        return filter_list
