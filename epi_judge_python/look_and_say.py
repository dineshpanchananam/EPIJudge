from test_framework import generic_test

def look_and_say(n: int) -> str:
  start = '1'
  for i in range(1, n):
    count, c = 1, start[0]
    new_start = ''
    for k in start[1:]+' ':
      if c == k:
        count += 1
      else:
        new_start = f"{new_start}{count}{c}"
        c, count = k, 1
    start = new_start
  return start

if __name__ == '__main__':
  exit(
    generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                   look_and_say))
