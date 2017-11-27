print(__doc__)

import preprocessing
import pandas as pd

t=open('labelled_with_ids.csv', 'w')

#df = pd.read_csv('dist_with_ids_6.csv',header=0)
df = pd.read_csv('dist.csv',header=0,encoding='cp1252') # cp1252 for windows utf-8 for linux
#tweet_ids=list()
#tweet_ids2=list()
#tweet_ids3=list()

total_topics = 5 # total cols = total_topics+3 hence 0:total_topics+2

X = df.as_matrix(columns=df.columns[0:total_topics+2])

for x1 in X.tolist():

    max=x1[0];
    ind=0;
    for i in range(1,total_topics): # range is always lower than upper bound
        #print (i)
        if(max<x1[i]):
            max=x1[i];
            ind=i;
            #print (ind)
    R=x1[total_topics]
    r2=str(ind)
    #print ("%s,%s,%s" % (r2,str(int(R)),str(x1[ind])))
    print("%s,%s,%s" % (r2, str(R), str(x1[ind])))
    R1 = r2+","+R
    t.write(R1)
    t.write("\n")

t.close()