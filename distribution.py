import numpy as np
#import cPickle as pickle
import pickle
import json

(ldak, phi, voca) = pickle.load(open('ldaphi_K5.p', "rb"))

words_to_column = {}
for i,w in enumerate(voca):
    words_to_column[w] = i

#tweets = json.loads(open("results.json").read())
#tweets=open('corp_without_hashAndDig.txt', 'r')
dist_file = open('dist.csv','w')

tweets=open('corp.txt', 'r')
f1=tweets.readlines();
for text in f1:
    #text = tweet.get('text')
    #title = tweet.get('title','').encode("ascii","ignore")
    #url = tweet.get('resolvedPageUrl',"").encode("ascii","ignore")

    sum_vector = np.zeros(ldak)
    for word in text.split():
        word = word.lower()
        if word in words_to_column:
            sum_vector += phi[:, words_to_column[word]]
    if sum_vector.sum() == 0:
        sum_vector = np.ones(ldak)/ldak;
    else:
        sum_vector = sum_vector / sum_vector.sum()

    print("%s,%s" % (",".join(["%2.3f" % s for s in sum_vector]), text))

    print ("%s,%s" %(",".join(["%2.3f" % s for s in sum_vector]),text),file=dist_file)

dist_file.close()