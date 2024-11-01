from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

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
