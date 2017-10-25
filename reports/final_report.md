# Clustered Scale-Free Networks without Preferential Attachment

Erica Lee and Emily Yeh

------

### Abstract
Holme and Kim propose a model, the HK model, based on Barabási and Albert's, the BA model, that yields a higher level of clustering. We explore Holme and Kim's algorithm using data from the Stanford Network Analysis Project (SNAP)<sup>5</sup> and the Python library NetworkX. We generate networks without preferential attachment and find that the results are still scale-free and highly clustered.

------
### Introduction
What characteristics of simulated networks are present in real-world social networks? Scientists trying to simulate social networks might choose to design their simulated networks to be scale-free so that they are applicable to any social network, regardless of its size. They might also design them to include the clustering behavior that is fundamental to social networks, where clustering is a measure of how connected a subset of nodes is. With the BA model, Barabási and Albert create a scale-free network using preferential attachment, which is when new nodes have a higher probability, or preference, of connecting to other nodes that already have high degrees. The BA model exhibits scale-free behavior, but its clustering coefficient is too low to represent a real-world social network. With the HK model, Holme and Kim introduce triad formation as an additional step to the BA model. This is because they observe that when one person in the real world becomes friends with another, they sometimes also become friends with the friends of the other person, thereby forming triads.

### Replicating Holme and Kim's Experiment

We replicate the HK model using Facebook network data from SNAP and confirm a higher clustering coefficient and shorter average path lengths between nodes using Holme and Kim's algorithm than using Barabási and Albert's.

We first generate the BA model with the following characteristics:

1. **Initial condition**: In the beginning, the network consists of _m_<sub>0</sub> vertices, where _m_ is the average number of triad formation trials per time step, and 0 edges.

2. **Growth**: One vertex _v_ with _m_ edges gets added with every time step. Time _t_ is the number of time steps.

3. **Preferential attachment (PA)**: Each edge of _v_ gets attached to an existing vertex _w_ with a probability proportional to the other vertex's degree.

We then implement the additional step in the HK model:

4. **Triad formation (TF)**: If an edge was added in the previous PA step, add one more edge from _v_ to a randomly-selected neighbor of _w_. If there remains no other pair to connect (all neighbors of _w_ are already connected to _v_), do another PA step instead.

|              | Facebook | Facebook Expected<sup>3</sup> | BA    |
|  ------      |  ------  |  ------                       | ----- |
| Nodes        | 4039     | 4039                          | 4039  |
| Clustering   | 0.613    | 0.61                          | 0.037 |
| Path Length  | 3.696    | 3.69                          | 2.51  |
| Mean Degrees | 43.691   | 43.7                          | 43.7  |

**Figure 1-1.** *Results we generate using data from SNAP. The results under "Facebook" are our results, while the results under "Facebook Expected" and "BA" are results from* Think Complexity.

|              | HK        | HK Expected<sup>3</sup> |
| ---          | ---       | ---                     |
| Nodes        | 4039      | 4039                    |
| Clustering   | 0.256     | > 0.037                 |
| Path Length  | 2.746     | 2.51                    |
| Mean Degrees | 43.754    | 43.7                    |

**Figure 1-2.** *Results we generate using data from SNAP. The results under "HK" are our results, while the results under "HK Expected" are what we expect for the HK model based on Downey's replication of the BA model in* Think Complexity, *which also makes use of the Facebook dataset from SNAP.*

Figure 1 displays our implementation result. We confirm that our results under "Facebook" in Figure 1-1 are relatively close to the results we expect - the largest margin of error is 0.009. We also confirm a higher clustering value for our implementation of the HK model than for "HK Expected" in Figure 1-2, where the values for "HK Expected" are derived from our expectation that the HK model should have a higher clustering coefficient than that of the BA model.

We also generate probability mass functions (PMFs) to examine the degree distributions of the Facebook data and our HK model. As Figure 2 shows, the PMF for the Facebook data is less linear than the PMF for our HK model, but both are approximately linear, as the dashed lines show, suggesting that the distributions of degrees of these graphs obey a power law and that these are scale-free networks.

![figure 2 PMF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/PMFGraphs_Original.png)

**Figure 2.** *PMFs for our Facebook and HK model results. For higher values, there is more noise in both graphs. There are some outliers for lower degrees in the PMF of the HK graph.*

To get a clearer idea of how reasonable our results are, we generate cumulative distribution functions (CDFs), which are less noisy than PMFs and show the shape of the distribution more clearly.<sup>3</sup> Figure 3 shows the CDF of the results of our implementation of the HK model overlaid on the CDF of the Facebook dataset. Both CDFs are similar in shape and distribution of degrees.

![figure 3 CDF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/CDFGraphs_Original.png)

**Figure 3.** *CDFs for our Facebook and HK model results. The graphs seem to align for higher values.*

As Figure 3 shows, the CDF for our replication of the HK model is clearly different from the CDF for the Facebook dataset, especially for lower degree values. However, for higher values, the two curves become more aligned, although how much more is difficult to tell. To determine how well the CDF graphs align for higher values, we generate complementary cumulative distribution functions (CCDFs). CCDF graphs are useful because if a distribution really obeys a power law, the CCDF will be a straight line on a log-log scale.

![figure 4 CCDF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/CCDFGraphs_Original.png)

**Figure 4.** *CCDFs for our Facebook and HK results.*

Figure 4 shows that the CCDF of our HK model replication almost aligns with the CCDF of the Facebook dataset. The CCDF of the HK model is also almost a straight line, meaning the distribution obeys a power law. This indicates that the HK model we generate does exhibit scale-free behavior. In combination with our results from Figure 1-2 (which show that our HK model has a high clustering coefficient), our HK model can be characterized as scale-free and highly clustered, both of which are key features of the original HK model.



### Removing Preferential Attachment
In their experiment, Barabási and Albert find that they must include all three of their conditions - the initial condition, growth, and preferential attachment - in order to  generate scale-free networks successfully. If any of the conditions are removed, their model is no longer scale-free.<sup>1</sup> Like Barabási and Albert, we remove conditions from the HK model and find that scale-free, clustered networks can still be generated without preferential attachment.

In order to produce scale-free, clustered networks without preferential attachment, we extend Holme and Kim's triad formation step. In Holme and Kim's experiment, there is a special case in which the average number of triads formed per time step is 1, and there is an average of 2 triads per node as well as 2 triads in the initial time step. This special case is similar to a model in which random triads are generated for each time step.<sup>4</sup>

We therefore modify and optimize the HK model procedure by removing the PA step and modifying the TF step:

1. **Initial condition**: In the beginning, the network consists of one triad - 3 vertices that are all connected to each other, so each vertex has a degree of 2.

2. **Growth**: One vertex _v_ gets added with every time step. Time _t_ is the number of time steps.

3. **Random triad formation**: Select one random existing edge _m_ and connect _v_ to both vertices of _m_.

We then generate a network with this "removed preferential attachment" procedure, which we will refer to as the RPA model. Our RPA model is the same size as our HK model to make comparing the results of the two easier, as shown in Figure 5.

|              | RPA      | HK        |
|  ------      | ------   | ------    |
| Nodes        | 4039     | 4039      |
| Clustering   | 0.751    | 0.256     |
| Path Length  | 5.698    | 2.746     |
| Mean Degrees | 3.999    | 43.754    |

**Figure 5.** *The results under "RPA" are the results from our RPA model and the results under "HK" are the results from our HK model.*

As Figure 5 shows, our RPA model demonstrates higher clustering than our HK model. Since this model has the high clustering property, the other property we test for is scale-free behavior. We do so by generating PMFs for our RPA model and Facebook dataset results.

![figure 6 PMF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/PMFGraphs_Modified.png)

**Figure 6.** *PMFs for the results of our RPA model and the Facebook dataset.*

Based on the PMF's linearity in Figure 6, the RPA procedure generates a scale-free network. We then generate a CDF to get a clearer picture of our distribution.

![figure 7 CDF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/CDFGraphs_Modified.png)

**Figure 7.** *CDFs for the results of our RPA model and the Facebook dataset.*

As Figure 7 shows, there is a large disparity between the two CDFs, though their shapes are similar. Based on these CDFs, it is possible that for larger degrees, the graphs overlap. As a final step, we generate CCDF graphs to get a closer look at the similarities between the distributions.

![figure 8 CCDF graphs](https://github.com/ericasaywhat/Epidemix/blob/master/reports/CCDFGraphs_Modified.png)

**Figure 8.** *CCDFs for the results of our RPA model and the Facebook dataset.*

The CCDFs still show a disparity between the two graphs. However, the CCDF of our RPA model is linear, indicating that our RPA model is a scale-free network, even without preferential attachment. In combination with our findings as shown in Figure 5, we conclude that our RPA model is a clustered and scale-free network. Therefore, while the PA step is important for the BA model to generate a scale-free network, it is not necessary for the HK model to generate a clustered and scale-free network, since the introduction of the TF step is sufficient to generate these behaviors.

In conclusion, we confirm Holme and Kim's proposal that introducing the TF step to the BA model method yields a network with higher clustering, similar to that of a real network, like Facebook. However, we find that scale-free and clustered networks can still be generated without the PA step, as utilizing a modified version of the TF step is sufficient to generate these behaviors.

We observe that the clustering of our RPA model is higher than that of the Facebook dataset, indicating that our RPA model is more clustered than a true Facebook network. The Facebook dataset we use, however, only contains data for a network of 4039 users, so this indication might not be completely accurate.

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
