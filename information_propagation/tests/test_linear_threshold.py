#!/usr/bin/env python

import networkx
import os
import sys

from nose.tools import assert_equal

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../..')))
from information_propagation import linear_threshold

class TestDiffusionLinearThreshold():
  def test_linear_threshold(self):
    G = networkx.DiGraph()
    G.add_edge(1,2,influence=.5)
    G.add_edge(2,1,influence=.5)
    G.add_edge(1,3,influence=.2)
    G.add_edge(3,1,influence=.2)
    G.add_edge(2,3,influence=.3)
    G.add_edge(2,4,influence=.5)
    G.add_edge(3,4,influence=.1)
    G.add_edge(3,5,influence=.2)
    G.add_edge(4,5,influence=.2)
    G.add_edge(5,6,influence=.6)
    G.add_edge(6,5,influence=.6)
    G.add_edge(6,4,influence=.3)
    G.add_edge(6,2,influence=.4)
    G.node[2]['threshold'] = .4
    G.node[3]['threshold'] = .4
    G.node[4]['threshold'] = .55
    G.node[5]['threshold'] = .5
    G.node[6]['threshold'] = .3

    layers = linear_threshold(G, [1])

    print layers

    assert_equal(len(layers[0]), 1)
    assert(1 in layers[0])
    assert_equal(len(layers[1]), 1)
    assert(2 in layers[1])
    assert_equal(len(layers[2]), 1)
    assert(3 in layers[2])
    assert_equal(len(layers[3]), 1)
    assert(4 in layers[3])
    assert_equal(len(reduce(lambda x,y: x+y, layers)), 4)

  def test_linear_threshold_graph_without_attribute(self):
    G = networkx.Graph()
    G.add_edges_from([(1,2), (1,3), (2,3), (3,4), (3,5), (4,5), (4,6), (5,6)])

    layers = linear_threshold(G, [1])
    assert_equal(len(layers[0]), 1)
    assert(1 in layers[0])
    assert_equal(len(layers[1]), 1)
    assert(2 in layers[1])
    assert_equal(len(layers[2]), 1)
    assert(3 in layers[2])

    layers = linear_threshold(G, [1,4])
    assert_equal(len(reduce(lambda x,y: x+y, layers)), 6)

    layers = linear_threshold(G, [1,2])
    assert_equal(len(layers[0]), 2)
    assert(1 in layers[0])
    assert(2 in layers[0])
    assert_equal(len(layers[1]), 1)
    assert(3 in layers[1])

  def test_linear_threshold_with_step(self):
    G = networkx.DiGraph()
    G.add_edge(1,2,influence=.5)
    G.add_edge(2,1,influence=.5)
    G.add_edge(1,3,influence=.2)
    G.add_edge(3,1,influence=.2)
    G.add_edge(2,3,influence=.3)
    G.add_edge(2,4,influence=.5)
    G.add_edge(3,4,influence=.1)
    G.add_edge(3,5,influence=.2)
    G.add_edge(4,5,influence=.2)
    G.add_edge(5,6,influence=.6)
    G.add_edge(6,5,influence=.6)
    G.add_edge(6,4,influence=.3)
    G.add_edge(6,2,influence=.4)
    G.node[2]['threshold'] = .4
    G.node[3]['threshold'] = .4
    G.node[4]['threshold'] = .55
    G.node[5]['threshold'] = .5
    G.node[6]['threshold'] = .3

    layers = linear_threshold(G, [1], 1)
    assert_equal(len(layers[0]), 1)
    assert(1 in layers[0])
    assert_equal(len(layers[1]), 1)
    assert(2 in layers[1])

    layers = linear_threshold(G, [1], 2)
    assert_equal(len(layers[0]), 1)
    assert(1 in layers[0])
    assert_equal(len(layers[1]), 1)
    assert(2 in layers[1])
    assert_equal(len(layers[2]), 1)
    assert(3 in layers[2])


