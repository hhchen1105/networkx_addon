#!/usr/bin/env python
import nose.tools as nt
import networkx
import numpy
import os
import sys

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from similarity import katz

class TestKatzSim:
  def setUp(self):
    G=networkx.Graph()
    G.add_edges_from([(0,1), (0,3), (0,4), (0,5), (1,2)])
    self.G=G
    self.G.katz_sim = numpy.matrix([\
        [4.9178, 2.6286, 1.1405, 2.1337, 2.1337, 2.1337], \
        [2.6286, 2.6369, 1.1441, 1.1405, 1.1405, 1.1405], \
        [1.1405, 1.1441, 1.4964, 0.4948, 0.4948, 0.4948], \
        [2.1337, 1.1405, 0.4948, 1.9258, 0.9258, 0.9258], \
        [2.1337, 1.1405, 0.4948, 0.9258, 1.9258, 0.9258], \
        [2.1337, 1.1405, 0.4948, 0.9258, 0.9258, 1.9258]
    ])

  def test_katz_sim(self):
    G = self.G
    katz_sim, nodelist = katz(G)
    nt.assert_equal(len(nodelist), 6)
    for i in range(6):
      nt.assert_true(i in nodelist)
    nt.assert_equal(len(katz_sim), 6)
    for i in range(self.G.katz_sim.shape[0]):
      for j in range(self.G.katz_sim.shape[1]):
        print i, ',', j
        nt.assert_almost_equal(self.G.katz_sim[i,j], katz_sim[i,j], places=4)

