from typing import List

from test_framework import generic_test

def justify_text(words: List[str], L: int) -> List[str]:
  tmp, tl, res = [], 0, []
  for word in words:
    lw = len(word)
    if tl+len(tmp)+lw <= L:
      tmp.append(word)
      tl += lw
    else:
      if len(tmp) == 1:
        res.append(f'{tmp[0]}{" "*(L-tl)}')
      else:
        space, extra = divmod(L-tl, len(tmp)-1)
        res.append((" "*space).join(tmp).replace(
          " "*space,
          " "*(space+1),
          extra,
        ))
      tmp, tl = [word], lw

  tmp = " ".join(tmp)
  return res+[tmp+' '*(L-len(tmp))]

if __name__ == '__main__':
  justify_text(
    ["Text", "justification", "is", "trickier", "than", "it", "seems!"], 14)
  exit(
    generic_test.generic_test_main('left_right_justify_text.py',
                                   'left_right_justify_text.tsv',
                                   justify_text))
