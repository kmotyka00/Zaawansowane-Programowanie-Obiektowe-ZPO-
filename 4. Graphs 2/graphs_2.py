# !/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Set, Dict, NamedTuple
import networkx as nx


# ZADANIE 1: NEIGHBORS


# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int
#
Distance = int
# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]


class NodeAndDistance(NamedTuple):
    node: VertexID
    distance: Distance


def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    white = set()
    gray = set()
    black = set()
    for key in adjlist.keys():
        if key not in white:
            white.add(key)
        for value in adjlist[key]:
            if value not in white:
                white.add(value)
    white.remove(start_vertex_id)
    gray.add(start_vertex_id)
    Q = list()
    d = 0
    Q.append(NodeAndDistance(start_vertex_id, d))
    while Q:
        u = Q.pop(0)
        if u.distance > max_distance:
            break
        if u.node in adjlist.keys():
            for node in adjlist[u.node]:
                if node in white:
                    white.remove(node)
                    gray.add(node)
                    Q.append(NodeAndDistance(node, u.distance + 1))
            gray.remove(u.node)
            black.add(u.node)
        else:
            black.add(u.node)
    black.remove(start_vertex_id)
    return black


VertexID = int
EdgeID = int


# Nazwana krotka reprezentująca segment ścieżki.
class TrailSegmentEntry(NamedTuple):
    aNode: VertexID
    bNode: VertexID
    edgeId: EdgeID
    weight: float


Trail = List[TrailSegmentEntry]


def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.

    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """
    with open(filepath) as f:
        edges = []
        for line in f:
            if line.strip():
                elem = line.split(" ")
                va = int(elem[0])
                vb = int(elem[1])
                w = float(elem[2])
                edges.append((va, vb, w))
        g = nx.MultiDiGraph()
        g.add_weighted_edges_from(edges)
        return g


def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.

    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """
    dij_path_nodes = nx.dijkstra_path(g, v_start, v_end)
    result: Trail = []
    for i in range(0, len(dij_path_nodes)-1):
        min_weight = g[dij_path_nodes[i]][dij_path_nodes[i+1]][0]['weight']
        path_number = 0
        dct = g[dij_path_nodes[i]][dij_path_nodes[i+1]]
        for path in dct:
            if dct[path]['weight'] < min_weight:
                path_number = path
                min_weight = dct[path]['weight']
        result.append(TrailSegmentEntry(dij_path_nodes[i], dij_path_nodes[i+1], path_number, min_weight))
    return result


def trail_to_str(trail: Trail) -> str:
    str_res = ""
    sum_of_weights = 0
    for elem in trail:
        sum_of_weights = sum_of_weights + elem.weight
        str_res = str_res + str(elem.aNode) + " -[" + str(elem.edgeId) + ": " + str(elem.weight)\
                  + "]-> "
    str_res = str_res + str(trail[-1].bNode) + "  (total = " + str(sum_of_weights) + ")"
    return str_res

