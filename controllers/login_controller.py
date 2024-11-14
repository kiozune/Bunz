from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import UserAccount

login_bp = Blueprint('login', __name__)

class LoginController:
    @staticmethod
    @login_bp.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = UserAccount.query.filter_by(username=username).first()

            if user:
                if user.is_suspended:
                    flash('Your account has been suspended. Please call the customer support for help'
                          , 'warning')
                    return render_template('login.html', title='Login Page')

                if user.check_password(password):
                    session['user_id'] = user.id
                    session['username'] = user.username
                    session['role_id'] = user.role_id
                    return redirect(url_for('index'))
                else:
                    flash('Invalid username or password', 'danger')
                    return render_template('login.html', title='Login Page')

        return render_template('login.html', title='Login Page')

    @staticmethod
    @login_bp.app_context_processor
    def inject_user():
        user_id = session.get('user_id')
        if user_id:
            user = UserAccount.query.get(user_id)
            return {'username': user.username if user else None}
        return {'username': None}
