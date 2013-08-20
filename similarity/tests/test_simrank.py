#!/usr/bin/env python
import nose.tools as nt
import networkx
import os
import sys

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from similarity import simrank

class TestSimRank:
  def setUp(self):
    G = networkx.Graph()
    G.add_edges_from([(0,1),(1,2),(0,2)])
    self.G = G
    self.G.simrank = { }
    self.G.simrank[0] = {0:1, 1:0.6921, 2:0.6921}
    self.G.simrank[1] = {0:0.6921, 1:1, 2:0.6921}
    self.G.simrank[2] = {0:0.6921, 1:0.6921, 2:1}

    H = networkx.Graph()
    H.add_edges_from([(0,1),(0,2),(1,2),(2,3)])
    self.H = H
    self.H.simrank = { }
    self.H.simrank[0] = {0:1, 1:0.6538, 2:0.6261, 3:0.7317}
    self.H.simrank[1] = {0:0.6538, 1:1, 2:0.6261, 3:0.7317}
    self.H.simrank[2] = {0:0.6261, 1:0.6261, 2:1, 3:0.5365}
    self.H.simrank[3] = {0:0.7317, 1:0.7317, 2:0.5365, 3:1}

    I = networkx.Graph()
    I.add_edges_from([(0,1), (1,2), (2,0)])
    I.add_node(3)
    self.I = I
    self.I.simrank = { }
    self.I.simrank[0] = {0:1, 1:0.6921, 2:0.6921, 3:0}
    self.I.simrank[1] = {0:0.6921, 1:1, 2:0.6921, 3:0}
    self.I.simrank[2] = {0:0.6921, 1:0.6921, 2:1, 3:0}
    self.I.simrank[3] = {0:0, 1:0, 2:0, 3:1}

  def test_simrank(self):
    # test graph G
    G = self.G
    sim = simrank(G, remove_neighbors=False, remove_self=False)
    nt.assert_equal(len(sim), 3)
    for i in range(3):
      nt.assert_in(i, sim)
    for i in self.G.simrank.keys():
      nt.assert_equal(len(self.G.simrank[i]), len(sim[i]))
      for j in self.G.simrank[i].keys():
        nt.assert_almost_equal(sim[i][j], self.G.simrank[i][j], places=4)
    # test graph H
    H = self.H
    sim = simrank(H, remove_neighbors=False, remove_self=False)
    nt.assert_equal(len(sim), 4)
    for i in range(4):
      nt.assert_in(i, sim)
    for i in self.H.simrank.keys():
      nt.assert_equal(len(self.H.simrank[i]), len(sim[i]))
      for j in self.H.simrank[i].keys():
        nt.assert_almost_equal(sim[i][j], self.H.simrank[i][j], places=4)

  def test_simrank_disregard_nb(self):
    # test graph G
    G = self.G
    sim = simrank(G, remove_neighbors=False, remove_self=False)
    nt.assert_equal(len(sim), 3)
    for i in range(3):
      nt.assert_in(i, sim)
    for i in self.G.simrank.keys():
      nt.assert_equal(len(self.G.simrank[i]), len(sim[i]))
      for j in self.G.simrank[i].keys():
        nt.assert_almost_equal(sim[i][j], self.G.simrank[i][j], places=4)
    # test graph H
    H = self.H
    sim = simrank(H, remove_neighbors=False, remove_self=False)
    nt.assert_equal(len(sim), 4)
    for i in range(4):
      nt.assert_in(i, sim)
    for i in self.H.simrank.keys():
      nt.assert_equal(len(self.H.simrank[i]), len(sim[i]))
      for j in self.H.simrank[i].keys():
        nt.assert_almost_equal(sim[i][j], self.H.simrank[i][j], places=4)

  def test_graph_with_orphan(self):
    I = self.I
    sim = simrank(I, remove_neighbors=False, remove_self=False)
    nt.assert_equal(len(sim), 4)
    for i in range(4):
      nt.assert_in(i, sim)
    for i in self.I.simrank.keys():
      nt.assert_equal(len(self.I.simrank[i]), len(sim[i]))
      for j in self.I.simrank[i].keys():
        nt.assert_almost_equal(sim[i][j], self.I.simrank[i][j], places=4)


