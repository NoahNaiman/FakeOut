"""
Implementing a simple machine learning algorithm using Naive-Bayes to detect whether a news article
is fake news.
"""

# Imports
import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from bs4 import BeautifulSoup
import random

class Data:
	def __init__(self):
		print('[INITIALIZING SCRIPT]')

		# Importing and shaping the data
		df = pd.read_csv("data/fake_or_real_news 2.csv")
		df = df.set_index("Unnamed: 0")
		y = df.label
		df.drop("label", axis=1)
		X_train, X_test, y_train, y_test = train_test_split(df['text'], y, test_size=0.33, random_state=53)

		# Creating a count vector to detect the frequency of words in each article
		self.count_vect = CountVectorizer(stop_words='english')
		count_train = self.count_vect.fit_transform(X_train) 
		count_test = self.count_vect.transform(X_test)

		self.tfidf_transformer = TfidfTransformer()
		X_train_tfidf = self.tfidf_transformer.fit_transform(count_train)

		# Initializing the model
		self.clf = MultinomialNB().fit(X_train_tfidf, y_train)
		print('[READY]')

	def scrape(self, url):
		"""
			Takes in a url of and scrapes a news articles
			Inputs:
			url is a string
		"""
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
		soup = soup.find_all('p')
		article = ''
		for i in soup:
			article += i.getText()
		return article

	def run(self, article):
		docs_new = [article]
		X_new_counts = self.count_vect.transform(docs_new)
		X_new_tfidf = self.tfidf_transformer.transform(X_new_counts)
		predicted = self.clf.predict(X_new_tfidf)
		return str(predicted[0])

	def alternative_article(self,article):

		global_warming = pd.read_csv("Scrapping_files/Global_warming_art.csv")
		russia = pd.read_csv("Scrapping_files/Russia_art.csv")
		north_korea = pd.read_csv("Scrapping_files/North_korea_art.csv")
		result = []
		new_article = article.split()
		print('New Article:', new_article)
		for i in range(0,len(new_article)):
			if new_article[i].lower() == 'warming' or new_article[i].lower() == 'global':
				output = random.sample(range(1, 15), 3)
				np.vstack(arr[:,:]).astype(np.float)
				result.append(global_warming.values[output[0]].tolist())
				result.append(global_warming.values[output[1]].tolist())
				result.append(global_warming.values[output[2]].tolist())
				break
			if new_article[i] == 'climate':
				output = random.sample(range(1, 15), 3)
				result.append(global_warming.values[output[0]].tolist())
				result.append(global_warming.values[output[1]].tolist())
				result.append(global_warming.values[output[2]].tolist())
				break

			elif new_article[i] == 'Russia':		
				output = random.sample(range(1, 14), 3)
				result.append(russia.values[output[0]].tolist())
				result.append(russia.values[output[1]].tolist())
				result.append(russia.values[output[2]].tolist())
				break
			elif new_article[i] == 'Korea':
				output = random.sample(range(1, 15), 3)
				result.append(north_korea.values[output[0]].tolist())
				result.append(north_korea.values[output[1]].tolist())
				result.append(north_korea.values[output[2]].tolist())
				break
		print('Result:', result)
		return result