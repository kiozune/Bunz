from . import db
from models.used_car_model import UsedCarListing

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

            listing = UsedCarListing.query.get(listing_id)
            if listing:
                listing.shortlisted_counter()

            return action
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error occurred while toggling favorite: {str(e)}")

    # Get the listings that are favorited by the buyer
    @staticmethod
    def get_favorite_listings(user_id):
        from models.used_car_model import UsedCarListing
        favorite_listings = (
            db.session.query(UsedCarListing, Favorite)
            .join(Favorite, Favorite.listing_id == UsedCarListing.id)
            .filter(Favorite.user_id == user_id)
            .all()
        )

        for listing, _ in favorite_listings:
            listing.is_favorited = True

        return [listing for listing, _ in favorite_listings]

    # Search the listings in my favorite list
    @staticmethod
    def search_favorite_listings(user_id, search_query):
        from models.used_car_model import UsedCarListing
        favorite_listings = (
            db.session.query(UsedCarListing, Favorite)
            .join(Favorite, Favorite.listing_id == UsedCarListing.id)
            .filter(
                Favorite.user_id == user_id,
                (UsedCarListing.brand.ilike(f"%{search_query}%")) |
                (UsedCarListing.model.ilike(f"%{search_query}%"))
            )
            .all()
        )

        for listing, _ in favorite_listings:
            listing.is_favorited = True

        return [listing for listing, _ in favorite_listings]
