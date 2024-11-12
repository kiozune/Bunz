from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from models.account_model import UserAccount
from models.favorites_model import Favorite
from models.used_car_model import UsedCarListing
from utils import login_required

# Blueprint for favorites
favorites_bp = Blueprint('favorites', __name__)

class FavoriteController:
    @staticmethod
    @favorites_bp.route('/toggle_favorite', methods=['POST'])
    @login_required
    def toggle_favorite():
        user_id = session.get('user_id')
        listing_id = request.form.get('listing_id')

        try:
            action = Favorite.toggle_favorite(user_id, listing_id)

            if action == 'added':
                flash("Car added to favorites.", "success")
            else:
                flash("Car removed from favorites.", "success")

            return redirect(request.referrer)

        except ValueError as e:
            flash(str(e), "error")
            return redirect(request.referrer)

    @favorites_bp.route('/view_favorites/<int:user_id>', methods=['GET'])
    def view_favorites(user_id):
        user = UserAccount.query.get(user_id)
        if not user:
            return "User not found", 404
        user_id = session.get('user_id')
        from models.favorites_model import Favorite
        favorite_cars = user.favorited_listings
        for listing in favorite_cars:
            listing.is_favorited = Favorite.query.filter_by(user_id=user_id, listing_id=listing.id).first() is not None

        return render_template('car_listing/favorites.html', favorite_cars=favorite_cars, user_id=user_id)

