from test_framework import generic_test

def shortest_equivalent_path(path: str) -> str:
  s = []
  for d in path.split("/"):
    if d in ".":
      continue
    if d == ".." and s and s[-1] != '..':
      s.pop()
    else:
      s.append(d)
  return ("/" if path.startswith("/") else "")+"/".join(s).rstrip("/")

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('directory_path_normalization.py',
                                   'directory_path_normalization.tsv',
                                   shortest_equivalent_path))
