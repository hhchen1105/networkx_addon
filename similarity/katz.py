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
import scipy.linalg

__author__ = """Hung-Hsuan Chen (hhchen@psu.edu)"""
__all__ = ['katz']

def katz(G, c=0.9, remove_neighbors=False, inv_method=0):
  # TODO: remove sim scores b2n neighbors when remove_neighbors==True
  """Return the katz similarity between nodes

  Parameters
  -----------
  G : graph
    A NetworkX graph
  remove_neighbors: boolean
    if true, only return katz similarity of non-neighbor nodes

  Returns
  -------
  katz: matrix of similarity
  nodelist: the node ids

  Examples
  --------
  >>> G=nx.Graph()
  >>> G.add_edges_from([(0,7), (0,1), (0,2), (0,3), (1,4), (2,4), (3,4), (4,5), (4,6)])
  >>> networkx_addon.similarity.katz(G)

  Notes
  -----

  References
  ----------
  """
  if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
    raise Exception("katz() not defined for graphs with multiedges.")

  if G.is_directed():
    raise Exception("katz() not defined for directed graphs.")

  A = nx.adjacency_matrix(G, nodelist=G.nodes(), weight=None)
  w, v = numpy.linalg.eigh(A)
  lambda1 = max([abs(x) for x in w])
  I = numpy.eye(A.shape[0])
  S = None
  if inv_method == 1:
    S = scipy.linalg.pinv(I - c/lambda1 * A)
  elif inv_method == 2:
    S = numpy.linalg.inv(I - c/lambda1 * A)
  else:
    S = numpy.linalg.pinv(I - c/lambda1 * A)
  return S, G.nodes()

