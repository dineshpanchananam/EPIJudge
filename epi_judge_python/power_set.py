from typing import List

from test_framework import generic_test, test_utils


# def generate_power_set(input_set: List[int]) -> List[List[int]]:
#     n = len(input_set)
#     ans = []
#     for i in range(1 << n):
#         tmp = []
#         for j in range(n):
#             if (1 << j) & i:
#                 tmp.append(input_set[j])
#         ans.append(tmp)
#     return ans


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def subs(a):
        if not a:
            return [[]]
        rest = subs(a[1:]) or []
        return rest + [[a[0]] + x for x in rest]

    return subs(input_set)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "power_set.py",
            "power_set.tsv",
            generate_power_set,
            test_utils.unordered_compare,
        )
    )
