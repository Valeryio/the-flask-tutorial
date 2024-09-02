from market import app
from market import db
from market.models import Item, User
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.forms import RegisterForm, LoginForm


@app.route("/")
def index():
    firstnames = ["Linson", "Valery", "Gnona", "Fifa"]
    return render_template("index.html", names=firstnames)


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    all_items = Item.query.all()
    return render_template("market.html", all_items=all_items)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email_address.data,
                              password=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("market_page"))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error when creating user {err_msg}", category="danger")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()

    return render_template("login.html", form=form)
