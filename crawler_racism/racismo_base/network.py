import csv
import networkx as nx 


G = nx.DiGraph() 


with open('/home/guibson/crawler/racismo_base/PageRank-master/RTs_racismo_graphID.csv', 'r') as tsvin: 
    tsvin = csv.reader(tsvin, delimiter=',') 
    for row in tsvin: 
        sender = row[0]
        recipients = row[1].split(',') 
        for recipient in recipients: 
            G.add_edge(sender, recipient) 

print (nx.info(G))
print (nx.betweenness_centrality(G))

#fh = open("/home/guibson/crawler/racismo_base/RTs_racismo_graphID.txt", 'r', delimiter=',')
#g = nx.read_edgelist(fh, create_using=nx.Graph(), nodetype=int)

#print(nx.info(g))

#print(nx.betweenness_centrality(g, normalized=False))
