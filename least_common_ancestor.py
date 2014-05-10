#!/usr/bin/python

'''
least_common_ancestor.py

Jeffrey Levesque
05/08/2014

Receives input data from input.py in order to generate a binary tree.  Then,
prompts users for two nodes in order to determine a least common ancestor.
'''

# import class definitions
import class_definitions

# import general python classes
import sys

# location of input file
filename = 'input.txt'

# ignore comment tuple (and new-line) from input file
ignore_type = ("#", "//", "\n")

# cast input values from input file
cast_type = float

# prompt user for value or parse filename
if sys.version_info >= (3,0,0):
  prompt_input_type = input('Would you like to enter values?')
else:
  prompt_input_type = raw_input('Would you like to enter values?')

# parse root, and tree values from input.py file
with open(filename, 'r') as f:
  for line in f:
    if any(line.startswith(s) for s in ignore_type):
      continue

    elif(line.startswith('root')):
      data_root = line.partition('[')[-1].rpartition(']')[0].split(',')

    elif(line.startswith('tree')):
      data_tree = line.partition('[')[-1].rpartition(']')[0].split(',')

    elif(line.startswith('lca')):
      data_lca = line.partition('[')[-1].rpartition(']')[0].split(',')

    else:
      print('Error: input file has incorrect syntax')

# create binary search tree (root, and immediate child nodes)
root = class_definitions.Node(cast_type(data_root[0]))

for item in data_tree:
  root.insert(cast_type(item))

# return least common ancestor
lca = root.lca_algorithm(cast_type(data_lca[0]), cast_type(data_lca[1]), root)
print('least common ancestor: ', lca.data)

# print binary search tree
root.print_tree_breadth()
