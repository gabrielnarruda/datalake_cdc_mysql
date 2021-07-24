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
