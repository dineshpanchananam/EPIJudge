import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook

def p(node):
  if node:
    l = p(node.left)
    tmp = node.data
    r = p(node.right)
    return l + [[tmp, node]] + r
  return []

<<<<<<< HEAD:epi_judge_python/successor_in_tree.py
def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    return None

=======
def find_successor(node):
  if curr := node.right:
    while curr:
      succ = curr
      curr = curr.left
    return succ
  while node.parent and node.parent.right == node:
    node = node.parent
  return node.parent
>>>>>>> c369a0b... some other problems:epi_judge_python/done/successor_in_tree.py

@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
