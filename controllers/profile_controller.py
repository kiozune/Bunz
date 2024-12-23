from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import UserProfile
from utils import login_required, admin_only

# Create Profile Controller
create_profile_bp = Blueprint('create_profile', __name__)
class CreateProfileController:
    @staticmethod
    @create_profile_bp.route('/create_profile', methods=['GET', 'POST'])
    @login_required
    @admin_only
    def create_profile():
        if request.method == 'POST':
            role = request.form.get('role').strip()
            description = request.form.get('description').strip()

            try:
                new_profile = UserProfile.create_profile(role, description)
                # Flash message if the role is successfully created
                flash(f'{role} created successfully!', 'success')
            except ValueError as e:
                # Flash the error message to notify the users
                flash(str(e), 'danger')
                return render_template('profile/create_profile.html')
        return render_template('profile/create_profile.html', title='Create New Profile')


# View Profile Controller
view_profile_bp = Blueprint('view_profile', __name__)
class ViewProfileController:
    @staticmethod
    @view_profile_bp.route('/view_profile')
    @login_required
    @admin_only
    def view_profile():
        # Instance that get all the profile stored in the database
        profiles = UserProfile.get_all_profile()
        return render_template('profile/profile_management.html', profiles=profiles, title='Profile Management')


# Update profile details controller
update_profile_bp = Blueprint('update_profile', __name__)
class UpdateProfileController:
    @staticmethod
    @update_profile_bp.route('/update_profile/<int:id>', methods=['GET', 'POST'])
    @login_required
    @admin_only
    def update_profile(id):
        # Retrieve the existing profile by ID
        profile = UserProfile.get_profile_by_id(id)
        if request.method == 'POST':
            role = request.form.get('role').strip()
            description = request.form.get('description').strip()

            try:
                updated_profile = UserProfile.update_profile(
                    profile.id, role, description
                )
                flash(f'Profile for role "{role}" updated successfully!', 'success')
            except ValueError as e:
                flash(str(e), 'danger')
                return render_template('profile/update_profile.html', id=id, title='Update Profile')

        return render_template('profile/update_profile.html', profile=profile, title='Update Profile')


# Suspend profile controller
suspend_profile_bp = Blueprint('suspend_profile', __name__)
class SuspendProfileController:
    @staticmethod
    @suspend_profile_bp.route('/suspend_profile/<int:id>', methods=['POST'])
    @login_required
    @admin_only
    def suspend_profile(id):
        profiles = UserProfile.get_all_profile()
        try:
            suspend_profile = UserProfile.suspend_profile(id)
            flash(f"Profile {UserProfile.get_profile_by_id(id).role} has been suspended successfully", 'success')
            return render_template('profile/profile_management.html', profiles=profiles, title='Profile Management')
        except ValueError as e:
            flash(str(e), 'danger')


# Search the profile controller
search_profile_bp = Blueprint('search_profile', __name__)
class SearchProfileController:
    @staticmethod
    @search_profile_bp.route('/search_profile', methods=['GET', 'POST'])
    @login_required
    @admin_only
    def search_profile():
        query = request.args.get('query', '').strip()
        profiles = UserProfile.get_all_profile()
        if query == '':
            return render_template('profile/profile_management.html', profiles=profiles, title='Profile Management')
        elif query:
            results = UserProfile.search_profile(query)
            return render_template('profile/profile_management.html', profiles=results, query=query, title='Profile Management')
        return render_template('profile/profile_management.html', profiles=profiles, title='Profile Management')
