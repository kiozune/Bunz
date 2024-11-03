from flask import Blueprint, request, jsonify
from models.used_car_model import UsedCarListing
import logging

# Create a logger for your application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

used_car_bp = Blueprint('used_car', __name__)


@used_car_bp.route('/create_listing', methods=['POST'])
def create_listing():
    data = request.json
    logger.info("Received data for creating a listing: %s", data)

    # Validate the incoming data
    required_fields = ['make', 'model', 'year', 'price']
    for field in required_fields:
        if field not in data:
            logger.error("Missing field: %s", field)
            return jsonify({"error": f"{field} is required."}), 400

    try:
        UsedCarListing.create_listing(
            make=data['make'],
            model=data['model'],
            year=data['year'],
            price=data['price'],
            description=data.get('description', '')
        )
        logger.info("Listing created successfully.")
        return jsonify({"message": "Listing created successfully"}), 201
    except ValueError as e:
        logger.error("Error creating listing: %s", str(e))
        return jsonify({"error": str(e)}), 400


@used_car_bp.route('/listings', methods=['GET'])
def get_listings():
    listings = UsedCarListing.get_all_listings()
    logger.info("Retrieved listings: %s", listings)
    return jsonify([{
        "id": listing.id,
        "make": listing.make,
        "model": listing.model,
        "year": listing.year,
        "price": listing.price,
        "description": listing.description
    } for listing in listings])


@used_car_bp.route('/update_listing/<int:listing_id>', methods=['PUT'])
def update_listing(listing_id):
    data = request.json
    logger.info("Received data for updating listing %d: %s", listing_id, data)

    try:
        UsedCarListing.update_listing(listing_id, **data)
        logger.info("Listing updated successfully.")
        return jsonify({"message": "Listing updated successfully"}), 200
    except ValueError as e:
        logger.error("Error updating listing %d: %s", listing_id, str(e))
        return jsonify({"error": str(e)}), 400


@used_car_bp.route('/delete_listing/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    logger.info("Received request to delete listing %d", listing_id)

    try:
        UsedCarListing.delete_listing(listing_id)
        logger.info("Listing deleted successfully.")
        return jsonify({"message": "Listing deleted successfully"}), 200
    except ValueError as e:
        logger.error("Error deleting listing %d: %s", listing_id, str(e))
        return jsonify({"error": str(e)}), 400


@used_car_bp.route('/search_listings', methods=['GET'])
def search_listings():
    query = request.args.get('query', '')
    logger.info("Searching listings with query: %s", query)

    listings = UsedCarListing.query.filter(
        (UsedCarListing.make.like(f"%{query}%")) |
        (UsedCarListing.model.like(f"%{query}%"))
    ).all()

    logger.info("Found listings: %s", listings)
    return jsonify([{
        "id": listing.id,
        "make": listing.make,
        "model": listing.model,
        "year": listing.year,
        "price": listing.price,
        "description": listing.description
    } for listing in listings])
