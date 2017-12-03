from flask import flask, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def fakeNews():
