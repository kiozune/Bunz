from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
