from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import UserAccount, UserProfile
from utils import login_required
from sqlalchemy.exc import IntegrityError

# Create Account Controller
create_account_bp = Blueprint('create_account', __name__)
class CreateAccountController:
    @staticmethod
    @create_account_bp.route('/create_account', methods=['GET', 'POST'])
    @login_required
    def create_account():
        roles = UserProfile.query.all()
        if request.method == 'POST':
            username = request.form.get('username').strip()
            password = request.form.get('password').strip()
            role_id = request.form.get('role_id').strip()
            email = request.form.get('email').strip()
            phone = request.form.get('phone').strip()

            try:
                new_account = UserAccount.create_account(username, password, role_id, email, phone)
                # Flash message if the role is successfully created
                flash(f'{username} created successfully!', 'success')
            except ValueError as e:
                # Flash the error message to notify the users
                flash(str(e), 'danger')
                return render_template('account/create_account.html', roles=roles, username=username,
                                       email=email, phone=phone, title='Create New Account')
            except IntegrityError as e:
                flash('Integrity error: ' + str(e.orig), 'danger')

        return render_template('account/create_account.html', roles=roles, title='Create New Account')


# View Account Controller
view_account_bp = Blueprint('view_account', __name__)
class ViewAccountController:
    @staticmethod
    @view_account_bp.route('/view_account')
    @login_required
    def view_account():
        # Instance that get all the accounts stored in the database
        account = UserAccount.get_all_accounts()
        return render_template('account/account_management.html', account=account, title='Account Management')


# Update Account Controller
update_account_bp = Blueprint('update_account', __name__)
class UpdateAccountController:
    @staticmethod
    @update_account_bp.route('/update_account/<int:id>', methods=['GET', 'POST'])
    @login_required
    def update_account(id):
        # Retrieve the existing profile by ID
        # Retrieve the existing profile by ID
        account = UserAccount.get_account_by_id(id)
        roles = UserProfile.query.all()
        if request.method == 'POST':
            username = request.form.get('username').strip()
            role_id = request.form.get('role_id').strip()
            email = request.form.get('email').strip()
            phone = request.form.get('phone').strip()

            try:
                updated_account = UserAccount.update_account(
                    account.id,  role_id, email, phone
                )
                flash(f'Account for "{username}" updated successfully!', 'success')
            except ValueError as e:
                flash(str(e), 'danger')
                return render_template('account/update_account.html',account=account, roles=roles,
                                       id=id, role=role_id, username=username, email=email, phone=phone,
                                       title='Update Account')

        return render_template('account/update_account.html', account=account, roles=roles, title='Update Account')


# Suspend Account Controller
suspend_account_bp = Blueprint('suspend_account', __name__)
class SuspendProfileController:
    @staticmethod
    @suspend_account_bp.route('/suspend_account/<int:id>', methods=['POST'])
    @login_required
    def suspend_account(id):
        account = UserAccount.get_all_accounts()
        try:
            suspend_account = UserAccount.suspend_account(id)
            flash(f"Profile {UserAccount.get_account_by_id(id).username} has been suspended successfully", 'success')
            return render_template('account/account_management.html', account=account, title='Account Management')
        except ValueError as e:
            flash(str(e), 'danger')


# Search Account Controller
search_account_bp = Blueprint('search_account', __name__)
class SearchProfileController:
    @staticmethod
    @search_account_bp.route('/search_account', methods=['GET', 'POST'])
    @login_required
    def search_account():
        query = request.args.get('query').strip()
        account = UserAccount.get_all_accounts()
        if query == '':
            return render_template('account/account_management.html', account=account, title='Account Management')
        elif query:
            results = UserAccount.search_account(query)
            return render_template('account/account_management.html', account=results, query=query,
                                   title='Account Management')
        return render_template('account/account_management.html', account=account, title='Account Management')
