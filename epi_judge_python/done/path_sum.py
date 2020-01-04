from test_framework import generic_test


def has_path_sum(tree, remaining_weight, path=[]):
  if not tree:
    return False
  diff = remaining_weight - tree.data
  if not (tree.left or tree.right):
    return diff == 0
  return has_path_sum(tree.left, diff) or \
         has_path_sum(tree.right, diff)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
          "path_sum.py", 
          'path_sum.tsv',
          has_path_sum))
