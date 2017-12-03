from data import Data
from flask import Flask
from flask import request
app = Flask(__name__)

checker = Data()
url = ''

@app.route('/', methods=['POST'])
def index():
	result = []
	url = request.data.decode('utf-8')
	article = checker.run(url)
	news_type = checker.run(article)
	result.append(news_type)
	if news_type == 'FAKE':
		articles = checker.alternative_article(news_type)
		result.append(articles)
	return(result);

if __name__ == "__main__":
	app.run(ssl_context=('server.crt', 'server.pem'))