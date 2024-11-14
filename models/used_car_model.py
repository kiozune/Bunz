from sqlalchemy.exc import IntegrityError
from datetime import datetime
from . import db
from flask import session


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
    agent_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    view_count = db.Column(db.Integer, default=0)
    shortlisted_count = db.Column(db.Integer, default=0)

    # Relationship
    seller = db.relationship('UserAccount', foreign_keys=[seller_id], backref='listings', lazy=True)
    agent = db.relationship('UserAccount', foreign_keys=[agent_id], backref='agent_listings', lazy=True)
    favorited_by_users = db.relationship(
        'UserAccount', secondary='favorites',
        primaryjoin="UsedCarListing.id == Favorite.listing_id",
        secondaryjoin="UserAccount.id == Favorite.user_id",
        backref=db.backref('favorite_listings', lazy='dynamic', overlaps="favorite_entries,favorite_listings"),
        lazy='dynamic', overlaps="favorite_entries,favorite_listings"
    )

    # Create a new listing
    @classmethod
    def create_listing(cls, brand, model, year, price, seller_id, agent_id, description=''):
        from models import UserAccount
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
            agent_id=agent_id,
            description=description
        )

        db.session.add(new_listing)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while saving the car listing. It might be a duplicate.")

    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'price': self.price,
            'description': self.description,
            'seller_username': self.seller_username
        }

    # Get all the listings
    @classmethod
    def get_all_listings(cls):
        return cls.query.all()

    # Retrieve a listing by its unique ID
    @classmethod
    def get_listing_by_id(cls, listing_id):
        listing = cls.query.get(listing_id)
        if not listing:
            raise ValueError("Listing not found.")
        return listing

    # Update the Listing's details
    @classmethod
    def update_listing(cls, listing_id, **kwargs):
        listing = cls.get_listing_by_id(listing_id)

        for key, value in kwargs.items():
            setattr(listing, key, value)

        try:
            db.session.commit()
            return listing

        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while updating the car listing.")

    # Delete the listing
    @classmethod
    def delete_listing(cls, listing_id):
        listing = cls.get_listing_by_id(listing_id)

        db.session.delete(listing)

        try:
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while deleting the car listing.")

    # Search the listings by brand or model
    @staticmethod
    def search_listings(search_query):
        return UsedCarListing.query.filter(
            (UsedCarListing.brand.ilike(f"%{search_query}%")) |
            (UsedCarListing.model.ilike(f"%{search_query}%"))
        ).all()

    #
    @classmethod
    def add_view_count(cls, listing_id):
        listing = cls.get_listing_by_id(listing_id)

        if 'viewed_car' not in session:
            session['viewed_cars'] = []

        try:
            if listing.id not in session['viewed_cars']:
                listing.view_count += 1
                db.session.commit()

        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while adding the view count.")

    # Shortlisted car listing counter
    def shortlisted_counter(self):
        from .favorites_model import Favorite
        self.shortlisted_count = db.session.query(Favorite).filter(Favorite.listing_id == self.id).count()
        try:
            db.session.commit()
        except IntegrityError as e:
            db.db.session.rollback()
            raise ValueError("An error occurred while counting the shortlisted count.")
