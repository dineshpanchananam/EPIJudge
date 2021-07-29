from typing import List

from test_framework import generic_test

def valid(s):
  if not s:
    return False
  return s == '0' if s.startswith('0') else 0 < int(s) < 256

def get_valid_ip_address(s: str) -> List[str]:
  ips = []
  for i in range(3):
    s1 = s[:i+1]
    if valid(s1):
      for j in range(i+1, i+4):
        s2 = s[i+1:j+1]
        if valid(s2):
          for k in range(j+1, j+4):
            s3 = s[j+1:k+1]
            s4 = s[k+1:]
            if valid(s3) and valid(s4):
              ips.append(f"{s1}.{s2}.{s3}.{s4}")

  return ips

def comp(a, b):
  return sorted(a) == sorted(b)

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('valid_ip_addresses.py',
                                   'valid_ip_addresses.tsv',
                                   get_valid_ip_address,
                                   comparator=comp))
