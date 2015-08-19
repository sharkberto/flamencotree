
# coding: utf-8

# In[247]:


# Author: Olivier Grisel <olivier.grisel@ensta.org>
#         Lars Buitinck <L.J.Buitinck@uva.nl>
# License: BSD 3 clause

from __future__ import print_function
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

from nltk.corpus import stopwords
spanishstop = stopwords.words('spanish')


# In[248]:

n_samples = 2500
n_features = 300
n_topics = 10
n_top_words = 20


# In[249]:

# http://scikit-learn.org/stable/auto_examples/applications/topics_extraction_with_nmf.html#example-applications-topics-extraction-with-nmf-py
# Load the 20 newsgroups dataset and vectorize it. We use a few heuristics
# to filter out useless terms early on: the posts are stripped of headers,
# footers and quoted replies, and common English words, words occurring in
# only one document or in at least 95% of the documents are removed.


print("Loading dataset and extracting TF-IDF features...")
dataset = []
datalabels = []
#
linenums = []
sample_ix = 0
with open ('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\true_palos_simple.txt', 'r') as labels:
    for line in labels:
        line = line.rstrip('\n')
        datalabels.append(line)
           
with open ('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\lyrics.txt', 'r') as samples:
    for line in samples:  # opened in text-mode; all EOLs are converted to '\n'
        line = line.rstrip('\n')
        dataset.append(line)
verse_counts = []
count = 0
with open ('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\verse_counts.txt') as counts:
    for line in counts:  # opened in text-mode; all EOLs are converted to '\n'
        dataset[count]+=str(line)
        count +=1
           # for ix in range(len(dataset)):
               # dataset[ix].join(line)


# In[250]:

#sort datalabels 
#remove duplicates and make this datalabelnames
#create datalabelnums array for range of 1:len(datalabels)
datalabelnames = sorted(set(datalabels))
datalabelnums =[None] * len(datalabels)                        
for i in range(len(datalabels)): 
    for j in range(len(datalabelnames)): 
        if datalabels[i]==datalabelnames[j]:
            datalabelnums[i] = j


# In[251]:

t0 = time()
vectorizer = TfidfVectorizer(max_df=0.95, min_df=4, max_features=n_features, stop_words=spanishstop) # Equivalent to CountVectorizer followed by TfidfTransformer.
tfidf = vectorizer.fit_transform(dataset)
# Fit the NMF model
print("Fitting the NMF model with n_samples=%d and n_features=%d..."
      % (n_samples, n_features))
nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
print("done in %0.3fs." % (time() - t0))


# In[252]:

feature_names = vectorizer.get_feature_names()

for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


# <b>MultinomialNB Classifier</b>

# In[253]:

tfidf.getnnz()


# In[254]:

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
categories = datalabelnames


# In[255]:

# get labels from training set and map them to the index of the list of categories
# for t in twenty_train.target[:10]:
# ...     print(twenty_train.target_names[t])
#

clf = MultinomialNB().fit(tfidf, datalabels)


# In[256]:

new_docs = []
with open('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\lyrics.txt') as test:
    count = 0
    for line in test:
        line = line.rstrip('\n')
        if count < 900:
            new_docs.append(line)
            count += 1

testverse_counts = []
count = 0
with open('C:\\Users\\Alex\\Documents\\flamenco_data\\raw_scraped_data\\verse_counts.txt') as testv:
    for line in testv:
        if count < 900:
            new_docs[count]+=str(line)
            count +=1



# In[257]:

X_new_tfidf = vectorizer.transform(new_docs)
predicted = clf.predict(X_new_tfidf)


# In[258]:

for doc, category in zip(new_docs, predicted):
     print('%r => %s' % (doc, category)) #twenty_train.target_names[category]


# In[259]:

np.mean(predicted==datalabels[0:900])


# In[260]:

from sklearn import metrics
print(metrics.classification_report(datalabels[:900], predicted)) #test set needs to be accurately labeled


# In[261]:

from sklearn.datasets import fetch_20newsgroups
import numpy as np
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)

