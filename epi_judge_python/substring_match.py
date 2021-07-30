from test_framework import generic_test

def hash_key(s):
  key = 0
  for c in s:
    key = key*2+ord(c)
  return key

def rabin_karp(t: str, s: str) -> int:
  t = "#"+t
  m, n = len(s), len(t)
  s_hash = hash_key(s)
  t_hash = hash_key(t[:m])
  last_power = 2**(m-1)
  for start in range(m, n):
    t_hash -= last_power*ord(t[start-m])
    t_hash = t_hash*2+ord(t[start])
    if s_hash == t_hash:
      return start-m

  return -1

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('substring_match.py', 'substring_match.tsv',
                                   rabin_karp))
