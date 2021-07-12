import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
  def __init__(self, data=None, left=None, right=None, size=None):
    self.data = data
    self.left = left
    self.right = right
    self.size = size


def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:

  while tree:
    l_sz = tree.left.size if tree.left else 0
    if l_sz+1 < k:
      k -= (l_sz+1)
      tree = tree.right
    elif l_sz+1 == k:
      break
    else:
      tree = tree.left

  return tree

  # def helper(tree, a):
  #   if tree:
  #     helper(tree.left, a)
  #     a[0] += 1
  #     if a[0] == k:
  #       a[1] = tree
  #     helper(tree.right, a)

  # ans = [0, None]
  # helper(tree, ans)
  # return ans[1]

  # if not tree:
  #   return 0, None
  # lc, lr = helper(tree.left, k)
  # if lc == k:
  #   return k, lr
  # elif lc+1 == k:
  #   return k, tree
  # rc, rr = helper(tree.right, k-lc-1)
  # return 1+lc+rc, rr

  # _, kth = helper(tree, K)
  # return kth


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
  def init_size(node):
    if not node:
      return 0
    node.size = 1+init_size(node.left)+init_size(node.right)
    return node.size

  init_size(tree)

  result = executor.run(functools.partial(find_kth_node_binary_tree, tree, k))

  if not result:
    raise TestFailure('Result can\'t be None')
  return result.data


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('kth_node_in_tree.py',
                                   'kth_node_in_tree.tsv',
                                   find_kth_node_binary_tree_wrapper))
