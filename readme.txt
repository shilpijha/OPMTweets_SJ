There were 2 csv files with the twitter data tw_bought.csv and tw_main.csv


For just getting the number of tweets and the words in a topic

1)to combine the formats in both the .csv's run make_corpus.py and redirect the output to a .txt say for example 'corp.txt'.
Currently make_corpus.py contains code to add the timestamp and ID with each tweet for making a csv but you don't need that for just modelling LDA,you'll need to make a csv later 
for assigning a category to each tweet.

2)Next use the generated file from step 1 as an argument for lda.py and use the 'k' argument to assign the number of topics so a typical comman can be something like
'lda.py corp.txt -k 3' for 3 topics.You can add other features to the LDA model like initial seed etc.... This model will generate a file called 'ldaphiK_3.p' which is a pickel file.

3)Open distribution.py and change line [(ldak, phi, voca) = pickle.load(open('ldaphi_K3.p', "rb"))] to replace "ldaphi_K3.p" to whatever file you've generated,aldo change the filename in 
  [tweets=open('corp.txt', 'r')] to the name of the corpora generated in step 1. Redirect the output of this to another .csv , for example 'dist.csv', this will contain the probability of the tweet being in every topic(in order) and the text of the topics

4)run labeller.py which chooses the highest probability and assigns a topic to every tweet


For getting tweet number assigned to a topic number

1) Same as the previous step one but generate a .csv with tweet and ids as well as the .txt.

2)Same 
 
3) use dist_with_ids.py instead,make the same changes except this time use the .csv

4)Same

