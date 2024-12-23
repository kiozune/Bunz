import unittest
from app import db, app
from models import UserAccount, UsedCarListing, Review, Favorite
from werkzeug.security import generate_password_hash


class SellerActionsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app
        cls.app.config["TESTING"] = True
        cls.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        cls.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        with cls.app.app_context():
            db.create_all()

            # Delete any existing data related to test users to avoid conflicts
            db.session.query(Review).filter(Review.agent_id == db.session.query(UserAccount.id).filter_by(
                username="wonglonglong").scalar()).delete()
            db.session.query(UsedCarListing).filter_by(seller_username='sebastianwilliam').delete()
            db.session.query(UserAccount).filter_by(username="sebastianwilliam").delete()
            db.session.query(UserAccount).filter_by(username="wonglonglong").delete()
            db.session.commit()

            cls.default_password = "12345678"
            cls.seller = UserAccount(
                username="sebastianwilliam",
                password=generate_password_hash(cls.default_password),
                role_name="seller",
                role_id=3,
                email="sebastian@gmail.com",
                phone_number='84232156'
            )

            cls.agent = UserAccount(
                username="wonglonglong",
                password=generate_password_hash(cls.default_password),
                role_name="agent",
                role_id=4,
                email="wongll@gmail.com",
                phone_number='91738172'
            )

            db.session.add(cls.seller)
            db.session.add(cls.agent)
            db.session.commit()

            cls.seller_id = cls.seller.id
            cls.agent_id = cls.agent.id
            cls.seller_username = cls.seller.username

        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    # Seller Login Testing
    def test_seller_login(self):
        response = self.client.post(
            "/login",
            data={"username": "sebastianwilliam", "password": self.default_password},
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"/", response.data)

        with self.client.session_transaction() as session:
            self.assertEqual(session.get("username"), "sebastianwilliam")

    # Seller Logout Testing
    def test_seller_logout(self):
        self.client.post("/login",
                         data={"username": "sebastianwilliam",
                               "password": self.default_password
                               },
                         follow_redirects=True
                         )
        response = self.client.get("/logout", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login", response.data)
        with self.client.session_transaction() as session:
            self.assertNotIn("username", session)

    # Seller view its vehicle view count
    def test_seller_view_vehicle_view_count(self):
        self.client.post("/login",
                         data={"username": "sebastianwilliam",
                               "password": self.default_password},
                         follow_redirects=True
                         )

        listing = UsedCarListing(
            brand="Honda",
            model="Civic",
            year=2015,
            price=15000,
            description='Cheap and Nice car',
            seller_id=self.seller.id,
            seller_username=self.seller.username,
            agent_id=self.agent.id,
            view_count=10
        )

        db.session.add(listing)
        db.session.commit()

        response = self.client.get(f"/my_car")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"10 views", response.data)

    # Seller view the vehicle count of being shortlisted
    def test_seller_view_vehicle_shortlist_count(self):
        self.client.post(
            "/login",
            data={"username": "sebastianwilliam",
                  "password": self.default_password},
            follow_redirects=True
        )

        listing = UsedCarListing(
            brand="Honda",
            model="Civic",
            year=2015,
            price=15000,
            description='Cheap and Nice car',
            seller_id=self.seller.id,
            seller_username=self.seller.username,
            agent_id=self.agent.id,
            shortlisted_count=5
        )
        db.session.add(listing)
        db.session.commit()

        response = self.client.get("/my_car")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"5 times", response.data)

    # Seller give ratings to agent
    def test_seller_rate_agent_success(self):
        self.client.post(
            "/login",
            data={"username": "sebastianwilliam",
                  "password": self.default_password},
            follow_redirects=True
        )
        rating_data = {
            "agent_id": self.agent.id,
            "rating": 2,
            "comment": "Not Very Good!"
        }
        response = self.client.post("/submit_review", data=rating_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Review submitted successfully!", response.data)

        saved_review = Review.query.filter_by(agent_id=self.agent.id).first()
        self.assertIsNotNone(saved_review)
        self.assertEqual(saved_review.rating, 2)
        self.assertEqual(saved_review.comment, "Not Very Good!")



if __name__ == "__main__":
    unittest.main()
