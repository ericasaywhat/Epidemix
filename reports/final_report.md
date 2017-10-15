# How Attached Are We to Preferential Attachment?

Erica Lee and Emily Yeh

------

### Abstract
Holme and Kim propose an extension of the Barabási-Albert model that yields a higher level of clustering to simulate social networks more accurately, including their observations of how social interactions took place. We explore Holme and Kim's algorithm from Stanford Network Analysis Project (SNAP) and the Python library, NetworkX and investigate the effects of a preferential attachment in networks.

------

We replicate Holme and Kim's work using Facebook network data from SNAP and confirm a higher clustering coefficient and shorter average path lengths between nodes using Holme and Kim's algorithm than using Barabási and Albert's. Holme and Kim generate graphs using the following steps:

1. **Initial condition**: In the beginning, the network consists of _m<sub>0</sub>_ vertices and 0 edges.

2. **Growth**: One vertex _v_ with _m_ edges gets added with every time step. Time _t_ is the number of time steps.

3. **Preferential attachment (PA)**: Each edge of _v_ gets attached to an existing vertex _w_ with a probability proportional to the other vertex's degree.

4. **Triad formation (TF)**, Holme and Kim's modification of the Barabási-Albert model: If an edge was added in the previous PA step, add one more edge from _v_ to a randomly-selected neighbor of _w_. If there remains no other pair to connect (all neighbors of _w_ are already connected to _v_), do another PA step instead.

### Results of Replication

|              | Facebook | Facebook Expected<sup>3/sup> |
|  ------      |  ------  |  ------                       |
| Degrees      | 4039     | 4039                          |
| Clustering   | 0.588    | 0.61                          |
| Path Length  | 3.689    | 3.69                          |
| Mean Degrees | 43.691   | 43.7                          |

|              | Holme Kim | Holme Kim Expected<sup>3</sup> |
| ---          | ---       | ---                            |
| Degrees      | 4039      | 4039                           |
| Clustering   | 0.082     | > 0.037                        |
| Path Length  | 2.136     | < 2.51                         |
| Mean Degrees | 85.274    | > 43.7                         |

**Figure 1.** Results of replication using Facebook data from SNAP. The results under _Facebook_ and _Holme Kim_ are our results, while the results under _Facebook Expected_ and _Holme Kim Expected_ are results from _Think Complexity_.

Figure 1 displays the results of our replication. Our replication results are close to the results from Holme and Kim's experiment. We expect higher values for clustering and mean degrees for our Holme Kim experiment than the results we display under _Holme Kim Expected_ because the results under _Holme Kim Expected_ are results from the Barabási-Albert model, which Holme and Kim change to yield higher clustering and shorter path lengths in their experiment.

We also generate PMF graphs to examine the the degree distribution of the graphs we generate for the Facebook data and the graphs Holme and Kim's experiment generate. As Figure 2 shows, the PMF curve for the Facebook data is less linear than the curve for Holme and Kim's experiment, but both are approximately linear, proving that the distributions of degrees of these graphs obey a power law, indicating that these are scale-free networks. 

![alt text](https://github.com/ericasaywhat/Epidemix/blob/master/reports/PMFGraphs.png)

**Figure 2.** PMF graphs for our Facebook and Holme Kim results. There is noisiness in both graphs and a curved tail for the Facebook results.

**ANALYZE PMF GRAPHS HERE**


**Figure 3.** TBE

We explore the Holme and Kim experiment by generating a clustered scale-free network without preferential attachment. Within the Holme and Kim experiment, there is a special case in which the average number of triads formed per time step is one and there are two triads as well as two triads in the initial time step. This special case is supposedly very similar to the model in which preferential attachment is disregarded <sup>2</sup>.

-----
# References

[1] **Albert-László Barabási and Réka Albert**. "Emergence of Scaling in Random Networks." *Science*. 286, 509 (1999).

_Barabási and Albert observe that a common property of many large networks is that the vertex connectivities follow a scale-free power-law distribution. They discover this through the use of graphs; they start with graphs with no edges, i.e., graphs completely composed of random vertices. Then, for every time step,  they add a vertex with several edges, where the edges are connected to other vertices based on the principle of preferential attachment (similar to the "rich get  richer" principle)._

[2] **Dorogovtsev, S. N., Mendes, J. F. F., and Samukhin, A. N.** "Size-dependent degree distribution of a scale-free growing network." _Physical Review_, E, Statistical Physics, Plasmas, Fluids, and Related Interdisciplinary Topics.

_Dorogovtsev et al. explore the effects of replacing the preferential attachment step of generating scale-free networks with purely random selection of vertices. Their process involves generating the simplest model of a scale-free network: starting with three nodes initially, each with connectivity 2, for each time step thereafter, they add another node that is connected to both ends of a randomly chosen link by two undirected links. The preferential linking arises not because of a special rule, as Barabasi-Albert proposed, but completely naturally. They find that the probability of a node being attached to a randomly chosen link is almost the same as the equation Barabasi and Albert came up with - the connectivity k of the node divided by the total number of links, 2t - 1._

[3] **Downey, Allen**. "Chapter 4: Scale-free Networks" *Think Complexity*. 2nd ed., O'Reilly, 2012, pp.47-65.

_Downey explains complexity science using programming examples in Python, data structures and algorithms, and computational modeling. He also puts his experiments and results under philosophical scrutiny, raising questions that relate to philosophy of science. Chapter 4 of his textbook has to do with scale-free networks; Downey replicates the Barabási-Albert (BA) and Watts-Strogatz (WS) models in the context of Facebook data from SNAP and finds that the WS model is not scale-free, whereas the BA model is._

[3] **Holme, Petter, and Beom Jun Kim** "Growing Scale-Free Networks with Tunable Clustering." *Physical Review* E, vol.65, no.2, Nov. 2002, doi:10.1103/physreve.65.026107.

_Real social networks have higher levels of clustering than Barabási and Albert's model convey. Holme and Kim observe that often times when one person befriends another, that person also becomes friends with a random friend of that friend. As a result, Holme and Kim add an extension to Barabási and Albert's  model that generates triads with a certain probability. With their model, changing the average number of triad formation trials per time step alters the clustering coefficient._
