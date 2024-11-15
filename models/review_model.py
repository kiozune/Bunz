from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import db  # Import db instance
from sqlalchemy.exc import IntegrityError

class Review(db.Model):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)  # FK to UserAccount
    rating = Column(Integer, nullable=False)
    comment = Column(String(2555), nullable=True)

    agent = relationship('UserAccount', backref='reviews')

    def __init__(self, agent_id, rating, comment):
        self.agent_id = agent_id
        self.rating = rating
        self.comment = comment

    @classmethod
    def create_review(cls, agent_id, rating, comment):
        # Create a review for the given agent
        review = cls(agent_id=agent_id, rating=rating, comment=comment)
        db.session.add(review)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while saving user profile. ")

    @classmethod
    def get_reviews_by_id(cls, agent_id):
        return cls.query.filter_by(agent_id=agent_id).all()