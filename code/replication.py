import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import thinkplot
from thinkstats2 import Cdf, Pmf
from scipy.stats import linregress
from networkx.algorithms.approximation import average_clustering

print("Initializing...")

def degrees(G):
    """List of degrees for nodes in `G`.

    G: Graph object

    returns: list of int
    """
    return [G.degree(u) for u in G]

def ba_graph(n, k, seed=None):
    """Constructs a BA graph.

    n: number of nodes
    k: number of edges for each new node
    seed: random seen
    """
    if seed is not None:
        random.seed(seed)

    G = nx.empty_graph(k)
    targets = list(range(k))
    repeated_nodes = []

    for source in range(k, n):
        G.add_edges_from(zip([source]*k, targets))

        repeated_nodes.extend(targets)
        repeated_nodes.extend([source] * k)

        targets = _random_subset(repeated_nodes, k)
    return G

def hk_graph(n, m, p, seed=None):
    """Constructs a Holme-Kim graph.

    n: number of nodes
    m: 
    p: probability of PA of edge to a given node
    m: number of edges for each new node
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

    G = nx.empty_graph(m)
    repeated_nodes = list(G.nodes())
    source = m
    for source in range(m,n):
        possible_targets = _random_subset(repeated_nodes, m)
        target = possible_targets.pop()
        G.add_edge(source, target)
        repeated_nodes.append(target)
        count = 1
        for count in range(1,m):
            if random.random() < p:
                neighborhood = [nbr for nbr in G.neighbors(target)
                                if not G.has_edge(source, nbr)
                                and not nbr == source]
                if neighborhood:
                    nbr = random.choice(neighborhood)
                    G.add_edge(source, nbr)
                    repeated_nodes.append(nbr)
                    count = count + 1
                    continue
            target = possible_targets.pop()
            G.add_edge(source, target)
            repeated_nodes.append(target)

        repeated_nodes.extend([source] * m)
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

    thinkplot.preplot(cols=2)

    thinkplot.plot([30, 2000], [5e-2, 2e-4], color='gray', linestyle='dashed')

    thinkplot.Pdf(pmf_fb, style='.', label='Facebook')
    thinkplot.config(xscale='log', yscale='log',
      xlabel='degree', ylabel='PMF')

    thinkplot.subplot(2)

    thinkplot.plot([55, 500], [5e-2, 2e-4], color='gray', linestyle='dashed')

    thinkplot.Pdf(pmf_hk, style='.', label='HK graph')
    thinkplot.config(xscale='log', yscale='log',
      xlabel='degree', ylabel='PMF')

    plt.savefig('PMFGraphs_Original.png')

def generate_cdf(fb, hk):
    cdf_fb = Cdf(degrees(fb))
    cdf_hk = Cdf(degrees(hk))

    thinkplot.Cdf(cdf_fb, color='gray', label="Facebook CDF")
    thinkplot.Cdf(cdf_hk, label='HK CDF')
    thinkplot.config(xlabel='degree', xscale='log',
                 ylabel='CDF')

    plt.savefig('CDFGraphs_Original.png')

def generate_ccdf(fb, hk):
    cdf_fb = Cdf(degrees(fb))
    cdf_hk = Cdf(degrees(hk))

    thinkplot.Cdf(cdf_fb, label='Facebook CCDF', color='gray', complement=True)
    thinkplot.Cdf(cdf_hk, label="HK CCDF", complement=True)
    thinkplot.config(xlabel='degree', xscale='log',
                 ylabel='CCDF', yscale='log')

    plt.savefig("CCDFGraphs_Original.pdf")

def main():
    fb = read_graph('facebook_combined.txt.gz')
    fb_clustering = average_clustering(fb)
    fb_length = estimate_path_length(fb)

    n = len(fb)
    m = len(fb.edges())
    k = int(round(m/n))

    hk = hk_graph(n, k, 1)

    # generate_pmf(fb, hk)
    # generate_cdf(fb, hk)
    # generate_ccdf(fb, hk)

    print("Degrees:", len(degrees(fb)), len(degrees(hk)))
    print("Clustering:", fb_clustering, average_clustering(hk))
    print("Path length:", fb_length, estimate_path_length(hk))
    print("Mean degrees:", np.mean(degrees(fb)), np.mean(degrees(hk)))

if __name__ == "__main__": main()