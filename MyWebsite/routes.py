from flask import Blueprint, render_template

routes = Blueprint(__name__, "routes")

@routes.route("/")
def home():
    return render_template("home.html")