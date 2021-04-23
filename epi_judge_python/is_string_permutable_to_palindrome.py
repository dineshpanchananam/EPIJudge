from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    char_freq = {}
    for c in s:
        if c not in char_freq:
            char_freq[c] = 0
        char_freq[c] += 1
    return sum(1 for x in char_freq.values() if x & 1) <= 1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            "is_string_permutable_to_palindrome.tsv",
            can_form_palindrome,
        )
    )
