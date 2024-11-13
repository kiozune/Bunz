from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import db  # Import db instance

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
        db.session.commit()