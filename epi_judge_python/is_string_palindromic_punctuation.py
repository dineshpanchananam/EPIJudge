from test_framework import generic_test

def is_palindrome(s: str) -> bool:
  n = len(s)
  i, j = 0, n-1
  while i <= j:
    if not s[i].isalnum():
      i += 1
    elif not s[j].isalnum():
      j -= 1
    elif s[i].lower() != s[j].lower():
      break
    else:
      i, j = i+1, j-1
  return j < i

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('is_string_palindromic_punctuation.py',
                                   'is_string_palindromic_punctuation.tsv',
                                   is_palindrome))
