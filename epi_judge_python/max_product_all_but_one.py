from typing import List

from test_framework import generic_test

def find_biggest_n_minus_one_product(A: List[int]) -> int:
  suff, s = [1], 1
  for i in reversed(A):
    s *= i
    suff.append(s)
  suff.reverse()
  pfx_prd, ans = 1, float('-inf')
  for i in range(len(A)):
    ans = max(ans, pfx_prd*suff[i+1])
    pfx_prd *= A[i]
  return ans

  # pos, neg, zero = 0, 0, 0
  # pos_prod = 1
  # neg_prod = 1
  # max_neg = float('-inf')
  # min_pos = float('inf')
  # for a in A:
  #   if a > 0:
  #     pos_prod *= a
  #     min_pos = min(min_pos, a)
  #     pos += 1
  #   elif a < 0:
  #     neg_prod *= a
  #     max_neg = max(max_neg, a)
  #     neg += 1
  #   else:
  #     zero += 1

  # if zero > 1:
  #   return 0
  # if zero:
  #   if neg & 1:
  #     return 0
  #   else:
  #     return pos_prod*neg_prod
  # elif neg & 1:
  #   return (pos_prod*neg_prod)//(max_neg)
  # elif neg > 1:
  #   return pos_prod*neg_prod//min(abs(max_neg), min_pos)
  # return (pos_prod*neg_prod)//min_pos

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('max_product_all_but_one.py',
                                   'max_product_all_but_one.tsv',
                                   find_biggest_n_minus_one_product))
