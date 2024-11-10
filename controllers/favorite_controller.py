from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from models.account_model import UserAccount
from models.used_car_model import UsedCarListing
from flask_sqlalchemy import SQLAlchemy

# Initialize your database (assuming you've already initialized `db` elsewhere)
db = SQLAlchemy()

# Blueprint for favorites
favorites_bp = Blueprint('favorites', __name__)

@favorites_bp.route('/add_to_favorites', methods=['POST'])
def add_to_favorites():
    user_id = request.form.get('user_id')  # Get user_id from the form
    car_id = request.form.get('car_id')  # Get car_id from the form

    # Fetch user and car from the database
    user = UserAccount.query.get(user_id)
    car = UsedCarListing.query.get(car_id)

    # If either the user or the car doesn't exist, show an error
    if not user or not car:
        flash("User or Car not found.", "danger")
        return redirect(url_for('used_car.car_listing'))  # Redirect back to car listings

    # Add the car to the user's favorites
    user.add_to_favorites(car)

    # Commit the changes to the database
    db.session.commit()

    # Flash a success message and redirect back to the car listing page
    flash(f"{car.brand} {car.model} has been added to your favorites.", "success")
    return redirect(url_for('used_car.view_car_listing', listing_id=car.id))  # Redirect to the car's listing page

@favorites_bp.route('/remove_from_favorites', methods=['POST'])
def remove_from_favorites():
    data = request.get_json()
    user_id = data.get('user_id')
    car_id = data.get('car_id')

    # Fetch user and car from the database
    user = UserAccount.query.get(user_id)
    car = UsedCarListing.query.get(car_id)

    if not user or not car:
        return jsonify({"error": "User or car not found."}), 404

    # Remove the car from the user's favorites
    user.remove_from_favorites(car)

    # Commit the changes to the database
    db.session.commit()

    return jsonify({"message": f"Car ID {car_id} removed from user {user_id}'s favorites."}), 200

@favorites_bp.route('/view_favorites/<int:user_id>', methods=['GET'])
def view_favorites(user_id):
    user = UserAccount.query.get(user_id)
    if not user:
        return "User not found", 404

    favorite_cars = user.favorites  # This will return all the cars in the user's favorites
    return render_template('car_listing/favorites.html', favorite_cars=favorite_cars, user_id=user_id)

