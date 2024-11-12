from flask import Flask, render_template
from models import db
from config import Config
from flask_migrate import Migrate
from controllers import *
from utils import page_not_found
import os
import logging

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(Config)
db.init_app(app)
logging.basicConfig(level=logging.DEBUG)

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

# Used Car
app.register_blueprint(used_car_bp, url_prefix='/')
app.register_blueprint(my_used_car_bp, url_prefix='/')
app.register_blueprint(favorites_bp, url_prefix='/')

app.register_error_handler(404, page_not_found)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/unauthorized_user')
def unauthorized():
    return render_template('permission_denied.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
