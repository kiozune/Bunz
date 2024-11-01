from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import UserAccount

# Create Account Controller
create_account_bp = Blueprint('create_account', __name__)
class CreateAccountController:
    @staticmethod
    @create_account_bp.route('/create_account', methods=['GET', 'POST'])
    def create_account():
        pass


# View Account Controller
view_account_bp = Blueprint('view_account', __name__)
class ViewAccountController:
    @staticmethod
    @view_account_bp.route('/view_profile')
    def view_account():
        # Instance that get all the accounts stored in the database
        pass

# Update Account Controller
update_account_bp = Blueprint('update_account', __name__)
class UpdateAccountController:
    @staticmethod
    @update_account_bp.route('/update_account/<int:id>', methods=['GET', 'POST'])
    def update_profile(id):
        # Retrieve the existing profile by ID
       pass

# Suspend Account Controller
suspend_account_bp = Blueprint('suspend_account', __name__)
class SuspendProfileController:
    @staticmethod
    @suspend_account_bp.route('/suspend_account/<int:id>', methods=['POST'])
    def suspend_account(id):
        pass


# Search Account Controller
search_account_bp = Blueprint('search_account', __name__)
class SearchProfileController:
    @staticmethod
    @search_account_bp.route('/search_account', methods=['GET', 'POST'])
    def search_profile():
        pass
