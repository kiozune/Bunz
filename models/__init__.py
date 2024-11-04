from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models here to prevent circular import issues
from .account_model import UserAccount
from .profile_model import UserProfile
