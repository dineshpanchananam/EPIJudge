from test_framework import generic_test

def is_well_formed(s: str) -> bool:
  clos = {'}': '{', ']': '[', ')': '('}
  st = []
  for c in s:
    if c in clos:
      if st and st[-1] == clos[c]:
        st.pop()
      else:
        return False
    else:
      st.append(c)
  return not st

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_valid_parenthesization.py',
                                   'is_valid_parenthesization.tsv',
                                   is_well_formed))
