from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
  if not tree:
    return []
  st = [(tree, 0)]
  order = []
  while st:
    n, marked = st.pop()
    if marked:
      order.append(n)
    elif n:
      st.append((n.data, 1))
      st.append((n.right, 0))
      st.append((n.left, 0))
  return order

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('tree_postorder.py', 'tree_postorder.tsv',
                                   postorder_traversal))
