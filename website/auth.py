from flask import Blueprint, flash, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        Username = request.form.get("username")

        if len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(Username) < 2:
            flash("Email must be greater than 1 characters", category="error")
        else:
            flash("Account created!", category="success")
    return render_template("sign-up.html")

@auth.route('/schedule-pick')
def schedule_pick():
    return render_template("schedules.htnl")