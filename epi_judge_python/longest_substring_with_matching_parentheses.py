from test_framework import generic_test

def longest_matching_parentheses(s: str) -> int:
  st, n = [], len(s)
  ans, last = 0, -1
  for i in range(n):
    if s[i] == ')' and st and s[st[-1]] == '(':
      st.pop()
      last = -1 if not st else st[-1]
    else:
      ans = max(ans, i-last-1)
      last = i
      st.append(i)
  return max(ans, n-1-last)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main(
      'longest_substring_with_matching_parentheses.py',
      'longest_substring_with_matching_parentheses.tsv',
      longest_matching_parentheses))
