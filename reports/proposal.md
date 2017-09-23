# ﻿Transmissibility of Language and Obesity
Erica Lee, Emily Yeh

## Abstract
With this project, we will investigate the spread of obesity or other epidemics, as well as the evolution of language. We will use Python 3 and Python’s NetworkX library to generate graphs of networks and analyze them.

## References
Rahul Goel, Sandeep Soni, Naman Goyal, John Paparrizos, Hanna Wallach, Fernando Diaz, and Jacob Eisenstein. “The Social Dynamics of Language Change in Online Networks.” _arXiv:1609.02075 [cs.CL]_
Language is complex and constantly evolving; in an attempt to understand the ways in which language evolves, in this report, researchers use a data set of several million Twitter users to track language changes as they happen in the modern era. These researchers introduce a new concept of phonetic contagion between Twitter users across regions to explain the evolution of new phonetic spellings for words. This concept is tested for the strength of its influence via a parametric Hawkes process model (not too sure what this is, but I think that in this case, it measures self-activation, mutual reply, tie strength, and locality as influences on a given user's inclination to start using a new phonetic spelling of a word). In the end, the researchers conclude that geographic locality plays a rather small role, and this conclusion seems to be supported by the model; the goodnesses of fit for the models compared to their expected results do not appear to be strong enough to support the concept of local phonetic contagion.

Moore, Cristopher, and Mark EJ Newman. "Epidemics and percolation in small-world networks." _Physical Review E 61.5 (2000): 5678._
In this article, Moore and Newman make the claim that since the degrees of separation in a network is small compared to the network itself, disease percolation also is much faster than one would expect. In other words, with Milgram's six degrees of separation, a highly infectious disease would be able to spread to all the people on the planet in just six incubation periods of the disease. They incorporate the two parameters of interest when talking about diseases into their networks: susceptibility and transmissibility. They conclude that their results provide simple models to simulate the onset of epidemic behaviour in diseases for which either susceptibility or transmissibility are less than 100%.

Nicholas A. Christakis, M.D., Ph.D., M.P.H., and James H. Fowler, Ph.D. "The Spread of Obesity in a Large Social Network over 32 Years." _N Engl J Med 2007; 357:370-379._ July 26, 2007.
In this study, these two researchers examined a network of 12067 people over 32 years, predicting that obesity is spread through social connectivity. They use the term "ego" to represent key subjects and "alters" to represent those linked to egos. They graphed the network using the Kamada-Kawai algorithm in Pajek software (not too sure what this is) and examined whether the data conformed to small-world, scale-free, and hierarchical types of network models. The researchers considered three explanations for the clustering of obese people: homophily (egos associate with alters), confounding (egos share attributes or experiences that cause their weight to vary at the same time), and induction (alters exert social influence on egos). The researchers arrived at a number of interesting conclusions that may or may not mean anything, such as that there is a relationship between the obesities of egos and alters up to three degrees of separation. The final conclusion the researchers arrived upon was that obesity spreads in social networks in a quantifiable and discernable pattern that depends on the nature of social ties - as such, the researchers hope that their findings will help slow the spread of obesity, since they have found a possible cause of its spread.

## Experiments
In the experiment that studies obesity, Fowler and Christakis generated the network from Framingham Heart Study using the Kamada-Kawai algorithm and examined the relation between the nodes that were deemed obese. They examine the probabilities of obesity when altering the relationships between nodes to determine the effect geographical distance, sex of the node as well as the sex of their friends. We are considering extending this research by generating PMF curves and investigating data in more recent times to see how these factors became more or less important over the years.

For the experiment that studies language change, by Rahul Goel, Sandeep Soni, Naman Goyal, John Paparrizos, Hanna Wallach, Fernando Diaz, and Jacob Eisenstein, the researchers examined Twitter Tweets across various regions and analyzed how the language used in the Tweets changed over time. We think that some fun extensions of this experiment might include analyzing Twitter follower networks to see if geographic location/environment affects the number of followers a user has, examining how small-world-ish Twitter networks are (do followers cluster? Are there short path lengths between most users? These questions can be answered by generating and analyzing some PMF curves), and taking a look at how language has evolved over time via the popularity of certain words.
Predicted Results
  
         
## Methods of Analysis
For the evolution of language experiment, we will plot the degree distributions of people on Twitter who talk to each other (a mutual-reply network). We will then use some of the algorithms and formulas mentioned in the article to analyze the data we have and find the transmissibility of new words.

We will evaluate our PMF curves to discern how the proportion of people who are obese have friends who are also obese and how that changes over time.

## Causes for Concern
We have a few concerns about this project; the first is that we are not completely sure where to find data for our project, or the data cited by our resources are outdated. However, we’re confident that we can find updated and relevant data for this project.

We are 67.3% sure that we can complete this project by the deadline, but we don’t actually know how long it will take us, so time management and scoping may also be causes for concern for us.

## Next Steps
We will spend our first week finding data for our project and beginning to graph and understand the data. We will probably start with the spread and evolution of language experiment, and see where that takes us.
