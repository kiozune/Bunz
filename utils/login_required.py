from functools import wraps
from flask import redirect, url_for, flash, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.", 'warning')
            return redirect(url_for('login.login'))
        return f(*args, **kwargs)
    return decorated_function
