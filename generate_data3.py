from faker import Faker
from app import db, app
from models import UserAccount, Review
import random

fake = Faker()


def generate_data():
    with app.app_context():
        # Fetch existing buyers and sellers (in your case, agents, buyers, and sellers)
        buyers = [u for u in UserAccount.query.all() if u.role_name == "buyer"]
        sellers = [u for u in UserAccount.query.all() if u.role_name == "seller"]
        agents = [u for u in UserAccount.query.all() if u.role_name == "agent"]

        # Define a pool of predefined comments
        comment_pool = [
            "Excellent service, very professional!",
            "The agent was very helpful and knowledgeable.",
            "Had a great experience working with this agent!",
            "Highly recommend this agent for their expertise.",
            "Very satisfied with the service provided by this agent.",
            "The agent was a pleasure to work with, very friendly.",
            "Great experience, would definitely work with this agent again.",
            "The agent went above and beyond to help me with my purchase.",
            "Professional and efficient. Great service overall.",
            "Really appreciated the agent's support throughout the process."
        ]

        # Add reviews (buyers and sellers reviewing agents)
        reviews = []
        for _ in range(100):  # Add 100 random reviews
            # Randomly choose a reviewer: buyer or seller
            reviewer = random.choice(buyers + sellers)  # Both buyers and sellers can review agents

            # Random agent to review
            agent = random.choice(agents)

            # Select a random comment from the pool
            comment = random.choice(comment_pool)

            # Create the review
            try:
                review = Review(
                    agent_id=agent.id,  # Review is tagged to the agent
                    rating=random.randint(1, 5),  # Random rating from 1 to 5
                    comment=comment  # Random comment from the pool
                )
                db.session.add(review)
                reviews.append(review)
                print(f"Added review from {reviewer.username} for agent {agent.username} with rating {review.rating}")
            except Exception as e:
                print(f"Error adding review: {e}")

        db.session.commit()
        print("Data generation completed successfully.")


generate_data()