from . import db
from sqlalchemy.exc import IntegrityError

class UsedCarListing(db.Model):
    __tablename__ = 'used_car_listing'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    @classmethod
    def create_listing(cls, make, model, year, price, description=''):
        if year > 2024:  # Replace 2024 with the current year or get dynamically
            raise ValueError("Year cannot be in the future.")
        if price < 0:
            raise ValueError("Price must be a positive number.")

        new_listing = cls(make=make, model=model, year=year, price=price, description=description)
        db.session.add(new_listing)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while saving the car listing. It might be a duplicate.")

    @classmethod
    def get_all_listings(cls):
        return cls.query.all()

    @classmethod
    def update_listing(cls, listing_id, **kwargs):
        listing = cls.query.get(listing_id)
        if not listing:
            raise ValueError("Listing not found.")

        for key, value in kwargs.items():
            setattr(listing, key, value)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while updating the car listing.")

    @classmethod
    def delete_listing(cls, listing_id):
        listing = cls.query.get(listing_id)
        if not listing:
            raise ValueError("Listing not found.")

        db.session.delete(listing)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while deleting the car listing.")
