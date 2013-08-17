#!/usr/bin/env python

import os
import sys
import nose.tools as nt
import networkx

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from similarity import jaccard

class TestJaccard:
  def setUp(self):
    G=networkx.Graph()
    G.add_edges_from([(0,2),(1,2),(2,3),(2,4),(3,5),(4,5),(5,6)])
    self.G=G
    self.G.jaccard = { }
    self.G.jaccard[0] = {1:1, 3:0.5, 4:0.5}
    self.G.jaccard[1] = {0:1, 3:0.5, 4:0.5}
    self.G.jaccard[2] = {5:0.4}
    self.G.jaccard[3] = {0:0.5, 1:0.5, 4:1, 6:0.5}
    self.G.jaccard[4] = {0:0.5, 1:0.5, 3:1, 6:0.5}
    self.G.jaccard[5] = {2:0.4}
    self.G.jaccard[6] = {3:0.5, 4:0.5}

  def test_jaccard(self):
    G = self.G
    jac = jaccard(G)
    nt.assert_equal(len(jac), 7)
    for i in range(7):
      assert(i in jac)
    for i in self.G.jaccard.keys():
      nt.assert_equal(len(self.G.jaccard[i]), len(jac[i]))
      for j in self.G.jaccard[i].keys():
        nt.assert_almost_equal(jac[i][j], self.G.jaccard[i][j], places=4)


