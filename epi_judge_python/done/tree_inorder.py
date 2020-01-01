from test_framework import generic_test


def inorder_traversal(tree):
  data = []
  if tree:
    data += inorder_traversal(tree.left)
    data += [tree.data]
    data += inorder_traversal(tree.right)
  return data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
