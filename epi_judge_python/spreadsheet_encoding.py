from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
  to_int = lambda x: ord(x)-64
  ans = 0
  for x in col:
    ans = 26*ans+to_int(x)
  return ans


if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('spreadsheet_encoding.py',
                                   'spreadsheet_encoding.tsv',
                                   ss_decode_col_id))
