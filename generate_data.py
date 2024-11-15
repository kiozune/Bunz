from faker import Faker
from werkzeug.security import generate_password_hash
from app import db, app
from models import UserAccount, UserProfile, UsedCarListing, Favorite, Review
import random

fake = Faker()

def generate_data():
    with app.app_context():
        # Clear existing data
        db.session.query(UsedCarListing).delete()
        db.session.query(UserAccount).delete()
        db.session.query(UserProfile).delete()

        # Predefined password (hashed)
        default_password = generate_password_hash("12345678")

        # Create user roles, ensure one "admin" role only
        roles = ["admin", "buyer", "seller", "agent"]
        user_roles = []

        for role in roles:
            is_admin = role == "admin"
            profile = UserProfile(
                role=role,
                description=fake.text(),
                is_suspended=False
            )
            db.session.add(profile)
            user_roles.append(profile)

        db.session.commit()

        # Add user accounts starting from id 10000
        user_accounts = []
        for profile in user_roles:
            if profile.role == "admin":
                # Only one admin account
                user = UserAccount(
                    username="admin_user",
                    password=default_password,
                    role_id=profile.id,
                    role_name=profile.role,
                    email="admin@example.com",
                    phone_number=random.randint(1000000000, 9999999999),
                    is_suspended=False
                )
                db.session.add(user)
                user_accounts.append(user)
            else:
                # Add 100 users for other roles
                for _ in range(100):
                    user = UserAccount(
                        username=fake.user_name(),
                        password=default_password,
                        role_id=profile.id,
                        role_name=profile.role,
                        email=fake.unique.email(),
                        phone_number=random.randint(1000000000, 9999999999),
                        is_suspended=random.choice([True, False])
                    )
                    db.session.add(user)
                    user_accounts.append(user)

        db.session.commit()

        # Add car listings
        car_listings = []
        for _ in range(100):
            car_brands = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Audi",
                          "Chevrolet", "Nissan", "Hyundai",
                          "Volkswagen"]
            car_models = ["Camry", "Civic", "Mustang", "X5", "A-Class", "A4",
                          "Impala", "Altima", "Sonata", "Golf"]
            car_years = list(range(2000, 2025))
            fuel_types = ["Petrol", "Diesel", "Electric", "Hybrid"]
            transmissions = ["Manual", "Automatic"]
            colors = ["Red", "Blue", "Black", "White", "Silver", "Gray", "Green", "Yellow", "Orange"]
            engine_sizes = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]  # in liters
            car_mileages = list(range(5000, 250000, 5000))  # Mileage from 5k to 250k km
            car_weights = list(range(1000, 2500))
            seller = random.choice([u for u in user_accounts if u.role_name == "seller"])
            agent = random.choice([u for u in user_accounts if u.role_name == "agent"])
            brand = random.choice(car_brands)
            model = random.choice(car_models)
            year = random.choice(car_years)

            mileage = random.choice(car_mileages)
            weight = random.choice(car_weights)
            fuel_type = random.choice(fuel_types)
            transmission = random.choice(transmissions)
            color = random.choice(colors)
            engine_size = random.choice(engine_sizes)

            # Generate description with random specifications
            description = f"Car Specifications:\n" \
                          f"Brand: {brand}\n" \
                          f"Model: {model}\n" \
                          f"Year: {year}\n" \
                          f"Mileage: {mileage} km\n" \
                          f"Weight: {weight} kg\n" \
                          f"Fuel Type: {fuel_type}\n" \
                          f"Transmission: {transmission}\n" \
                          f"Color: {color}\n" \
                          f"Engine Size: {engine_size}L"

            listing = UsedCarListing(
                brand=brand,
                model=model,
                year=year,
                price=round(random.uniform(5000, 30000), 2),
                description=description,
                seller_username=seller.username,
                seller_id=seller.id,
                agent_id=agent.id,
                view_count=random.randint(0, 500),
            )
            db.session.add(listing)
            car_listings.append(listing)

        db.session.commit()

# Run the data generation function
generate_data()
