from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here to prevent circular import issues
from .account_model import UserAccount
from .profile_model import UserProfile
from .calculator_model import Calculator
from .used_car_model import UsedCarListing

