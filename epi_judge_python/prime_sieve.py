from typing import List

from test_framework import generic_test

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
  s = [1]*(n+1)
  primes = []
  for i in range(2, n+1):
    if s[i]:
      primes.append(i)
      for k in range(2*i, n+1, i):
        s[k] = 0
  return primes

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                   generate_primes))
