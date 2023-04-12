from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "login page"

@auth.route('/sign-up')
def sign_up():
    return "sign-up"

@auth.route('/schedule-pick')
def schedule_pick():
    return "<h1>Schedule your pick up...</h1>"