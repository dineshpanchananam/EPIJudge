from typing import List

from test_framework import generic_test

def justify_text(words: List[str], L: int) -> List[str]:
  def transform(x):
    words = x.strip().split()
    if len(words) == 1:
      return f"{words[0]}{' '*(L-len(words[0]))}"
    wl = sum(len(w) for w in words)
    gaps = len(words)-1
    spaces = (L-wl)//gaps
    extra = L-wl-gaps*spaces
    spaces = [" "*spaces]*gaps
    for i in range(extra):
      spaces[i] += " "
    spaces.append('')
    return "".join(w+s for (w, s) in zip(words, spaces))

  res = []
  i, n = 0, len(words)
  tmp = ""
  for word in words:
    if len(tmp+word) <= L:
      tmp += word+" "
    else:
      res.append(transform(tmp))
      tmp = word+" "
  tmp = tmp.strip()
  return res+[tmp+' '*(L-len(tmp))]

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('left_right_justify_text.py',
                                   'left_right_justify_text.tsv',
                                   justify_text))
