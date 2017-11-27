import networkx as nx
import string
#from sys import maxint

import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('for_graph5.csv',header=0)
df = pd.read_csv('labelled_with_ids.csv',header=0,encoding='cp1252')
X = df.as_matrix(columns=df.columns[0:2])


#wordList2 = [string.rstrip(x.lower(), ',.!?;') for x in wordList1]

dG = nx.DiGraph()

for x in X.tolist():
    R=''.join(x[1])
    if(int(x[0])==4):
        str1=R
        wordList1 = str1.split(None)
        #print (wordList1)
        for i, word in enumerate(wordList1):
             word = word.title()
             try:
                 next_word = wordList1[i + 1]
                 next_word = next_word.title()
                 if not next_word is word:
                     if not dG.has_node(word):
                         dG.add_node(word)
                         dG.node[word]['count'] = 1
                     else:
                        dG.node[word]['count'] += 1
                     if not dG.has_node(next_word):
                        dG.add_node(next_word)
                        dG.node[next_word]['count'] = 0

                     if not dG.has_edge(word, next_word):
                         dG.add_edge(word, next_word, weight=0)
                     else:
                         dG.edge[word][next_word]['weight'] += 1
             except IndexError:
                 if not dG.has_node(word):
                   dG.add_node(word)
                   dG.node[word]['count'] = 1
                 else:
                   dG.node[word]['count'] += 1
             except:
                 raise


nlarge_node =[u for (u,d) in dG.nodes(data=True) if d['count'] >100]

#elarge=[(u,v) for (u,v,d) in dG.edges(data=True) if d['weight'] >10]
#nlarge_edge =[(u,v) for (u,v,d) in dG.edges(data=True) if d['weight'] >100]
#nlarge1=[v for (u,v,d) in dG.edges(data=True) if d['weight'] >200]
#esmall=[(u,v) for (u,v,d) in dG.edges(data=True) if d['weight'] <=1000]
#print (nlarge_node)
#print (nlarge_edge)
dG1=dG.subgraph(nlarge_node)

#pos=nx.spring_layout(dG1,iterations=500,weight='weight')
#nx.draw(dG1,pos,node_color='#A0CBE2',node_size=1000,node_shape='s',edge_color='#BB0000',edge_cmap=plt.cm.Blues)
#plt.show()
#pos=nx.spectral_layout(dG1) # positions for all nodes

# nodes
#nx.draw_networkx_nodes(dG1,pos,node_size=1000,node_shape='s')
#nx.draw_networkx_nodes(dG,pos,nodelist=nlarge2,node_size=500)

#nx.draw_networkx_nodes(dG,pos,nodelist=nlarge1,node_size=200)

# edges
#nx.draw_networkx_edges(dG1,pos,width=1)
#nx.draw_networkx_edges(dG,pos,edgelist=esmall,width=6,alpha=0.5,edge_color='b',style='dashed')

# labels
#nx.draw_networkx_labels(dG1,pos,font_size=8,font_family='sans-serif')
#nx.draw_networkx_labels(dG,pos,nodelist=nlarge2,font_size=10,font_family='sans-serif')

#nx.draw_shell(dG1)
nx.write_graphml(dG1,'K5_T4_100.graphml')

#plt.axis('off')
#plt.savefig("topic_2_200.png") # save as png
#plt.show() # display
