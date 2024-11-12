from . import db

class Favorite(db.Model):
    __tablename__ = 'favorites'
    user_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), primary_key=True, nullable=False)
    listing_id = db.Column(db.Integer, db.ForeignKey('used_car_listing.id'), primary_key=True, nullable=False)

    user = db.relationship('UserAccount',
                           backref=db.backref('favorite_entries', lazy='dynamic', overlaps="favorited_listings"))
    listing = db.relationship('UsedCarListing',
                              backref=db.backref('favorite_records', lazy='dynamic', overlaps="favorited_by_users"))
    @staticmethod
    def toggle_favorite(user_id, listing_id):
        favorite = Favorite.query.filter_by(user_id=user_id, listing_id=listing_id).first()

        if favorite:
            db.session.delete(favorite)
            action = 'removed'
        else:
            # If the car is not in the favorites list, add it
            new_favorite = Favorite(user_id=user_id, listing_id=listing_id)
            db.session.add(new_favorite)
            action = 'added'

        try:
            db.session.commit()
            return action
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error occurred while toggling favorite: {str(e)}")