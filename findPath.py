import networkx as nx
import pickle
import matplotlib.pyplot as plt

def find_shortest(path_dict:dict):
    shortest = 10000

    for key, value in path_dict.items():

        if (value < shortest):
            result_key = key
            shortest = value

    return result_key

network_path = r'E:\编程文件\python\Uni Lorraine\recipeCreator\network.pkl'
G = nx.Graph()

with open(network_path, 'rb') as file:
    network = pickle.load(file)

# print(network)

for edge, weight in network.items():
    weight = 1.0 / weight
    # print(weight)
    G.add_weighted_edges_from([(edge[0], edge[1], weight)])

# print(G.edges(data= True))
pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=False, node_size=30)
# plt.show()

nodes_input = [ 'eggplant', 'coffee', 'pudding']
nodes_isolate = []
all_groups = []
result = []
test = nodes_input[:]

for index in range(len(nodes_input)):

    if (G.degree(nodes_input[index]) == 0):

        nodes_isolate.append(nodes_input[index])
        nodes_input.pop(index)

while (len(nodes_input) != 0):

    node = nodes_input[0]
    temp_group = [node]
    index = 1

    while index < len(nodes_input):

        for node_source in temp_group:

            try:

                if(nx.has_path(G, node_source, nodes_input[index])):

                    temp_group.append(nodes_input[index])
                    nodes_input.pop(index)
            except:

                continue

        index += 1

    nodes_input.pop(0)
    all_groups.append(temp_group)
    temp_group = []

# print(all_groups)

for cell_group in all_groups:

    node_now = cell_group[0]
    nodes_done = []
    result.append(node_now)
    nodes_done.append(node_now)
    cell_group.pop(0)
    path_dict = dict()
    # length_dict = {node : nx.shortest_path_length(G, source=node_now, target=node) for node in cell_group if node != cell_group[0]}

    # print(length_dict)

    while (len(cell_group) != 0):

        for node_source in nodes_done:

            for node_target in cell_group:

                path_dict[(node_source, node_target)] = nx.shortest_path_length(G, source=node_source, target=node_target, weight='weight', method='dijkstra')

        print(path_dict)
        shortest_pair = find_shortest(path_dict)
        path_dict.clear()
        path = nx.shortest_path(G, source=shortest_pair[0], target=shortest_pair[1], weight='weight', method='dijkstra')
        result += path
        cell_group.remove(shortest_pair[1])

print({}.fromkeys(result).keys())
print(test)















