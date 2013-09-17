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
    G.add_edges_from([(0,2),(1,2),(2,3),(2,4),(3,5),(4,5),(5,6)])
    self.G=G
    self.G.katz_sim = numpy.matrix([\
        [-2.0012094, -2.0012094, -2.223566, 0.26589496, 0.26589496, 2.51900484, 2.26710435], \
        [-2.0012094, -2.0012094, -2.223566, 0.26589496, 0.26589496, 2.51900484, 2.26710435], \
        [-2.223566, -2.223566, -3.47062889, 0.29543884, 0.29543884, 2.79889426, 2.51900484], \
        [0.26589496, 0.26589496, 0.29543884, -0.60176227, -0.60176227, -0.96406358, -0.86765722], \
        [0.26589496, 0.26589496, 0.29543884, -0.60176227, -0.60176227, -0.96406358, -0.86765722], \
        [2.51900484, 2.51900484, 2.79889426, -0.96406358, -0.96406358, -4.87007602, -3.48306842], \
        [2.26710435, 2.26710435, 2.51900484, -0.86765722, -0.86765722, -3.48306842, -3.13476158]
    ])

  def test_katz_sim(self):
    G = self.G
    katz_sim = katz(G)
    nt.assert_equal(len(katz_sim), 7)
    for i in range(self.G.katz_sim.shape[0]):
      for j in range(self.G.katz_sim.shape[1]):
        nt.assert_almost_equal(self.G.katz_sim[i,j], katz_sim[i,j], places=4)

