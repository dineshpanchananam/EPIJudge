from test_framework import generic_test

# 1 2 5 7
# 3 6 8

# 1 2 3 5
# 6 7 8

def fill(A, B, m, n, s, e, i, j):
  for k in range(s, e):
    if (i < m and j < n and A[i] < B[j]) or (j >= n):
      A[k] = A[i]
      i += 1
    else:
        A[k] = B[j]
        j += 1
  return i, j

def merge_two_sorted_arrays1(A, m, B, n):
  i, j = fill(A, B, m, n, m, m+n, 0, 0)
  _, _ = fill(A, B, m, n, 0, m, i, j)
  for i in range(n):
    B[i] = A[m+i]
  for i in range(1, m+1):
    A[n+m-i] = A[m-i]
  for i in range(n):
    A[i] = B[i]

def merge_two_sorted_arrays(A, m, B, n):
  w_idx = m + n - 1
  i, j = m - 1, n - 1
  while i >= 0 and j >= 0:
    if A[i] > B[j]:
      A[w_idx] = A[i]
      i -= 1
    else:
      A[w_idx] = B[j]
      j -= 1
    w_idx -= 1
  while j >= 0:
    A[w_idx] = B[j]
    j -= 1
    w_idx -= 1

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
