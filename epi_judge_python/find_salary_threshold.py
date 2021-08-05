from typing import List

from test_framework import generic_test

def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
  current_salaries.sort()
  n = len(current_salaries)
  total = sum(current_salaries)
  if target_payroll > total:
    return -1
  rsum, cap = 0, 0
  for i in range(n):
    cap = (target_payroll-rsum)/(n-i)
    if current_salaries[i] > cap:
      break
    rsum += current_salaries[i]
  return cap

if __name__ == '__main__':
  # print(find_salary_cap(210, [20, 30, 40, 90, 100]))
  exit(
    generic_test.generic_test_main('find_salary_threshold.py',
                                   'find_salary_threshold.tsv',
                                   find_salary_cap))
