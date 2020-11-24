import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
import networkx as nx
#print(brown.categories())
# meat = wn.synset('dry.n.01')
# print(meat.hypernyms())
# hyper  = lambda s: s.hypernyms()
# print(list(meat.closure(hyper)))
#
# G = nx.Graph()
#
# print(G.get_edge_data(0, 1))
print({1,2} == {2,1})
print(type({1,2}))
dic = {1:2}
l = [2, 1]
print(l.sort())
print(l)
print(dic.get(3))
a = [1,3]
b = [2,4]
print(a+b)