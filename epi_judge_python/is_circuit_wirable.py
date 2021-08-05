import functools
from typing import List
import collections

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class GraphVertex:
  def __init__(self) -> None:
    self.d = -1
    self.edges: List[GraphVertex] = []

def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
  def bfs(s):
    s.d += 1
    q = collections.deque([s])
    while q:
      node = q.popleft()
      for v in node.edges:
        if v.d == -1:
          v.d = 1-node.d
          q.append(v)
        elif v.d == node.d:
          return False
    return True

  return all(bfs(x) for x in graph if x.d == -1)

  # is_bipartite = True
  # q = collections.deque(graph)
  # colors = {}
  # while q:
  #   node = q.popleft()
  #   if node not in colors:
  #     colors[node] = 0
  #   for v in node.edges:
  #     if v not in colors:
  #       colors[v] = 1-colors[node]
  #       q.append(v)
  #     elif colors[v] == colors[node]:
  #       is_bipartite = False
  #       q.clear()
  # return is_bipartite

@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
  if k <= 0:
    raise RuntimeError('Invalid k value')
  graph = [GraphVertex() for _ in range(k)]

  for (fr, to) in edges:
    if fr < 0 or fr >= k or to < 0 or to >= k:
      raise RuntimeError('Invalid vertex index')
    graph[fr].edges.append(graph[to])

  return executor.run(functools.partial(is_any_placement_feasible, graph))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_circuit_wirable.py',
                                   'is_circuit_wirable.tsv',
                                   is_any_placement_feasible_wrapper))
