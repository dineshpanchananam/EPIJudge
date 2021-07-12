from functools import lru_cache
from typing import List

from test_framework import generic_test


def is_valid(x):
    return x and (len(x) == 1 or (x[0] != "0" and int(x) <= 255))


@lru_cache
def helper(s, n):
    if n == 1:
        return [s] if is_valid(s) else []

    addrs = []
    for i in range(1, len(s)):
        part = s[:i]
        if is_valid(part):
            sub = helper(s[i:], n - 1)
            addrs.extend([f"{part}.{x}" for x in sub])
    return addrs


def get_valid_ip_address_x(s: str):
    return helper(s, 4)


def get_valid_ip_address(s: str) -> List[str]:
    n = len(s)
    result = []
    for i in range(1, min(n, 4)):
        p1 = s[:i]
        if is_valid(p1):
            for j in range(i, min(n, i + 4)):
                p2 = s[i:j]
                if is_valid(p2):
                    for k in range(j, min(n, j + 4)):
                        p3 = s[j:k]
                        p4 = s[k:]
                        if is_valid(p3) and is_valid(p4):
                            result.append(f"{p1}.{p2}.{p3}.{p4}")
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            "valid_ip_addresses.tsv",
            get_valid_ip_address,
            comparator=comp,
        )
    )
