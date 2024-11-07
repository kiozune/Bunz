from flask import Blueprint, render_template, request, redirect, url_for, flash, session

logout_bp = Blueprint('logout', __name__)
class LogoutController:
    @staticmethod
    @logout_bp.route('/logout')
    def logout():
        session.clear()  # Clears all session data
        flash("You have been logged out.", 'info')
        return redirect(url_for('login.login'))
