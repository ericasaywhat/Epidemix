# Detaching Preferential Attachment

Erica Lee and Emily Yeh

------

### Abstract
Holme and Kim propose a model based on Barabási and Albert's that yields a higher level of clustering and simulates the dynamics of social networks more accurately. We explore Holme and Kim's algorithm using data from Stanford Network Analysis Project (SNAP)<sup>5</sup> and the Python library NetworkX. The world consists of scale-free networks beyond social networks with preferential attachment, such as the process of establishing towns. When new towns are built, each new town needs to be accessible by at least two other towns without preference to the sizes or connectedness of the towns. To simulate the establishment of these towns, we generate networks without preferential attachment and find that the results are still scale-free and highly clustered.

------

### Replicating Holme and Kim's Experiment

We replicate Holme and Kim's experiment using Facebook network data from SNAP and confirm a higher clustering coefficient and shorter average path lengths between nodes using Holme and Kim's algorithm than using Barabási and Albert's. We replicate Holme-Kim's method:

1. **Initial condition**: In the beginning, the network consists of _m<sub>0</sub>_ vertices, where m is the average number of triad formation trials per time step, and 0 edges.

2. **Growth**: One vertex _v_ with _m_ edges gets added with every time step. Time _t_ is the number of time steps.

3. **Preferential attachment (PA)**: Each edge of _v_ gets attached to an existing vertex _w_ with a probability proportional to the other vertex's degree.

4. **Triad formation (TF)**, Holme and Kim's modification of the Barabási-Albert model: If an edge was added in the previous PA step, add one more edge from _v_ to a randomly-selected neighbor of _w_. If there remains no other pair to connect (all neighbors of _w_ are already connected to _v_), do another PA step instead.

### Replication Results

|              | Facebook | Facebook Expected<sup>3</sup> | Barabási-Albert |
|  ------      |  ------  |  ------                       | -----           |
| Nodes        | 4039     | 4039                          | 4039            |
| Clustering   | 0.613    | 0.61                          | 0.037           |
| Path Length  | 3.696    | 3.69                          | 2.51            |
| Mean Degrees | 43.691   | 43.7                          | 43.7            |

**Figure 1-1.** Results of replication using Facebook data from SNAP. The results under _Facebook_ are our results, while the results under _Facebook Expected_ and _Barabási-Albert_ are results from _Think Complexity_<sup>(2)</sup>.

|              | Holme-Kim | Holme-Kim Expected<sup>3</sup> |
| ---          | ---       | ---                            |
| Nodes        | 4039      | 4039                           |
| Clustering   | 0.256     | > 0.037                        |
| Path Length  | 2.746     | 2.51                           |
| Mean Degrees | 43.754    | 43.7                           |

**Figure 1-2.** Figure 1-2. Results of replication using Facebook data from SNAP. The results under _Holme-Kim_ are our results, while the results under _Holme-Kim Expected_ are what we expect for the Holme-Kim model based on _Think Complexity's_<sup>(2)</sup> results of the Barabási-Albert model of SNAP's Facebook dataset. The Holme-Kim model should have a higher clustering value than the Barabási-Albert model.

Figure 1 displays the results of our replication. Our replication results are close to the results from Holme and Kim's experiment. We expect and confirm a higher value for clustering for our Holme-Kim experiment than for the results under _Holme Kim Expected_ because the results under _Holme Kim Expected_ are results from the Barabási-Albert model, which Holme and Kim change to yield higher clustering.

We also generate probability mass function (PMF) graphs to examine the the degree distribution of the graphs we generate for the Facebook data and the graphs Holme and Kim's experiment generate. As Figure 2 shows, the PMF curve for the Facebook data is less linear than the curve for Holme and Kim's experiment, but both are approximately linear, as the dashed lines show, proving that the distributions of degrees of these graphs obey a power law and indicating that these are scale-free networks.

![figure 2 PMF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/PMFGraphs_Original.png)

**Figure 2.** PMF graphs for our Facebook and Holme Kim results. For higher values, there is more noise in both graphs and a curved tail for the Facebook results.

To get a clearer idea of how accurate our results are, we generate cumulative distribution function (CDF) graphs, which are less noisy than PMF graphs and can provide a clearer picture of the shape of a distribution.<sup>3</sup> Figure 3 shows the CDF of the results from our replication of Holme and Kim's experiment overlaid on the degree CDF for the Facebook dataset.

![figure 3 CDF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/CDFGraphs_Original.png)

**Figure 3.** CDF graphs for our Facebook and Holme Kim results. The graphs almost align for higher values, but it is difficult to tell how close they really are.

As Figure 3 shows, the CDF for the Holme-Kim replication is clearly different from the CDF for the Facebook dataset, especially for lower degree values, but for higher values, the two curves become more aligned - although how much more is difficult to tell. To determine just how well the CDF graphs align for higher values, we finally generate complementary cumulative distribution function (CCDF) graphs. CCDF graphs are useful because if a distribution really obeys a power law, the CCDF will be a straight line on a log-log scale.

![figure 4 CCDF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/CCDFGraphs_Original.png)

**Figure 4.** CCDF graphs for our Facebook and Holme Kim results. The Facebook CCDF is not linear, while the Holme-Kim CCDF is linear enough; the two graphs also align much more clearly.

Figure 4 shows that the CCDF graph of our Holme-Kim replication matches the CCDF graph of the Facebook dataset well. The CCDF of the Holme-Kim replication is also almost a straight line, meaning the distribution obeys a power law, which is a characteristic of scale-free networks.

### Detaching Preferential Attachment

We extend Holme and Kim's "triad formation" to generating a clustered scale-free network without preferential attachment. In Holme and Kim's experiment, there is a special case in which the average number of triads formed per time step is 1, and there is an average of 2 triads per node as well as 2 triads in the initial time step. This special case is similar to a model in which preferential attachment is disregarded.<sup>4</sup> We modify and optimize the procedure to:

1. **Initial condition**: In the beginning, the network consists of 3 vertices that are all connected to each other, so each vertex has a degree of 2.

2. **Growth**: One vertex _v_ gets added with every time step. Time _t_ is the number of time steps.

3. **Random edge selection**: Select a random existing edge and connect _v_ to both vertices of the edge.

We generate a network of the same size as our Holme-Kim replication, as shown in Figure 5.

### Modification Results

|              | Modified | Holme-Kim |
|  ------      | ------   | ------    |
| Nodes        | 4039     | 4039      |
| Clustering   | 0.751    | 0.256     |
| Path Length  | 5.698    | 2.746     |
| Mean Degrees | 3.999    | 43.754    |

**Figure 5.** Results of our modification. The results under _Modified_ are the results we generate without preferential attachment and the results under _Holme-Kim_ are the results from our replication, which are reproduced here to make comparing the values easier.

As Figure 5 shows, the results of our experiment shows higher clustering than our replication.

![figure 6 PMF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/PMFGraphs_Modified.png)

**Figure 6.** PMF graphs for our Facebook and Holme Kim results.

From the PMF graph's linearity shown in Figure 6, our neighborhood network is a scale-free network. We then generate a CDF graph to get a clearer picture of our distribution.

![figure 7 CDF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/CDFGraphs_Modified.png)

**Figure 7.** CDF graphs for our Facebook and Holme Kim results.

The two graphs do not align well, as Figure 7 shows, although it is possible that for larger values, the graphs do align. As a last step, we generate CCDF graphs to get a final look at the similarity of the distributions.

![figure 8 CCDF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/CCDFGraphs_Modified.png)

**Figure 8.** CCDF graphs for our Facebook and Holme Kim results.

The two graphs do not align at all in the CCDF graphs in Figure 8. However, the CCDF of our modified Holme-Kim graph is reasonably linear, indicating that we did successfully generate a scale-free network without preferential attachment. While the PA step is important for the Barabási-Albert model to simulate social networks, and both the PA and TF steps are important for the Holme-Kim model to simulate a more realistic social network, the PA step is not necessary in generating scale-free networks in which existing paths don't matter.

In conclusion, we implement and confirm Holme and Kim's proposal that including triad formations on the Barabási-Albert method of generating networks yields a network with clustering coefficients closer to those of real networks, like Facebook. However, we also find that scale-free networks can still be generated for networks in which preferential attachment does not exist, such as our town establishment model. In removing preferential attachment, we find that our town model is still scale-free.

The clustering of our town model is higher than that of the Holme-Kim model, indicating that the network of towns we generate is more clustered than a Facebook network. This Facebook data, however, only contains data for 4039 users. Therefore, this indication may not be wholly accurate.

-----

# References

[1] **Albert-László Barabási and Réka Albert**. "Emergence of Scaling in Random Networks." *Science*. 286, 509 (1999).

_Barabási and Albert observe that a common property of many large networks is that the vertex connectivities follow a scale-free power-law distribution. They discover this through the use of graphs; they start with graphs with no edges, i.e., graphs completely composed of random vertices. Then, for every time step,  they add a vertex with several edges, where the edges are connected to other vertices based on the principle of preferential attachment (similar to the "rich get  richer" principle)._

[2] **Dorogovtsev, S. N., Mendes, J. F. F., and Samukhin, A. N.** "Size-dependent degree distribution of a scale-free growing network." _Physical Review_, E, Statistical Physics, Plasmas, Fluids, and Related Interdisciplinary Topics.

_Dorogovtsev et al. explore the effects of replacing the preferential attachment step of generating scale-free networks with purely random selection of vertices. Their process involves generating the simplest model of a scale-free network: starting with three nodes initially, each with connectivity 2, for each time step thereafter, they add another node that is connected to both ends of a randomly chosen link by two undirected links. The preferential linking arises not because of a special rule, as Barabási-Albert proposed, but completely naturally. They find that the probability of a node being attached to a randomly chosen link is almost the same as the equation Barabási and Albert came up with - the connectivity k of the node divided by the total number of links, 2t - 1._

[3] **Downey, Allen**. "Chapter 4: Scale-free Networks" *Think Complexity*. 2nd ed., O'Reilly, 2012, pp.47-65.

_Downey explains complexity science using programming examples in Python, data structures and algorithms, and computational modeling. He also puts his experiments and results under philosophical scrutiny, raising questions that relate to philosophy of science. Chapter 4 of his textbook has to do with scale-free networks; Downey replicates the Barabási-Albert (BA) and Watts-Strogatz (WS) models in the context of Facebook data from SNAP and finds that the WS model is not scale-free, whereas the BA model is._

[4] **Holme, Petter and Beom Jun Kim** "Growing Scale-Free Networks with Tunable Clustering." *Physical Review* E, vol.65, no.2, Nov. 2002, doi:10.1103/physreve.65.026107.

_Real social networks have higher levels of clustering than Barabási and Albert's model convey. Holme and Kim observe that often times when one person befriends another, that person also becomes friends with a random friend of that friend. As a result, Holme and Kim add an extension to Barabási and Albert's  model that generates triads with a certain probability. With their model, changing the average number of triad formation trials per time step alters the clustering coefficient._

[5] **Leskovec, Jure and Krevl, Andrej.** "SNAP Datasets: Stanford Large Network Dataset Collection." _http://snap.stanford.edu/data_, June 2014.

_A collection of datasets, tools, and libraries. The datasets are mined from various websites._
