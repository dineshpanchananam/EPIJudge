from typing import List

from test_framework import generic_test, test_utils


<<<<<<< HEAD:epi_judge_python/power_set.py
def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    return []

=======
def generate_power_set(S):
  n, ans = len(S), []
  for i in range(2**n):
    tmp = []
    for j in range(n):
      if i & (1 << j):
        tmp.append(S[j])
    ans.append(tmp)
  return ans
>>>>>>> ee84769... added run and check:epi_judge_python/done/power_set.py

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
