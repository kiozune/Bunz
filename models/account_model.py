from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
<<<<<<< Updated upstream

db = SQLAlchemy()

class UserAccount:
    pass
#     __tablename__ = 'user_profile'
#     id = db.Column(db.Integer, primary_key=True)
#     role = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.Text, nullable=True)
#     is_suspended = db.Column(db.Boolean, default=False)
#
# # Create a new profile and load it into database for storage
#     @classmethod
#     def create_profile(cls, role, description):
#         # Check if profile/role existing in the database
#         check_existing_role = UserProfile.query.filter_by(role=role).first()
#         if check_existing_role:
#             raise ValueError(f"The role : {role} is already exists. Please choose a different role")
#
#         new_profile = cls(role=role, description=description)
#         db.session.add(new_profile)
#         try:
#             db.session.commit()
#         except IntegrityError:
#             db.session.rollback()
#             raise ValueError("An error occurred while saving user profile. ")
#
#     @classmethod
#     def get_all_profile(cls):
#         # Get all the user profiles
#         return cls.query.all()
#
#     @classmethod
#     def get_profile_by_role(cls, role):
#         # Retrieves a profile by its role
#         return cls.query.get(role)
#
#     @classmethod
#     def get_profile_by_id(cls, profile_id):
#         # Retrieves a profile by its ID
#         return cls.query.get(profile_id)
#
# # Update latest profile details into database
#     @classmethod
#     def update_profile(cls, profile_id, new_role, new_description):
#         profile = cls.query.get(profile_id)
#
#         if new_role != profile.role:
#             existing_role = cls.query.filter_by(role=new_role).first()
#             if existing_role:
#                 raise ValueError(f"The role {new_role} is already exists.")
#
#         profile.role = new_role
#         profile.description = new_description
#         try:
#             db.session.commit()
#         except IntegrityError:
#             db.session.rollback()
#             raise ValueError("An error occurred while saving user profile. ")
#
#     @classmethod
#     def suspend_profile(cls, profile_id):
#         profile = cls.query.get(profile_id)
#         profile.is_suspended = True
#         try:
#             db.session.commit()
#             return profile.role
#         except IntegrityError:
#             db.session.rollback()
#             raise ValueError("An error occurred while saving user profile. ")
#
#     @classmethod
#     def search_profile(cls, query):
#         return cls.query.filter(cls.role.like(f'%{query}%')).all()


    # def __repr__(self):
    #     return f'<UserAccount {self.role}>'
=======
from werkzeug.security import generate_password_hash, check_password_hash
from .profile_model import UserProfile
from .favorites import favorite_used_car
from . import db



class UserAccount(db.Model):
    __tablename__ = 'user_account'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    role_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    is_suspended = db.Column(db.Boolean, default=False)

    role = db.relationship('UserProfile', backref='user_accounts')

    favorites = db.relationship('UsedCarListing',
                                secondary='favorite_used_car',
                                backref=db.backref('favorited_by', lazy='dynamic'))
    # Hash password
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Check hash password if match
    def check_password(self, password):
        return check_password_hash(self.password, password)

# Create a new profile and load it into database for storage
    @classmethod
    def create_account(cls, username, password, role_id,  email, phone):
        # Create role instance
        role = UserProfile.query.get(role_id)

        # Check role id exist
        if not role:
            raise ValueError("Invalid role ID provided.")

        # Check if profile/role existing in the database
        check_existing_username = UserAccount.query.filter_by(username=username).first()
        if check_existing_username:
            raise ValueError(f"Username : {username} already exist! Please choose another username")

        # Check duplicate email
        check_existing_email = UserAccount.query.filter_by(email=email).first()
        if check_existing_email:
            raise ValueError(f"Email : {username} already used! Please choose another email")

        # Create account instance
        new_account = cls(
            username=username,
            password=password,
            role_id=role_id,
            email=email,
            phone_number=phone,
            role_name=role.role
        )
        # Hash the instance password
        new_account.set_password(password)
        db.session.add(new_account)

        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print(e)
            print(f'Creating account with username: {username}, email: {email}, role_id: {role_id}, phone: {phone}')
            raise ValueError("An error occurred while saving user profile. ")

    # Retrieve all user accounts details
    @classmethod
    def get_all_accounts(cls):
        # Get all the user accounts
        return cls.query.all()

    @classmethod
    def get_account_by_id(cls, account_id):
        # Retrieves an account by its ID
        return cls.query.get(account_id)

    # Update latest profile details into database
    @classmethod
    def update_account(cls, account_id, new_role_id,  new_email, new_phone):
        account = cls.query.get(account_id)

        if new_email != account.email:
            existing_email = cls.query.filter_by(email=new_email).first()
            if existing_email:
                raise ValueError(f"The role {new_email} is already exists.")

        account.role_id = new_role_id
        account.email = new_email
        account.phone_number = new_phone

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while saving user profile. ")


    @classmethod
    def suspend_account(cls, account_id):
        account = cls.query.get(account_id)
        account.is_suspended = True
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("An error occurred while saving user profile. ")

    # Search query

    @classmethod
    def search_account(cls, query):
        results = cls.query.filter(
             cls.username.ilike(f'%{query}%') |
             cls.email.ilike(f'%{query}%') |
             cls.phone_number.ilike(f'%{query}%')
        ).all()
        return results



    # Method to add a car to the user's favorites
    def add_to_favorites(self, car):
        if car not in self.favorites:
            self.favorites.append(car)
            db.session.commit()



    # Method to remove a car from favorites
    def remove_from_favorites(self, car):
        if car in self.favorites:
            self.favorites.remove(car)
            db.session.commit()
>>>>>>> Stashed changes
