"""
Implement linear threshold models
"""
#!/usr/bin/env python
#    Copyright (C) 2004-2010 by
#    Hung-Hsuan Chen <hhchen@psu.edu>
#    All rights reserved.
#    BSD license.
#    NetworkX:http://networkx.lanl.gov/.
__author__ = """Hung-Hsuan Chen (hhchen@psu.edu)"""

import copy
import networkx as nx

__all__ = ['linear_threshold']

def linear_threshold(G, seeds, steps=0):
  """Return the active nodes of each diffusion step by linear threshold model

  Parameters
  ----------
  G : networkx graph
      The number of nodes.

  seeds: list of nodes
      The seed nodes of the graph

  steps: int
      The number of steps to diffuse
      When steps <= 0, the model diffuses until no more nodes
      can be activated

  Return
  ------
  layer_i_nodes : list of list of activated nodes
    layer_i_nodes[0]: the seeds
    layer_i_nodes[k]: the nodes activated at the kth diffusion step

  Notes
  -----
  1. Each node is supposed to have an attribute "threshold".  If not, the
     default value is given (0.5).
  2. Each edge is supposed to have an attribute "influence".  If not, the
     default value is given (1/in_degree)

  References
  ----------
  [1] GranovetterMark. Threshold models of collective behavior.
      The American journal of sociology, 1978.

  Examples
  --------
  >>> DG = nx.DiGraph()
  >>> DG.add_edges_from([(1,2), (1,3), (1,5), (2,1), (3,2), (4,2), (4,3), \
  >>>   (4,6), (5,3), (5,4), (5,6), (6,4), (6,5)])
  >>> layers = networkx_addon.information_propagation.linear_threshold(DG, [1])

  """
  if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
      raise Exception( \
          "linear_threshold() is not defined for graphs with multiedges.")

  # make sure the seeds are in the graph
  for s in seeds:
    if s not in G.nodes():
      raise Exception("seed", s, "is not in graph")

  # change to directed graph
  if not G.is_directed():
    DG = G.to_directed()
  else:
    DG = copy.deepcopy(G)

  # init thresholds
  for n in DG.nodes():
    if 'threshold' not in DG.node[n]:
      DG.node[n]['threshold'] = 0.5
    elif DG.node[n]['threshold'] > 1:
      raise Exception("node threshold:", DG.node[n]['threshold'], \
          "cannot be larger than 1")

  # init influences
  in_deg = DG.in_degree()
  for e in DG.edges():
    if 'influence' not in DG[e[0]][e[1]]:
      DG[e[0]][e[1]]['influence'] = 1.0 / in_deg[e[1]]
    elif DG[e[0]][e[1]]['influence'] > 1:
      raise Exception("edge influence:", DG[e[0]][e[1]]['influence'], \
          "cannot be larger than 1")

  # perform diffusion
  A = copy.deepcopy(seeds)
  if steps <= 0:
    # perform diffusion until no more nodes can be activated
    return _diffuse_all(DG, A)
  # perform diffusion for at most "steps" rounds only
  return _diffuse_k_rounds(DG, A, steps)

def _diffuse_all(G, A):
  layer_i_nodes = [ ]
  layer_i_nodes.append([i for i in A])
  while True:
    len_old = len(A)
    A, activated_nodes_of_this_round = _diffuse_one_round(G, A)
    layer_i_nodes.append(activated_nodes_of_this_round)
    if len(A) == len_old:
      break
  return layer_i_nodes

def _diffuse_k_rounds(G, A, steps):
  layer_i_nodes = [ ]
  layer_i_nodes.append([i for i in A])
  while steps > 0 and len(A) < len(G):
    len_old = len(A)
    A, activated_nodes_of_this_round = _diffuse_one_round(G, A)
    layer_i_nodes.append(activated_nodes_of_this_round)
    if len(A) == len_old:
      break
    steps -= 1
  return layer_i_nodes

def _diffuse_one_round(G, A):
  activated_nodes_of_this_round = set()
  for s in A:
    nbs = G.successors(s)
    for nb in nbs:
      if nb in A:
        continue
      active_nb = list(set(G.predecessors(nb)).intersection(set(A)))
      if _influence_sum(G, active_nb, nb) >= G.node[nb]['threshold']:
        activated_nodes_of_this_round.add(nb)
  A.extend(list(activated_nodes_of_this_round))
  return A, list(activated_nodes_of_this_round)

def _influence_sum(G, froms, to):
  influence_sum = 0.0
  for f in froms:
    influence_sum += G[f][to]['influence']
  return influence_sum


