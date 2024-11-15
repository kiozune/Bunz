from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from models.account_model import UserAccount, db
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
                flash("Listing added to favorites.", "success")
            else:
                flash("Listing removed from favorites.", "success")

            return redirect(request.referrer)

        except ValueError as e:
            flash(str(e), "error")
            return redirect(request.referrer)

class ViewFavoriteController:
    @favorites_bp.route('/view_favorites/<int:user_id>', methods=['GET'])
    @login_required
    def view_favorites(user_id):
        listings = Favorite.get_favorite_listings(user_id)

        return render_template('car_listing/favorites.html', favorite_cars=listings, user_id=user_id, title='My favorite')

class SearchFavoriteController:
    @favorites_bp.route('/search_favorites/<int:user_id>', methods=['GET'])
    @login_required
    def search_favorites(user_id):
        user = UserAccount.query.get(user_id)
        if not user:
            return "User not found", 404

        search_query = request.args.get('query', '')
        listings = Favorite.search_favorite_listings(user_id, search_query)
        return render_template('car_listing/favorites.html', favorite_cars=listings, user_id=user_id,
                               search_query=search_query, title='My favorite')

