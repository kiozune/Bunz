from . import db

favorite_used_car = db.Table(
    'favorite_used_car',
    db.Column('user_id', db.Integer, db.ForeignKey('user_account.id'), primary_key=True),
    db.Column('car_id', db.Integer, db.ForeignKey('used_car_listing.id'), primary_key=True)
)