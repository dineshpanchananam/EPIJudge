from test_framework import generic_test


def look_and_say(n: int) -> str:
    pass


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "look_and_say.py", "look_and_say.tsv", look_and_say
        )
    )
