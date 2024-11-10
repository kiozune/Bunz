<<<<<<< Updated upstream
from flask import Flask, render_template
from models import db, UserProfile
=======
from flask import Flask, render_template, session
from models import UserProfile, UserAccount, db
>>>>>>> Stashed changes
from config import Config
from flask_migrate import Migrate
from controllers import create_profile_bp, view_profile_bp, update_profile_bp, suspend_profile_bp, search_profile_bp
# from controllers import create_account_bp, view_account_bp, update_account_bp, suspend_account_bp, search_account_bp
from controllers.used_car_controller import used_car_bp


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

migrate = Migrate(app, db)

# Register Blueprint
app.register_blueprint(create_profile_bp, url_prefix='/')
app.register_blueprint(view_profile_bp, url_prefix='/')
app.register_blueprint(update_profile_bp, url_prefix='/')
app.register_blueprint(suspend_profile_bp, url_prefix='/')
app.register_blueprint(search_profile_bp, url_prefix='/')
app.register_blueprint(used_car_bp, url_prefix='/used_car')

<<<<<<< Updated upstream
# app.register_blueprint(create_account_bp, url_prefix='/')
# app.register_blueprint(view_account_bp, url_prefix='/')
# app.register_blueprint(update_account_bp, url_prefix='/')
# app.register_blueprint(suspend_account_bp, url_prefix='/')
# app.register_blueprint(search_account_bp, url_prefix='/')
=======
# User Account
app.register_blueprint(create_account_bp, url_prefix='/')
app.register_blueprint(view_account_bp, url_prefix='/')
app.register_blueprint(update_account_bp, url_prefix='/')
app.register_blueprint(suspend_account_bp, url_prefix='/')
app.register_blueprint(search_account_bp, url_prefix='/')

# login
app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(logout_bp, url_prefix='/')

# Loan Calculator
app.register_blueprint(loan_calculator_bp, url_prefix='/')

app.register_blueprint(used_car_bp, url_prefix='/')
app.register_blueprint(favorites_bp, url_prefix='/favorites')

app.register_error_handler(404, page_not_found)
>>>>>>> Stashed changes

@app.route('/')
def index():
    # Check if user_id is stored in session
    user_id = session.get('user_id')  # Assuming 'user_id' is saved in session
    return render_template('index.html', user_id=user_id)

@app.route('/used_car/add', methods=['GET'])
def add_car_listing():
    return render_template('car listing/add_car_listing.html', title='Add Car Listing')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
