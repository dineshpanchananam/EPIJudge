import functools
from typing import List
from collections import deque

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
  def lb(t):
    if not t or not (t.left or t.right):
      return
    ext.append(t)
    if t.left:
      lb(t.left)
    elif t.right:
      lb(t.right)

  def rb(t):
    if not t or not (t.left or t.right):
      return
    if t.right:
      rb(t.right)
    elif t.left:
      rb(t.left)
    ext.append(t)

  def leaves(t):
    if not t:
      return []
    if not (t.left or t.right):
      ext.append(t)
    else:
      leaves(t.left)
      leaves(t.right)

  if not tree:
    return []
  ext = [tree]
  lb(tree.left)
  leaves(tree.left)
  leaves(tree.right)
  rb(tree.right)
  return ext

  # ext = {}

  # def helper(tree, loc=0):
  #   if not tree:
  #     return
  #   if loc not in ext:
  #     ext[loc] = tree
  #   helper(tree.left, loc-1)
  #   helper(tree.right, loc+1)

  # helper(tree)
  # return [ext[x] for x in sorted(ext)]

def create_output_list(L):
  if any(l is None for l in L):
    raise TestFailure('Resulting list contains None')
  return [l.data for l in L]

@enable_executor_hook
def create_output_list_wrapper(executor, tree):
  result = executor.run(functools.partial(exterior_binary_tree, tree))

  return create_output_list(result)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                   create_output_list_wrapper))
