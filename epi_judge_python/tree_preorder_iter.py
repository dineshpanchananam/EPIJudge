from test_framework import generic_test


def preorder_traversal(tree):
  data = []
  if tree:
    data = [tree.data]
    data += preorder_traversal(tree.left)
    data += preorder_traversal(tree.right)
  return data
  
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
