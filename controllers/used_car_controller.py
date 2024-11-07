from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from models import UsedCarListing, UserAccount


# Initialize the blueprint
used_car_bp = Blueprint('used_car', __name__)

class AddCarController:
    @staticmethod
    @used_car_bp.route('/add_car_listing', methods=['GET', 'POST'])
    def add_car_listing():
        accounts = UserAccount.query.all()
        if request.method == 'POST':
            data = request.get_json()

            required_fields = ['brand', 'model', 'year', 'price', 'seller_id']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({'error': f"{field} is required."}), 400

            try:
                brand = data['brand']
                model = data['model']
                year = int(data['year'])
                price = float(data['price'])
                seller_id = int(data['seller_id'])
                description = data.get('description', '')

                listing = UsedCarListing.create_listing(
                    brand=brand,
                    model=model,
                    year=year,
                    price=price,
                    seller_id=seller_id,
                    description=description
                )

                # Redirect to the car listing view or the newly created listing
                return jsonify({'message': 'Listing added successfully!'}), 200
            except ValueError as ve:
                return jsonify({'error': str(ve)}), 400
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        return render_template('car_listing/add_car_listing.html', accounts=accounts, title='Add Car Listing')

class ViewCarController:
    @staticmethod
    @used_car_bp.route('/car_listing', methods=['GET'])
    def car_listing():
        listings = UsedCarListing.get_all_listings()
        return render_template('car_listing/view_car_listing.html', car_listings=listings)

class CarDetailsController:
    @used_car_bp.route('/car_details/<int:listing_id>', methods=['GET'])
    def car_details(listing_id):
        try:
            listing = UsedCarListing.get_listing_by_id(listing_id)
            return render_template('car_listing/car_details.html', listing=listing)
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 404

class EditCarController:
    @staticmethod
    @used_car_bp.route('/car_listing/edit/<int:listing_id>', methods=['GET', 'POST'])
    def edit_car_listing(listing_id):
        try:
            listing = UsedCarListing.get_listing_by_id(listing_id)
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 404

        if request.method == 'POST':
            data = request.form
            try:
                updated_listing = UsedCarListing.update_listing(
                    listing_id,
                    brand=data['brand'],
                    model=data['model'],
                    year=int(data['year']),
                    price=float(data['price']),
                    description=data.get('description', '')
                )
                return redirect(url_for('used_car.car_details', listing_id=updated_listing.id))
            except ValueError as ve:
                return jsonify({'error': str(ve)}), 400

        return render_template('car_listing/edit_car_listing.html', listing=listing)

class DeleteCarController:
    @staticmethod
    @used_car_bp.route('/car_listing/delete/<int:listing_id>', methods=['POST'])
    def delete_listing(listing_id):
        try:
            UsedCarListing.delete_listing(listing_id)
            return redirect(url_for('used_car.car_listing'))  # Redirect after successful deletion
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 404  # Return error if listing not found
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Handle other exceptions

class SearchCarController:
    @staticmethod
    @used_car_bp.route('/search', methods=['GET'])
    def search_car_listings():
        search_query = request.args.get('search', '').strip()
        if search_query:
            filtered_listings = UsedCarListing.search_listings(search_query)
        else:
            filtered_listings = []
        return render_template('car_listing/search_results.html', car_listings=filtered_listings, search_query=search_query)