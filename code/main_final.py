import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# g = nx.read_edgelist('twitter_combined.txt', create_using = nx.Graph(), nodetype = int)

# print (nx.info(g))

# sp = nx.spring_layout(g)

# plt.axis('off')

# nx.draw_networkx(g, pos = sp, with_labels=False, node_size = 350)

# plt.show()

# print("Completed!")

def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    print("Completed 1")
    G.add_edges_from(array)
    print("Completed 2")
    return G

nx.draw(read_graph("twitter_combined.txt"))
plt.savefig("graph.pdf")

print("Completed!!!")