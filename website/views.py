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
    return render_template("about.html")

@views.route('/my-orders')
def contact():
    return render_template("order.html")