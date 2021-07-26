from test_framework import generic_test

def square_root(k: int) -> int:
  l, h = 0, k
  while l <= h:
    m = (l+h)//2
    if m*m <= k:
      l = m+1
    else:
      h = m-1
  return l-1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('int_square_root.py', 'int_square_root.tsv',
                                   square_root))
