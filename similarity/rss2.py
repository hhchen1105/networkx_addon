"""
Implement rss2 similarity
"""
#    Copyright (C) 2004-2010 by
#    Hung-Hsuan Chen <hhchen@psu.edu>
#    All rights reserved.
#    BSD license.
#    NetworkX:http://networkx.lanl.gov/.
import networkx as nx
__author__ = """Hung-Hsuan Chen (hhchen@psu.edu)"""
__all__ = ['rss2']

def rss2(G, remove_neighbors=False, dump_process=False, disregard_weight=False):
  """Return the rss2 similarity between nodes

  Parameters
  -----------
  G : graph
    A NetworkX graph
  remove_neighbors: boolean
    if true, only return rss2 similarity of non-neighbor nodes
  dump_process: boolean
    if true, the calculation process is dumped
  disregard_weight: boolean
    if true, the edge weight is ignored

  Returns
  -------
  rss2: dictionary of dictionary of double
    if rss2[i][j] = k, this means the rss2 similarity
    between node i and node j is k

  Examples
  --------
  >>> G=nx.Graph()
  >>> G.add_edges_from([(0,7), (0,1), (0,2), (0,3), (1,4), (2,4), (3,4), (4,5), (4,6)], weight=1)
  >>> networkx_addon.similarity.rss2(G)

  Notes
  -----

  References
  ----------
  """
  if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
    raise Exception("rss2() not defined for graphs with multiedges.")

  if G.is_directed():
    raise Exception("rss2() not defined for directed graphs.")

  weighted_deg = G.degree(weight='weight')
  rss2 = { }
  cur_iter = 0
  total_iter = G.number_of_nodes()
  for a in G.nodes():
    if dump_process:
      cur_iter += 1
      print cur_iter, '/', total_iter
    for b in G.neighbors(a):
      for c in G.neighbors(b):
        if a == c:
          continue
        if remove_neighbors and c in G.neighbors(a):
          continue
        if disregard_weight:
          t1 = float(1)
          t2 = float(1)
          s1 = len(set(G.neighbors(a)))
          s2 = len(set(G.neighbors(b)))
        else:
          t1 = float(G[a][b]['weight'])
          t2 = float(G[b][c]['weight'])
          s1 = weighted_deg[a]
          s2 = weighted_deg[b]
        if a not in rss2:
          rss2[a] = { }
        if c not in rss2[a]:
          rss2[a][c] = t1/s1 * t2/s2
        else:
          rss2[a][c] += t1/s1 * t2/ s2
  return rss2


