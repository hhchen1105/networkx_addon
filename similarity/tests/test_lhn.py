#!/usr/bin/env python
import nose.tools as nt
import networkx
import numpy
import os
import sys

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from similarity import lhn

class TestKatzSim:
  def setUp(self):
    G=networkx.Graph()
    G.add_edges_from([(0,1), (0,3), (0,4), (0,5), (1,2)])
    self.G=G
    self.G.lhn_sim = numpy.matrix([\
        [0.3074, 0.3286, 0.2851, 0.5334, 0.5334, 0.5334], \
        [0.3286, 0.6592, 0.5720, 0.5702, 0.5702, 0.5702], \
        [0.2851, 0.5720, 1.4964, 0.4948, 0.4948, 0.4948], \
        [0.5334, 0.5702, 0.4948, 1.9258, 0.9258, 0.9258], \
        [0.5334, 0.5702, 0.4948, 0.9258, 1.9258, 0.9258], \
        [0.5334, 0.5702, 0.4948, 0.9258, 0.9258, 1.9258]
    ])

  def test_lhn_sim(self):
    G = self.G
    lhn_sim, nodelist = lhn(G)
    nt.assert_equal(len(nodelist), 6)
    for i in range(6):
      nt.assert_true(i in nodelist)
    nt.assert_equal(len(lhn_sim), 6)
    for i in range(self.G.lhn_sim.shape[0]):
      for j in range(self.G.lhn_sim.shape[1]):
        print i, ',', j
        nt.assert_almost_equal(self.G.lhn_sim[i,j], lhn_sim[i,j], places=4)

