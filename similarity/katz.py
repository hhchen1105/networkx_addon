"""
Implement katz similarity
"""
#    Copyright (C) 2004-2010 by
#    Hung-Hsuan Chen <hhchen@psu.edu>
#    All rights reserved.
#    BSD license.
#    NetworkX:http://networkx.lanl.gov/.
import networkx as nx
import numpy

__author__ = """Hung-Hsuan Chen (hhchen@psu.edu)"""
__all__ = ['katz']

def katz(G, c=0.9, remove_neighbors=True, dump_process=False):
  """Return the katz similarity between nodes

  Parameters
  -----------
  G : graph
    A NetworkX graph
  remove_neighbors: boolean
    if true, only return katz similarity of non-neighbor nodes
  dump_process: boolean
    if true, the calculation process is dumped

  Returns
  -------
  katz: matrix of similarity

  Examples
  --------
  >>> G=nx.Graph()
  >>> G.add_edges_from([(0,7), (0,1), (0,2), (0,3), (1,4), (2,4), (3,4), (4,5), (4,6)])
  >>> nx.katz(G)

  Notes
  -----

  References
  ----------
  """
  if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
    raise Exception("katz() not defined for graphs with multiedges.")

  if G.is_directed():
    raise Exception("katz() not defined for directed graphs.")

  A = nx.adjacency_matrix(G)
  I = numpy.eye(A.shape[0])
  return numpy.linalg.pinv(I - c * A) - I


