from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("base.html")

@views.route('/home')
def home():
    return render_template("base.html")

@views.route('/about')
def about():
    return "<h1>About Us Page</h1>"

@views.route('/contact')
def contact():
    return "<h1>Contact Page</h1>"