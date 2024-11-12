from flask import Blueprint, request, redirect, url_for, flash, render_template
from models import Review, UserAccount

# Define blueprint for reviews
review_bp = Blueprint('review', __name__)

# Route to display the form to write a review
@review_bp.route('/write_review')
def write_review():
    # Retrieve all agents to display in the dropdown
    agents = UserAccount.query.filter_by(role_name='agent').all()
    return render_template('reviews/add_reviews.html', agents=agents)  # Corrected template path

# Route to handle the review submission
@review_bp.route('/submit_review', methods=['POST'])
def submit_review():
    # Get the selected agent's ID, rating, and comment from the form
    agent_id = request.form.get('agent_id')
    rating = int(request.form.get('rating'))
    comment = request.form.get('comment')

    try:
        # Create a new review for the selected agent
        Review.create_review(agent_id, rating, comment)
        flash("Review submitted successfully!")
    except ValueError as e:
        # Handle validation errors (e.g., invalid rating, comment)
        flash(str(e))

    # Redirect back to the review form to write another review
    return redirect(url_for('review.write_review'))

# Route to display reviews for a specific agent
@review_bp.route('/view_reviews/<int:agent_id>', methods=['GET'])
def view_reviews(agent_id):
    # Retrieve all reviews for the given agent
    reviews = Review.query.filter_by(agent_id=agent_id).all()

    # Optionally, print or log the agent username for debugging purposes
    for review in reviews:
        print(f"Review ID: {review.id}, Agent Username: {review.agent.username}")

    # Render the template to display the reviews
    return render_template('reviews/view_reviews.html', reviews=reviews)  # Corrected template path
