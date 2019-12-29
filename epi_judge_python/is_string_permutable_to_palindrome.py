from test_framework import generic_test

<<<<<<< HEAD

def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    return True

=======
def can_form_palindrome(s):
  d = {}
  for i in s:
    d[i] = d.get(i, 0) + 1
  freqs = d.values()
  return len([x for x in freqs if x % 2 == 1]) < 2
>>>>>>> cf3ad5a... solved some

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
