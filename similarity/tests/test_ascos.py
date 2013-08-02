#!/usr/bin/env python

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

