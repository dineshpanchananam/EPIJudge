from test_framework import generic_test

def roman_to_integer(s: str) -> int:
  syms = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
  n = len(s)
  value = syms[s[-1]]
  for i in range(n-2, -1, -1):
    value += (syms[s[i]] if syms[s[i]] >= syms[s[i+1]] else -syms[s[i]])
  return value

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('roman_to_integer.py',
                                   'roman_to_integer.tsv', roman_to_integer))
