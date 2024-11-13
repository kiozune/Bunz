from functools import wraps
from flask import redirect, url_for, flash, session

def buyer_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.", 'warning')
            return redirect(url_for('login.login'))
        elif session.get('role_id') != 2:
            flash("Unauthorized Page.", 'warning')
            return redirect(url_for('unauthorized'))
        return f(*args, **kwargs)
    return decorated_function
