from . import db
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from .account_model import UserAccount


class UsedCarListing(db.Model):
    __tablename__ = 'used_car_listing'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    seller_username = db.Column(db.String(50), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)

    @classmethod
    def create_listing(cls, brand, model, year, price, seller_id, description=''):
        current_year = datetime.now().year
        seller = UserAccount.query.get(seller_id)
        if year > current_year:
            raise ValueError("Year cannot be in the future.")
        if price < 0:
            raise ValueError("Price must be a positive number.")

        new_listing = cls(
            brand=brand,
            model=model,
            year=year,
            price=price,
            seller_username=seller.username,
            seller_id=seller_id,
            description=description
        )

        db.session.add(new_listing)
        try:
            db.session.commit()
            return new_listing  # Return the created listing for further reference if needed
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while saving the car listing. It might be a duplicate.")

    def to_dict(self):
        """Convert the object to a dictionary."""
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'price': self.price,
            'description': self.description,
            'seller_username': self.seller_username
        }

    @classmethod
    def get_all_listings(cls):
        """Retrieve all car listings."""
        return cls.query.all()

    @classmethod
    def get_listing_by_id(cls, listing_id):
        """Retrieve a car listing by its ID."""
        listing = cls.query.get(listing_id)
        if not listing:
            raise ValueError("Listing not found.")
        return listing

    @classmethod
    def update_listing(cls, listing_id, **kwargs):
        """Update the specified car listing."""
        listing = cls.get_listing_by_id(listing_id)  # Use the new method to get the listing

        for key, value in kwargs.items():
            setattr(listing, key, value)

        try:
            db.session.commit()
            return listing  # Return the updated listing for confirmation
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while updating the car listing.")

    @classmethod
    def delete_listing(cls, listing_id):
        """Delete the specified car listing."""
        listing = cls.get_listing_by_id(listing_id)  # Use the new method to get the listing

        db.session.delete(listing)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while deleting the car listing.")

    @staticmethod
    def search_listings(search_query):
        return UsedCarListing.query.filter(
            (UsedCarListing.brand.ilike(f"%{search_query}%")) |
            (UsedCarListing.model.ilike(f"%{search_query}%"))
        ).all()
