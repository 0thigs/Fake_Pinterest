from flask import render_template, url_for
from fakepinterest import app

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/user/<user>")
def profile(user):
    return render_template('profile.html', user=user)