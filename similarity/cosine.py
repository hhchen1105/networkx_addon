"""
Implement cosine similarity
"""
#    Copyright (C) 2004-2010 by
#    Hung-Hsuan Chen <hhchen@psu.edu>
#    All rights reserved.
#    BSD license.
#    NetworkX:http://networkx.lanl.gov/.
import networkx as nx
__author__ = """Hung-Hsuan Chen (hhchen@psu.edu)"""
__all__ = ['cosine']

def cosine(G, remove_neighbors=False, dump_process=False):
  """Return the cosine similarity between nodes

  Parameters
  -----------
  G : graph
    A NetworkX graph
  remove_neighbors: boolean
    if true, only return cosine similarity of non-neighbor nodes
  dump_process: boolean
    if true, the calculation process is dumped

  Returns
  -------
  cosine: dictionary of dictionary of double
    if cosine[i][j] = k, this means the cosine similarity
    between node i and node j is k

  Examples
  --------
  >>> G=nx.Graph()
  >>> G.add_edges_from([(0,7), (0,1), (0,2), (0,3), (1,4), (2,4), (3,4), (4,5), (4,6)])
  >>> networkx_addon.similarity.cosine(G)

  Notes
  -----

  References
  ----------
  """
  if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
    raise Exception("cosine() not defined for graphs with multiedges.")

  if G.is_directed():
    raise Exception("cosine() not defined for directed graphs.")

  cos = { }
  total_iter = G.number_of_nodes()
  for i, a in enumerate(G.nodes()):
    if dump_process:
      print i+1, '/', total_iter
    for b in G.neighbors(a):
      for c in G.neighbors(b):
        if a == c:
          continue
        if remove_neighbors and c in G.neighbors(a):
          continue
        s1 = set(G.neighbors(a))
        s2 = set(G.neighbors(c))
        if a not in cos:
          cos[a] = { }
        cos[a][c] = float(len(s1 & s2)) / (len(s1) + len(s2))

  return cos



