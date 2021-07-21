from test_framework import generic_test

def levenshtein_distance(A: str, B: str) -> int:
  m, n = len(A), len(B)
  dp = [[0]*(n+1) for _ in range(m+1)]
  dp[0] = range(n+1)
  for i in range(m):
    dp[i+1][0] = i+1
  for i in range(1, m+1):
    for j in range(1, n+1):
      c1, c2 = A[i-1], B[j-1]
      sub_cost = 0 if c1 == c2 else 1
      dp[i][j] = min(
        dp[i-1][j-1]+sub_cost,  # substitute
        dp[i-1][j]+1,  # delete from A
        dp[i][j-1]+1,  # add to A
      )

  return dp[-1][-1]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('levenshtein_distance.py',
                                   'levenshtein_distance.tsv',
                                   levenshtein_distance))
