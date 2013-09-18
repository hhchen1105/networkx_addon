#!/usr/bin/env python

import math
import networkx
import numpy
import os
import sys

import nose.tools as nt

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from similarity import ascos

class TestAscos():
  def test_ascos(self):
    G = networkx.Graph()
    G.add_edge(1,2)
    G.add_edge(1,4)
    G.add_edge(1,5)
    G.add_edge(1,6)
    G.add_edge(2,3)

    node_ids, sim = ascos(G)
    nt.assert_equal(len(node_ids), 6)
    nt.assert_equal(sim.shape, (6, 6))
    sim_ans = numpy.matrix((
        '1      0.5732 0.3474 0.5296 0.5296 0.5296;'
        '0.7563 1      0.6063 0.4005 0.4005 0.4005;'
        '0.6807 0.9000 1      0.3604 0.3604 0.3604;'
        '0.9000 0.5159 0.3126 1      0.4766 0.4766;'
        '0.9000 0.5159 0.3126 0.4766 1      0.4766;'
        '0.9000 0.5159 0.3126 0.4766 0.4766 1'))
    for i in range(sim.shape[0]):
      for j in range(sim.shape[1]):
        nt.assert_almost_equal(sim[i,j], sim_ans[i,j], 4)

  def test_weighted_ascos(self):
    G = networkx.Graph()
    G.add_edge('a', 'b', weight=1)
    node_ids, sim = ascos(G, is_weighted=True)
    for i in range(sim.shape[0]):
      for j in range(sim.shape[1]):
        if i == j:
          nt.assert_equal(sim[i, j], 1)
        else:
          nt.assert_almost_equal(sim[i,j], .9 * (1 - math.exp(-1)), 4)

    G['a']['b']['weight'] = 100
    node_ids, sim = ascos(G, is_weighted=True)
    for i in range(sim.shape[0]):
      for j in range(sim.shape[1]):
        if i == j:
          nt.assert_equal(sim[i, j], 1)
        else:
          nt.assert_almost_equal(sim[i,j], .9 * (1 - math.exp(-100)), 4)

    G = networkx.Graph()
    G.add_edge('a', 'b', weight=1)
    G.add_edge('b', 'c', weight=1)
    node_ids, sim = ascos(G, is_weighted=True)
    print node_ids
    sim_ans = numpy.matrix((
        '1 0.1931 .5689;'
        '0.1931 1 0.5689;'
        '0.3394 0.3394 1'))
    for i in range(sim.shape[0]):
      for j in range(sim.shape[1]):
        print i, ',', j
        nt.assert_almost_equal(sim[i, j], sim_ans[i, j], 4)

    G = networkx.Graph()
    G.add_edge('a', 'b', weight=1)
    G.add_edge('b', 'c', weight=10)
    node_ids, sim = ascos(G, is_weighted=True)
    print node_ids
    sim_ans = numpy.matrix((
        '1 0.4796 0.5689;'
        '0.1762 1 0.9000;'
        '0.1959 0.8429 1'))
    for i in range(sim.shape[0]):
      for j in range(sim.shape[1]):
        print i, ',', j
        nt.assert_almost_equal(sim[i, j], sim_ans[i, j], 4)



