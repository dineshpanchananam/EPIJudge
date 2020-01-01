from test_framework import generic_test
import bisect

def search_first_of_k(A, k):
  last_found = -1
  l, h = 0, len(A)-1
  while l <= h:
    mid = (l + h) // 2
    if A[mid] == k:
      last_found = mid
      h = mid-1
    elif A[mid] < k:
      l = mid + 1
    else:
      h = mid - 1
  return last_found

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
