import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from thinkstats2 import Cdf, Pmf
import thinkplot

from networkx.algorithms.approximation import average_clustering

print("Initializing...")

def degrees(G):
    """List of degrees for nodes in `G`.
    
    G: Graph object
    
    returns: list of int
    """
    return [G.degree(u) for u in G]

def hk_ba_graph(n, k, seed=None):
    """Constructs a BA graph.
    
    n: number of nodes
    k: number of edges for each new node
    seed: random seed

    from jupyter notebook
    """
    if seed is not None:
        random.seed(seed)
    
    G = nx.empty_graph(k)
    targets = list(range(k))
    repeated_nodes = []

    for source in range(k, n):
        G.add_edges_from(zip([source]*k, targets))

        G.add_edges_from(holme_kim(G, source, targets))

        repeated_nodes.extend(targets)
        repeated_nodes.extend([source] * k)

        targets = _random_subset(repeated_nodes, k)

    return G

def _random_subset(repeated_nodes, k):
    """Select a random subset of nodes without repeating.
    
    repeated_nodes: list of nodes
    k: size of set
    
    returns: set of nodes

    from jupyter notebook
    """
    targets = set()
    while len(targets) < k:
        x = random.choice(repeated_nodes)
        targets.add(x)
    return targets

def holme_kim(G, source, targets):
	triads = []
	for target in targets:
		random_neighbor = random.choice(G.neighbors(target))
		if G.has_edge(random_neighbor, source) | G.has_edge(source, random_neighbor):
			pass
		else:
			triads.append((source, random_neighbor))
	return triads

def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G

def random_path_lengths(G, nodes=None, trials=1000):
    """Choose random pairs of nodes and compute the path length between them.

    G: Graph
    nodes: list of nodes to choose from
    trials: number of pairs to choose

    returns: list of path lengths
    """
    if nodes is None:
        nodes = G.nodes()
    else:
        nodes = list(nodes)
        
    pairs = np.random.choice(nodes, (trials, 2))
    lengths = [nx.shortest_path_length(G, *pair) 
               for pair in pairs]
    return lengths

def estimate_path_length(G, nodes=None, trials=1000):
    return np.mean(random_path_lengths(G, nodes, trials))

fb = read_graph('facebook_combined.txt.gz')
fb_clustering = average_clustering(fb)
fb_length = estimate_path_length(fb)

n = len(fb)
m = len(fb.edges())

k = int(round(m/n))
hk_graph = hk_ba_graph(n, k)

pmf_fb = Pmf(degrees(fb))
pmf_hk = Pmf(degrees(hk_graph))

thinkplot.preplot(cols=2)

thinkplot.Pdf(pmf_fb, style='.', label='Facebook')
thinkplot.config(xscale='log', yscale='log',
	xlabel='degree', ylabel='PMF')

thinkplot.subplot(2)

thinkplot.Pdf(pmf_hk, style='.', label='HK graph')
thinkplot.config(xscale='log', yscale='log',
	xlabel='degree', ylabel='PMF')

plt.savefig('PMFGraphs.pdf')

print("Degrees:", len(degrees(fb)), len(degrees(hk_graph)))
print("Clustering:", fb_clustering, average_clustering(hk_graph))
print("Path length:", fb_length, estimate_path_length(hk_graph))
print("Mean degrees:", np.mean(degrees(fb)), np.mean(degrees(hk_graph)))

# nx.draw(read_graph("twitter_combined.txt"))
# plt.savefig("graph.pdf")

# twitter = read_graph('twitter_combined.txt.gz')
# twitter_clustering = average_clustering(twitter)
# twitter_length = estimate_path_length(twitter)

# n = len(twitter)
# m = len(twitter.edges())
# k = int(round(m/n))
# hk_graph = hk_ba_graph(n, k)

# print("Degrees:", len(degrees(twitter)), len(degrees(hk_graph)))
# print("Clustering:", twitter_clustering, average_clustering(hk_graph))
# print("Path length:", twitter_length, estimate_path_length(hk_graph))
# print("Mean degrees:", np.mean(degrees(twitter)), np.mean(degrees(hk_graph)))

# cdf_twitter = Cdf(degrees(twitter), label='Twitter')
# cdf_hk_graph = Cdf(degrees(hk_graph), label='HK')
# thinkplot.Cdf(cdf_twitter)
# thinkplot.Cdf(cdf_hk_graph, color='gray')
# thinkplot.config(xscale='log', xlabel='log(degree)', ylabel='CDF')

print("Completed!")