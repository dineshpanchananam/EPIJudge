from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    tri = [[1]]
    for i in range(1, n):
        last = tri[-1]
        tri.append([1] + [last[k] + last[k + 1] for k in range(len(last) - 1)] + [1])
    return tri[:n]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
