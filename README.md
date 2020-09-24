networkx_addon
==============

***CAUTION***
This project was developed in 2013, when Python 2.x and networkx 1.x were still popular.

If you want to use this library on later Python (e.g., Python 3.x) and later networkx (e.g., networkx 2.x), you'll need to modify the code.

### Some add-on modules to networkx library

1. Information propagation models
  (1) independent cascade model
  (2) linear threshold model

2. Vertex similarity measures
  (1) ASCOS (for both weighted and unweighted network)
  (2) Jaccard
  (3) Cosine
  (4) SimRank
  (5) RSS (r=2)
  (6) Katz
  (7) LHN

### Dependent packages
* numpy
* scipy
* networkx

### How to use it
Put the "networkx_addon/" folder inside your source directory

### Sample usage

1. network propagation

```Python
>>> import networkx
>>> import networkx_addon
>>> G = networkx.DiGraph()
>>> G.add_edge(1,2,act_prob=.5)
>>> G.add_edge(2,1,act_prob=.5)
>>> G.add_edge(1,3,act_prob=.2)
>>> G.add_edge(3,1,act_prob=.2)
>>> G.add_edge(2,3,act_prob=.3)
>>> networkx_addon.information_propagation.independent_cascade(G, [1], steps=2)
```

2. network similarity

```Python
>>> import networkx
>>> import networkx_addon
>>> G = networkx.Graph()
>>> G.add_edges_from([(0,1),(1,2),(0,2)])
```
