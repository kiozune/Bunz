from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import UserProfile
from forms import UserProfileForm

# Create Profile Controller
create_profile_bp = Blueprint('create_profile', __name__)
class CreateProfileController:
    @staticmethod
    @create_profile_bp.route('/create_profile', methods=['GET', 'POST'])
    def create_profile():
        # Create an instance for UserProfileForm()
        form = UserProfileForm()
        if form.validate_on_submit():
            try:
                new_profile = UserProfile.create_profile(
                    role=form.role.data,
                    description=form.description.data
                )
                # Flash message if the role is successfully created
                flash(f'{new_profile.role} created successfully!', 'success')
                return redirect(url_for('view_profile.view_profile'))
            except ValueError as e:
                # Flash the error message to notify the users
                flash(str(e), 'danger')
                return redirect(url_for('create_profile.create_profile'))
        return render_template('create_profile.html', form=form)


# View Profile Controller
view_profile_bp = Blueprint('view_profile', __name__)
class ViewProfileController:
    @staticmethod
    @view_profile_bp.route('/view_profile')
    def view_profile():
        # Instance that get all the profile stored in the database
        profiles = UserProfile.get_all_profile()
        return render_template('profile_management.html', profiles=profiles)


#Update profile details controller
update_profile_bp = Blueprint('update_profile', __name__)
class UpdateProfileController:
    @staticmethod
    @update_profile_bp.route('/update_profile/<int:id>', methods=['GET', 'POST'])
    def update_profile(id):
        # Retrieve the existing profile by ID
        profile = UserProfile.get_profile_by_id(id)

        # Initialize the form and populate it with the existing profile data
        form = UserProfileForm(obj=profile)
        if form.validate_on_submit():
            try:
                updated_profile = UserProfile.update_profile(
                    profile_id=id,
                    new_role=form.role.data,
                    new_description=form.description.data
                )
                flash(f'Profile for role "{updated_profile.role}" updated successfully!', 'success')
                return redirect(url_for('view_profile.view_profile', id=profile.id))
            except ValueError as e:
                flash(str(e), 'danger')
                return redirect(url_for('update_profile.update_profile', id=id))

        return render_template('update_profile.html', form=form, profile=profile)


# Suspend profile controller
suspend_profile_bp = Blueprint('suspend_profile', __name__)
class SuspendProfileController:
    @staticmethod
    @suspend_profile_bp.route('/suspend_profile/<int:id>', methods=['GET'])
    def suspend_profile(id):
        try:
            suspend_profile = UserProfile.suspend_profile(id)
            flash(f"Profile {suspend_profile.role} has been suspended successfully", 'success')
        except ValueError as e:
            flash(str(e), 'danger')
            return redirect(url_for('view_profile.view_profile', id=id))
        return render_template('profile_management.html')


# Search the profile controller
search_profile_bp = Blueprint('search_profile', __name__)
class SearchProfileController:
    @staticmethod
    @search_profile_bp.route('/search_profile', methods=['GET', 'POST'])
    def search_profile():
        query = request.args.get('query', '')
        if query:
            results = UserProfile.search_profile(query)
            if not results:
                flash('No Profile Found', 'info')
            return render_template('profile_management.html', profiles=results, query=query)
        return render_template('profile_management.html', profiles=[], query=query)
