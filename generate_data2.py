from faker import Faker
from app import db, app
from models import UserAccount, UsedCarListing, Favorite, Review
import random

fake = Faker()


def generate_data():
    with app.app_context():
        # Clear existing favorites and reviews
        db.session.query(Favorite).delete()
        db.session.query(Review).delete()

        # Fetch existing users with the "buyer" and "agent" roles
        buyers = [u for u in UserAccount.query.all() if u.role_name == "buyer"]
        agents = [u for u in UserAccount.query.all() if u.role_name == "agent"]

        # Fetch all car listings
        car_listings = UsedCarListing.query.all()

        # Add favorites (users favoriting listings)
        favorites = []
        for user in buyers:
            for _ in range(random.randint(1, 5)):  # Each buyer favorites 1-5 listings
                listing = random.choice(car_listings)

                # Check if this favorite already exists
                existing_favorite = Favorite.query.filter_by(user_id=user.id, listing_id=listing.id).first()

                if not existing_favorite:
                    try:
                        favorite = Favorite(user_id=user.id, listing_id=listing.id)
                        db.session.add(favorite)
                        favorites.append(favorite)
                        print(f"Added favorite for user {user.username} to listing {listing.id}")
                    except Exception as e:
                        print(f"Error adding favorite: {e}")
                else:
                    print(f"Favorite for user {user.username} and listing {listing.id} already exists.")
        db.session.commit()

        print("Data generation completed successfully.")


generate_data()