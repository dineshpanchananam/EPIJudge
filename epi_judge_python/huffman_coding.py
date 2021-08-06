import collections
import functools
from typing import List
import heapq as h
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

CharWithFrequency = collections.namedtuple('CharWithFrequency', ('c', 'freq'))

class node:
  def __init__(self, k, f, left=None, right=None):
    self.key = k
    self.freq = f
    self.left = left
    self.right = right

  def __lt__(self, other):
    return self.freq < other.freq

def preorder(r):
  if r:
    return f"({r.key} {preorder(r.left)} {preorder(r.right)})"
  else:
    return '-'

def sum_codes(root, acc=0):
  if not root:
    return 0
  if not (root.left or root.right):
    return acc*root.freq/100
  return sum_codes(root.left, acc+1)+sum_codes(root.right, acc+1)

def huffman_encoding(symbols: List[CharWithFrequency]) -> float:
  heap = [node(s.c, s.freq) for s in symbols]
  h.heapify(heap)
  while len(heap) > 1:
    a = h.heappop(heap)
    b = h.heappop(heap)
    h.heappush(heap, node('.', a.freq+b.freq, left=a, right=b))
  root = heap[0]
  return sum_codes(root)

@enable_executor_hook
def huffman_encoding_wrapper(executor, symbols):
  if any(len(x[0]) != 1 for x in symbols):
    raise RuntimeError('CharWithFrequency parser: string length is not 1')

  symbols = [CharWithFrequency(c[0], freq) for (c, freq) in symbols]
  return executor.run(functools.partial(huffman_encoding, symbols))

if __name__ == '__main__':
  # print(
  #   huffman_encoding([
  #     CharWithFrequency('a', 2),
  #     CharWithFrequency('b', 4),
  #     CharWithFrequency('c', 1),
  #     CharWithFrequency('d', 8),
  #   ]))
  exit(
    generic_test.generic_test_main('huffman_coding.py', 'huffman_coding.tsv',
                                   huffman_encoding_wrapper))
