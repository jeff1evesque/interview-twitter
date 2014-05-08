#!/usr/bin/python
'''
least-common-ancestor.py

Jeffrey Levesque
05/08/2014

Receives input data from input.py in order to generate a binary tree.  Then,
prompts users for two nodes in order to determine a least common ancestor.
'''

# location of input file
filename = 'input.py'

# comment tuple (and new-line) from input file
ignore_type = ("#", "//", "\n")

# read data from input.py file
with open(filename, 'r') as f:
  for line in f:
    if any(line.startswith(s) for s in ignore_type):
      continue
    print(line)

if __name__ == '__main__':
  print('hi')
