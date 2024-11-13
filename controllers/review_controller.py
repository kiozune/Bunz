from flask import Blueprint, request, redirect, url_for, flash, render_template
from models import Review, UserAccount
from utils import login_required, agent_only

review_bp = Blueprint('review', __name__)

class ReviewController:
    # Route to display the form to write a review
    @review_bp.route('/write_review/<int:agent_id>')
    @login_required
    def write_review(agent_id):
        agent = UserAccount.query.get(agent_id)
        return render_template('review/create_review.html', agent=agent)  # Corrected template path

    # Route to handle the review submission
    @review_bp.route('/submit_review', methods=['POST'])
    @login_required
    def submit_review():
        agent_id = request.form.get('agent_id')
        rating = int(request.form.get('rating'))
        comment = request.form.get('comment')

        try:
            Review.create_review(agent_id, rating, comment)
            flash("Review submitted successfully!")
        except ValueError as e:
            flash(str(e))

        return redirect(url_for('account.view_agent', agent_id=agent_id))

    # Route to display reviews for a specific agent
    @review_bp.route('/view_reviews/<int:agent_id>', methods=['GET'])
    @login_required
    @agent_only
    def view_reviews(agent_id):
        agent = UserAccount.query.get_or_404(agent_id)
        reviews = Review.query.filter_by(agent_id=agent_id).all()
        return render_template('review/view_reviews.html', agent=agent, reviews=reviews)

    # controllers.py

    @review_bp.route('/view_agent/<int:agent_id>', methods=['GET'])
    @login_required
    def view_agent(agent_id):
        agent = UserAccount.query.get_or_404(agent_id)
        reviews = Review.query.filter_by(agent_id=agent_id).all()  # Fetch all reviews for this agent
        for each in reviews:
            print(each)
        return render_template('agent/view_agent.html', agent=agent)

