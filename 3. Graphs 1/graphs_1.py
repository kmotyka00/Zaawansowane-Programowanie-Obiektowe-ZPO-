#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Dict, List


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    n = len(adjmat)
    dct: Dict[int, List[int]] = dict()
    for i in range(0, n):
        lst = []
        for j in range(0, n):
            for k in range(0, adjmat[i][j]):
                lst.append(j+1)
        if len(lst) > 0:
            dct[i+1] = lst
    return dct


def dfs_recursive_inside(G: Dict[int,List[int]], s: int, visited: List[int]) -> List[int]:
    visited.append(s)
    if s in G.keys():
        for u in G[s]:
            if u not in visited:
                dfs_recursive_inside(G, u, visited)
    return visited


def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    visited = []
    result = dfs_recursive_inside(G, s, visited)
    return result


def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack: List[int] = list()
    visited: List[int] = list()
    stack.append(s)
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if v in G.keys():
                for u in G[v][::-1]:
                    stack.append(u)
    return visited


def is_acyclic(G: Dict[int, List[int]]) -> bool:
    for node in G.keys():
        for reachableNode in G[node]:
            visited = dfs_recursive(G, reachableNode)
            if node in visited:
                return False
    return True
