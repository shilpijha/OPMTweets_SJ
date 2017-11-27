print(__doc__)

import preprocessing
import pandas as pd
import time

corp_txt =open('corp.txt','w',errors='ignore') # write output to corp.txt file, windows uses cp1252 and linux uses utf-8 encoding

df = pd.read_csv('tw_bought.csv',header=0) # read tw_bought.csv file which containg 18000 tweets
#tweet_ids=list()
#tweet_ids2=list()
#tweet_ids3=list()
X = df.as_matrix(columns=df.columns[0:7]) # segregate columns into matrix form

for x in X.tolist():
    R=''.join(x[6]) # tweet column data
    id1=int(x[0]) # contain userid
    d1=''.join(x[1]) # date column data
    d1=d1+' '
    t1=''.join(x[2]) # time column data
    dt=d1+t1
    struct_Time= time.mktime(time.strptime(dt,'%Y-%m-%d %H:%M')) # combine date and time into single data format
    #print (R)
    t= preprocessing.processAll(R) # remove all special characters from tweet and convert them into readable words
    print(t, ',', id1, ',', struct_Time)
    print(t,',',id1,',',struct_Time,file=corp_txt) # write to output file as well

    #corp_txt.write(pr_txt) # write to output file

df1 = pd.read_csv('tw_main.csv',header=0) # read main.csv file
#tweet_ids=list()
#tweet_ids2=list()
#tweet_ids3=list()
X1 = df1.as_matrix(columns=df1.columns[0:3]) # read only 3 columns

for x1 in X1.tolist():
    R1=''.join(x1[1]) # contain tweets
    id2=int(x1[0]) # contain user id
    dt2=''.join(x1[2]) # contain data time combined format
    #print (dt2)
    #try:
    #struct_Time1=time.mktime(time.strptime(dt2,'%Y-%m-%d %H:%M'))
    t1= preprocessing.processAll(R1)

    print (t1,',',id2,',',dt2)
    print(t1, ',', id2, ',', dt2,file=corp_txt) #write to file as well
    #except:
    #    i=1

corp_txt.close()