# How Attached Are We to Preferential Attachment?

Erica Lee and Emily Yeh

------

### Abstract
Holme and Kim propose an extension of the Barabási-Albert model that yields a higher level of clustering to simulate social networks more accurately, including their observations of how social interactions took place. We explore Holme and Kim's algorithm for directed and undirected graphs using data from Stanford Network Analysis Project (SNAP) and the Python library, NetworkX and investigate the effects of a preferential attachment in networks.

------

We replicate Holme and Kim's work using Facebook network data from SNAP and confirm a higher clustering coefficient and shorter average path lengths between nodes using Holme and Kim's algorithm than using Barabási and Albert's. Holme and Kim generate graphs using the following steps:

1. **Initial condition**: In the beginning, the network consists of _m<sub>0</sub>_ vertices and 0 edges.

2. **Growth**: One vertex _v_ with _m_ edges gets added with every time step. Time _t_ is the number of time steps.

3. **Preferential attachment (PA)**: Each edge of _v_ gets attached to an existing vertex _w_ with a probability proportional to the other vertex's degree.

4. **Triad formation (TF)**, Holme and Kim's modification of the Barabási-Albert model: If an edge was added in the previous PA step, add one more edge from _v_ to a randomly-selected neighbor of _w_. If there remains no other pair to connect (all neighbors of _w_ are already connected to _v_), do another PA step instead.

Figure 1 displays the results of our replication. Our replication results are close to the results from Holme and Kim's experiment. We expect higher values for clustering and mean degrees for our Holme Kim experiment than the results we display under _Holme Kim Expected_ because the results under _Holme Kim Expected_ are results from the Barabási-Albert model, which Holme and Kim change to yield higher clustering and shorter path lengths in their experiment.

### Results of Replication

|              | Facebook | Facebook Expected<sup>2</sup> |
|  ------      |  ------  |  ------                       |
| Degrees      | 4039     | 4039                          |
| Clustering   | 0.588    | 0.61                          |
| Path Length  | 3.689    | 3.69                          |
| Mean Degrees | 43.691   | 43.7                          |

|              | Holme Kim | Holme Kim Expected<sup>2</sup> |
| ---          | ---       | ---                            |
| Degrees      | 4039      | 4039                           |
| Clustering   | 0.082     | > 0.037                        |
| Path Length  | 2.136     | < 2.51                         |
| Mean Degrees | 85.274    | > 43.7                         |

**Figure 1.** Results of replication using Facebook data from SNAP. The results under _Facebook_ and _Holme Kim_ are our results, while the results under _Facebook Expected_ and _Holme Kim Expected_ are results from _Think Complexity_.

We also generate PMF graphs to examine the the degree distribution of the graphs we generate for the Facebook data and the graphs Holme and Kim's experiment generate. As Figure 2 shows, the PMF curve for the Facebook data is less linear than the curve for Holme and Kim's experiment, but both are approximately linear, proving that the distributions of degrees of these graphs obey a power law, indicating that these are scale-free networks. 

![alt text](https://github.com/ericasaywhat/Epidemix/blob/master/reports/PMFGraphs.png "wow so linear")

**Figure 2.** PMF graphs for our Facebook and Holme Kim results. There is noisiness in both graphs and a curved tail for the Facebook results.

We investigate an extension to Holme and Kim's work by making it applicable to directed graphs. Holme and Kim's experiment shows that in undirected graphs, an additional "triad formation" step preserves the same scale-free and power-law degree distribution characteristics as Barabási and Albert's graphs, but with additional high-clustering. However, the "triad formation" step as Holme and Kim describe it only applies to undirected graphs because it requires adding random edges between a source and a random neighboring node. This increases clustering and decreases average path lengths in undirected graphs, where the direction of the edge does not matter, but in directed graphs, a randomly added edge between two nodes does not guarantee that clustering increases nor that path length decreases. For example, when User A follows User B on a social media site like Twitter, but User B never follows User A back, there is a connection from User A to User B but not a connection from User B back to User A.

Our goal is to fix the disparity between Holme and Kim's work for undirected versus directed graphs. After successfully replicating Holme and Kim's experiment, we modify our replication such that it is based on directed graphs. The results of our modification of holme and Kim's experiment are displayed in the following table.The results for the clustering coefficient are similar with a difference of only 0.009, but there are significant differences between the path lengths and mean degrees generated by our modification of Holme and Kim's work when compared to the original work. (As a result, this experiment is still in progress, while we try to find and demolish the errors in our ways.)

### Results of Modification

|              | Twitter | Holme Kim Modified | Holme Kim Expected |
| ---          | ---     | ---                | ---                |
| Degrees      | 81306   | 81306              | 81306              |
| Clustering   | 0.082   | 0.223              | 0.214              |
| Path Length  | 3.889   | 1.997              | 3.676              |
| Mean Degrees | 33.019  | 67.954             | 43.988             |

**Figure 3.** TBE

We also explore the Holme and Kim experiment by generating a clustered scale-free network without preferential attachment.(This experiment is also in progress though.) Within the Holme and Kim experiment, there is a special case in which the average number of triads formed per time step is one and there are two triads as well as two triads in the initial time step. This special case is very similar to the model in which preferential attachment is disregarded.

-----
# References

[1] **Albert-László Barabási and Réka Albert**."Emergence of Scaling in Random Networks" *Science*. 286, 509 (1999).

_Barabási and Albert observe that a common property of many large networks is that the vertex connectivities follow a scale-free power-law distribution. They discover this through the use of graphs; they start with graphs with no edges, i.e., graphs completely composed of random vertices. Then, for every time step,  they add a vertex with several edges, where the edges are connected to other vertices based on the principle of preferential attachment (similar to the "rich get  richer" principle)._

[2] **Downey, Allen**. "Chapter 4: Scale-free Networks" *Think Complexity*. 2nd ed., O'Reilly, 2012, pp.47-65.

_Downey explains complexity science using programming examples in Python, data structures and algorithms, and computational modeling. He also puts his experiments and results under philosophical scrutiny, raising questions that relate to philosophy of science. Chapter 4 of his textbook has to do with scale-free networks; Downey replicates the Barabási-Albert (BA) and Watts-Strogatz (WS) models in the context of Facebook data from SNAP and finds that the WS model is not scale-free, whereas the BA model is._

[3] **Holme, Petter, and Beom Jun Kim** "Growing Scale-Free Networks with Tunable Clustering." *Physical Review* E, vol.65, no.2, Nov. 2002, doi:10.1103/physreve.65.026107.

_Real social networks have higher levels of clustering than Barabási and Albert's model convey. Holme and Kim observe that often times when one person befriends another, that person also becomes friends with a random friend of that friend. As a result, Holme and Kim add an extension to Barabási and Albert's  model that generates triads with a certain probability. With their model, changing the average number of triad formation trials per time step alters the clustering coefficient._
