import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import thinkplot
from thinkstats2 import Cdf, Pmf
from networkx.algorithms.approximation import average_clustering

print("Initializing...")

def degrees(G):
    """List of degrees for nodes in `G`.

    G: Graph object

    returns: list of int
    """
    return [G.degree(u) for u in G]

def hk_graph_modified(n, p, m=2, seed=None):
    """Constructs a Holme-Kim graph.

    n: number of nodes
    p: probability of PA of edge to a given node
    k: number of edges for each new node
    seed: random seen
    """

    if m < 1 or n < m:
        raise ValueError(
            "NetworkXError must have m>1 and m<n, m=%d,n=%d" % (m, n))

    if p > 1 or p < 0:
        raise ValueError(
            "NetworkXError p must be in [0,1], p=%f" % (p))
    if seed is not None:
        random.seed(seed)

    G = nx.empty_graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0)])

    for source in range(m + 1, n):
        v, w = random.choice(G.edges())
        G.add_edge(source, v)
        G.add_edge(source, w)
    return G

def triad_formation(G, v, w):
    if G.neighbors(w) == [v]:
        random_neighbor = random.choice(G.neighbors(w))
        if not G.has_edge(v, random_neighbor):
            G.add_edge(v, random_neighbor)
    else:
        random_neighbor = random.choice(G.neighbors(v))
        G.add_edge(w, random_neighbor)
    return G

def _random_subset(repeated_nodes, k):
    """Select a random subset of nodes without repeating.

    repeated_nodes: list of nodes
    k: size of set

    returns: set of nodes
    """
    targets = set()
    while len(targets) < k:
        x = random.choice(repeated_nodes)
        targets.add(x)
    return targets

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

def flip(p):
    """Returns True with probability p."""
    return np.random.random() < p

def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G

def generate_pmf(fb, hk):
    pmf_fb = Pmf(degrees(fb))
    pmf_hk = Pmf(degrees(hk))

    thinkplot.plot([6, 150], [5e-1, 2e-4], color='gray', linestyle='dashed')

    thinkplot.Pdf(pmf_hk, style='.', label='Modified graph')
    thinkplot.config(xscale='log', yscale='log',
      xlabel='degree', ylabel='PMF')

    plt.savefig('PMFGraphs_Modified.png')

def generate_cdf(fb, hk):
    cdf_fb = Cdf(degrees(fb))
    cdf_hk = Cdf(degrees(hk))

    thinkplot.Cdf(cdf_fb, color='gray', label="Facebook CDF")
    thinkplot.Cdf(cdf_hk, label='Modified CDF')
    thinkplot.config(xlabel='degree', xscale='log',
                 ylabel='CDF')

    plt.savefig('CDFGraphs_Modified.png')

def generate_ccdf(fb, hk):
    cdf_fb = Cdf(degrees(fb))
    cdf_hk = Cdf(degrees(hk))

    thinkplot.Cdf(cdf_fb, label='Facebook CCDF', color='gray', complement=True)
    thinkplot.Cdf(cdf_hk, label="Modified CCDF", complement=True)
    thinkplot.config(xlabel='degree', xscale='log',
                 ylabel='CCDF', yscale='log')

    plt.savefig("CCDFGraphs_Modified.png")

def main():
    fb = read_graph('facebook_combined.txt.gz')
    fb_clustering = average_clustering(fb)
    fb_length = estimate_path_length(fb)

    n = len(fb)
    m = len(fb.edges())
    k = int(round(m/n))

    hk = hk_graph_modified(n, 1)

    # generate_pmf(fb, hk)
    # generate_cdf(fb, hk)
    generate_ccdf(fb, hk)

    print("Degrees:", len(degrees(fb)), len(degrees(hk)))
    print("Clustering:", fb_clustering, average_clustering(hk))
    print("Path length:", fb_length, estimate_path_length(hk))
    print("Mean degrees:", np.mean(degrees(fb)), np.mean(degrees(hk)))

if __name__ == "__main__": main()