#!/usr/bin/env python

import nose.tools as nt
import networkx
import os
import sys

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from similarity import rss2

class TestRss2:
  def setUp(self):
    G = networkx.Graph()
    G.add_edges_from([(0,2),(1,2),(2,3),(2,4),(3,5),(4,5),(5,6),(3,7)])
    self.G = G
    self.G.rss2_sim = { }
    self.G.rss2_sim[0] = {1:0.25, 3:0.25, 4:0.25}
    self.G.rss2_sim[1] = {0:0.25, 3:0.25, 4:0.25}
    self.G.rss2_sim[2] = {5:0.2083, 7:0.0833}
    self.G.rss2_sim[3] = {0:0.0833, 1:0.0833, 4:0.1944, 6:0.1111}
    self.G.rss2_sim[4] = {0:0.125, 1:0.125, 3:0.2917, 6:0.1667}
    self.G.rss2_sim[5] = {2:0.2778, 7:0.1111}
    self.G.rss2_sim[6] = {3:0.3333, 4:0.3333}
    self.G.rss2_sim[7] = {2:0.3333, 5:0.3333}

    H = networkx.Graph()
    H.add_edges_from([(0,1,{'weight':2}), (1,2,{'weight':1}), \
        (0,3,{'weight':1}), (3,2,{'weight':3}), (2,4,{'weight':4})])
    self.H = H
    self.H.rss2_sim = { }
    self.H.rss2_sim[0] = {2:0.4722}
    self.H.rss2_sim[1] = {3:0.3472, 4:0.1667}
    self.H.rss2_sim[2] = {0:0.1771}
    self.H.rss2_sim[3] = {1:0.2604, 4:0.375}
    self.H.rss2_sim[4] = {1:0.125, 3:0.375}

  def test_rss2_sim_no_weight(self):
    G = self.G
    rss2_sim = rss2(G, disregard_weight=True)
    nt.assert_equal(len(rss2_sim), 8)
    for i in range(8):
      assert(i in rss2_sim)
    for i in self.G.rss2_sim.keys():
      nt.assert_equal(len(self.G.rss2_sim[i]), len(rss2_sim[i]))
      for j in self.G.rss2_sim[i].keys():
        nt.assert_almost_equal(rss2_sim[i][j], self.G.rss2_sim[i][j], places=4)

  def test_rss2_sim_with_weight(self):
    H = self.H
    rss2_sim = rss2(H)
    nt.assert_equal(len(rss2_sim), 5)
    for i in range(5):
      assert(i in rss2_sim)
    for i in self.H.rss2_sim.keys():
      nt.assert_equal(len(self.H.rss2_sim[i]), len(rss2_sim[i]))
      for j in self.H.rss2_sim[i].keys():
        print i, ',', j
        nt.assert_almost_equal(rss2_sim[i][j], self.H.rss2_sim[i][j], places=4)



