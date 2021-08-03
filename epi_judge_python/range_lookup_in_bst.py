import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))

def inorder(t, fn):
  if t:
    inorder(t.left, fn)
    proceed = fn(t.data)
    inorder(t.right, fn)

def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
  order = []

  def fn(x):
    if interval.left <= x <= interval.right:
      order.append(x)

  inorder(tree, fn)
  return order

  # if not tree:
  #   return []
  # if tree.data > interval.right:
  #   return range_lookup_in_bst(tree.left, interval)
  # if tree.data < interval.left:
  #   return range_lookup_in_bst(tree.right, interval)
  # return range_lookup_in_bst(tree.left, Interval(interval.left, tree.data))+[
  #   tree.data
  # ]+range_lookup_in_bst(tree.right, Interval(tree.data, interval.right))

def range_lookup_in_bst_wrapper(tree, i):
  return range_lookup_in_bst(tree, Interval(*i))

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('range_lookup_in_bst.py',
                                   'range_lookup_in_bst.tsv',
                                   range_lookup_in_bst_wrapper))
