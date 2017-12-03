from data import Data
from flask import Flask
from flask import request
app = Flask(__name__)

d = Data()

@app.route('/', methods=['POST'])
def index():
	rd = request.data
	print(rd)
	return d.run("This is a cool site")

if __name__ == "__main__":
	app.run(ssl_context=('server.crt', 'server.pem'))
