from test_framework import generic_test

from functools import lru_cache


def dp(n, k):
  if k in (0, n):
    return 1
  k = min(k, n-k)
  cache = [1]+[0]*k
  for _ in range(n):
    for j in range(k, 0, -1):
      cache[j] += cache[j-1]
  return cache[-1]


def compute_binomial_coefficient(n: int, k: int) -> int:
  return dp(n, k)


@lru_cache
def compute_binomial_coefficient_recur(n: int, k: int) -> int:
  if k in (0, n):
    return 1
  return (compute_binomial_coefficient(n-1, k-1)+
          compute_binomial_coefficient(n-1, k))


# 5c3
# 1 0 0 0
# 1 1 0 0
# 1 2 1 0
# 1 3 3 1
# 1 4 6 4
# 1 5 10 10

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('binomial_coefficients.py',
                                   'binomial_coefficients.tsv',
                                   compute_binomial_coefficient))
