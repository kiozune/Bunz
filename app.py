from flask import Flask, render_template
from models import UserProfile, UserAccount, db
from config import Config
from flask_migrate import Migrate
from controllers import create_profile_bp, view_profile_bp, update_profile_bp, suspend_profile_bp, search_profile_bp
from controllers import create_account_bp, view_account_bp, update_account_bp, suspend_account_bp, search_account_bp
from controllers import login_bp, logout_bp, loan_calculator_bp
from utils import page_not_found
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(Config)
db.init_app(app)

migrate = Migrate(app, db)

# Register Blueprint
# User Profile
app.register_blueprint(create_profile_bp, url_prefix='/')
app.register_blueprint(view_profile_bp, url_prefix='/')
app.register_blueprint(update_profile_bp, url_prefix='/')
app.register_blueprint(suspend_profile_bp, url_prefix='/')
app.register_blueprint(search_profile_bp, url_prefix='/')

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

app.register_error_handler(404, page_not_found)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
