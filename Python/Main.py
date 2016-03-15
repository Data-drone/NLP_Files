
import pandas as pd
import os.path
#import textmining - breaks with float objects
from sklearn.feature_extraction.text import CountVectorizer

path = '../NYTimes_Data/'

dataSet = pd.read_csv(os.path.join(path, 'NYTimesBlogTrain.csv'))
#tdm = textmining.TermDocumentMatrix()

vectorizer = CountVectorizer()
x1 = vectorizer.fit_transform(dataSet['Abstract'].dropna())

df = pd.DataFrame(x1.toarray().transpose(), index = vectorizer.get_feature_names())

df.columns = 

