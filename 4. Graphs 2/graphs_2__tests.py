#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import graphs_2
import networkx as nx


class TestDijkstra(unittest.TestCase):
    def test_length(self):
        g = nx.MultiDiGraph()
        g.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 0.4), (2, 3, 0.3), (1, 3, 1.0)])
        trial = graphs_2.find_min_trail(g, 1, 3)
        sum_of_weights = 0
        for elem in trial:
            sum_of_weights = sum_of_weights + elem.weight
        self.assertEqual(sum_of_weights, nx.dijkstra_path_length(g, 1, 3))