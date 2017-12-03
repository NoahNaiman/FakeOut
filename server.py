from data import Data
from flask import Flask
from flask import request
app = Flask(__name__)

checker = Data()
url = ''

@app.route('/', methods=['POST'])
def index():
	url = request.data
	print('\n', url, '\n')
	print(checker.run("This is a cool site"))
	return('Hello, World!');

if __name__ == "__main__":
	app.run(ssl_context=('server.crt', 'server.pem'))
