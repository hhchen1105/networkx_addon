#!/usr/bin/env python
import os
import sys
import nose.tools as ns
import networkx

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from similarity import cosine

class TestCosSim:
  def setUp(self):
    G=networkx.Graph()
    G.add_edges_from([(0,2),(1,2),(2,3),(2,4),(3,5),(4,5),(5,6)])
    self.G = G
    self.G.cos_sim = { }
    self.G.cos_sim[0] = {1:0.5, 3:0.3333, 4:0.3333}
    self.G.cos_sim[1] = {0:0.5, 3:0.3333, 4:0.3333}
    self.G.cos_sim[2] = {5:0.2857}
    self.G.cos_sim[3] = {0:0.3333, 1:0.3333, 4:0.5, 6:0.3333}
    self.G.cos_sim[4] = {0:0.3333, 1:0.3333, 3:0.5, 6:0.3333}
    self.G.cos_sim[5] = {2:0.2857}
    self.G.cos_sim[6] = {3:0.3333, 4:0.3333}

  def test_cosine(self):
    G = self.G
    cos = cosine(G)
    ns.assert_equal(len(cos), 7)
    for i in range(7):
      assert(i in cos)
    for i in self.G.cos_sim.keys():
      ns.assert_equal(len(self.G.cos_sim[i]), len(cos[i]))
      for j in self.G.cos_sim[i].keys():
        ns.assert_almost_equal(cos[i][j], self.G.cos_sim[i][j], places=4)


