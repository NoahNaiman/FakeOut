from data import Data
from flask import Flask
app = Flask(_name_)

d = Data()

@app.before_first_request
def _run_on_start():
	d.run()

@app.route("/")
def run_server():
	print('hi')
