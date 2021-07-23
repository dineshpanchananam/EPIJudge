from test_framework import generic_test

def ss_decode_col_id(col: str) -> int:
  s = 0
  for c in col:
    s = 26*s+(ord(c)-64)
  return s

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('spreadsheet_encoding.py',
                                   'spreadsheet_encoding.tsv',
                                   ss_decode_col_id))
