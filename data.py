'''
Implmenting a simple machine learning algorithm using Naive-Bayes to detect whether a news article
is fake news.
'''

# Imports
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

print('[LOADING]')

# Importing and shaping the data
df = pd.read_csv("data/fake_or_real_news 2.csv")
df = df.set_index("Unnamed: 0")
y = df.label
df.drop("label", axis=1)
X_train, X_test, y_train, y_test = train_test_split(df['text'], y, test_size=0.33, random_state=53)

# Creating a count vector to detect the frequency of words in each article
count_vect = CountVectorizer(stop_words='english')
count_train = count_vect.fit_transform(X_train) 
count_test = count_vect.transform(X_test)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(count_train)

# Initializing the model
clf = MultinomialNB().fit(X_train_tfidf, y_train)
print('[READY]')

# Input and output of the model
while True:
	try:
		docs_new = []
		docs_new.append(raw_input(''))
		X_new_counts = count_vect.transform(docs_new)
		X_new_tfidf = tfidf_transformer.transform(X_new_counts)
		predicted = clf.predict(X_new_tfidf)
		print(str(predicted[0]))
	except (EOFError):
		break

	