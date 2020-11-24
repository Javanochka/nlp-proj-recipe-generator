import networkx as nx
import matplotlib.pyplot as plt
import pickle


G = nx.Graph()
path = r'E:\编程文件\python\Uni Lorraine\recipeCreator\all_nodes.txt'
edges = dict()

with open(path, 'r') as file:
    time = 0

    for i in file.readlines():

        time += 1
        nodes = i[:-2].split(' ')
        temp_edges = []

        for start in range(len(nodes)-1):

            for mark in range(start+1, len(nodes)):
                l = [nodes[start], nodes[mark]]
                l.sort()
                temp_edges.append(tuple(l))

        for x in temp_edges:

            if(edges.get(x) == None):
                edges[x] = 1

            else:
                edges[x] +=1

print(edges)
network_path = r'E:\编程文件\python\Uni Lorraine\recipeCreator\network.pkl'
with open(network_path, 'wb') as file:
    pickle.dump(edges, file, pickle.HIGHEST_PROTOCOL)

for edge, weight in edges.items():
    G.add_weighted_edges_from([(edge[0], edge[1], weight)])

pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=False, node_size=30)
# plt.show()