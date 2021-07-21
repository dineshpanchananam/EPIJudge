from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def bfs(ts):
  if not ts:
    return []
  values = [x.data for x in ts]
  children = [c for t in ts for c in (t.left, t.right) if c]
  return [values]+bfs(children)

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
  from collections import deque
  levels = []
  q = [tree] if tree else []
  while q:
    children = []
    level = []
    for t in q:
      level.append(t.data)
      children += [x for x in (t.left, t.right) if x]
    levels.append(level)
    q = children

  return levels

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('tree_level_order.py',
                                   'tree_level_order.tsv',
                                   binary_tree_depth_order))
