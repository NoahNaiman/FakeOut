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
		soup = soup.find(attrs={'class': None})
		article = ''
		for i in soup:
			article += i.getText()
		print(article)
		return article

	def run(self, string):
		docs_new = [self.scrape(string)]
		# print("HEEEEELLLLLOOOOO!", docs_new)
		# docs_new.append(string)
		X_new_counts = self.count_vect.transform(docs_new)
		X_new_tfidf = self.tfidf_transformer.transform(X_new_counts)
		predicted = self.clf.predict(X_new_tfidf)
		return str(predicted[0])