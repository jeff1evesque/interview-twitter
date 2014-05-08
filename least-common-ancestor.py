#!/usr/bin/python
'''
least-common-ancestor.py

Jeffrey Levesque
05/08/2014

Receives input data from input.py in order to generate a binary tree.  Then,
prompts users for two nodes in order to determine a least common ancestor.
'''

# location of input file
filename = 'input.txt'

# ignore comment tuple (and new-line) from input file
ignore_type = ("#", "//", "\n")

# execute commands from input.py file
with open(filename, 'r') as f:
  for line in f:
    if any(line.startswith(s) for s in ignore_type):
      continue
    print(line, type(line))
    exec(line)

class Node:

  """ Constructor """
  def __init__(self, d=None, l=None, r=None):
    print('jeff')

if __name__ == '__main__':
  print('hi')
