#!/usr/bin/env python

import networkx
import os
import sys

from nose.tools import assert_almost_equal

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from information_propagation import independent_cascade

class TestIndependentCascade():
  run_times = 10000
  def test_independent_cascade(self):
    G = networkx.DiGraph()
    G.add_edge(1,2,act_prob=.5)
    G.add_edge(2,1,act_prob=.5)
    G.add_edge(1,3,act_prob=.2)
    G.add_edge(3,1,act_prob=.2)
    G.add_edge(2,3,act_prob=.3)
    G.add_edge(2,4,act_prob=.5)
    G.add_edge(3,4,act_prob=.1)
    G.add_edge(3,5,act_prob=.2)
    G.add_edge(4,5,act_prob=.2)
    G.add_edge(5,6,act_prob=.6)
    G.add_edge(6,5,act_prob=.6)
    G.add_edge(6,4,act_prob=.3)
    G.add_edge(6,2,act_prob=.4)

    n_A = 0.0
    for i in range(TestIndependentCascade.run_times):
      A = independent_cascade(G, [1], steps=1)
      for layer in A:
        n_A += len(layer)
    assert_almost_equal(n_A / TestIndependentCascade.run_times, 1.7, places=1)

    n_A = 0.0
    A = [ ]
    for i in range(TestIndependentCascade.run_times):
      A = independent_cascade(G, [1], steps=2)
      for layer in A:
        n_A += len(layer)
    assert_almost_equal(n_A / TestIndependentCascade.run_times, 2.16, places=1)

    G = networkx.DiGraph()
    G.add_edges_from([(1,2), (1,3), (2,4), (3,4)], act_prob=0.4)
    n_A = 0.0
    A = [ ]
    for i in range(TestIndependentCascade.run_times):
      A = independent_cascade(G, [1])
      for layer in A:
        n_A += len(layer)
    assert_almost_equal(n_A / TestIndependentCascade.run_times, 2.09, places=1)

  def test_independent_cascade_without_attribute(self):
    G = networkx.DiGraph()
    G.add_edges_from([(1,2), (1,3), (2,4), (3,4)])

    n_A = 0.0
    A = [ ]
    for i in range(TestIndependentCascade.run_times):
      A = independent_cascade(G, [1], steps=1)
      for layer in A:
        n_A += len(layer)
    assert_almost_equal(n_A / TestIndependentCascade.run_times, 1.2, places=1)



