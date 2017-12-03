from data import Data
from flask import Flask
from flask import request
app = Flask(__name__)

checker = Data()
url = ''

@app.route('/', methods=['POST'])
def index():
	url = request.data.decode('utf-8')
	# print('\n', url, '\n')
	print(checker.run(url))
	return('Hello, World!');

if __name__ == "__main__":
	app.run(ssl_context=('server.crt', 'server.pem'))
