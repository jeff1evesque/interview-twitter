#!/usr/bin/python

'''
least-common-ancestor.py

Jeffrey Levesque
05/08/2014

Receives input data from input.py in order to generate a binary tree.  Then,
prompts users for two nodes in order to determine a least common ancestor.
'''

# import class definitions
import class_definitions

# location of input file
filename = 'input.txt'

# ignore comment tuple (and new-line) from input file
ignore_type = ("#", "//", "\n")

# cast input values from input file
cast_type = float

# parse root, and tree values from input.py file
with open(filename, 'r') as f:
  for line in f:
    if any(line.startswith(s) for s in ignore_type):
      continue

    elif(line.startswith('root')):
      data_root = line.partition('[')[-1].rpartition(']')[0].split(',')

    elif(line.startswith('tree')):
      data_tree = line.partition('[')[-1].rpartition(']')[0].split(',')

    else:
      print('Error: input file has incorrect syntax')

# create binary search tree (root, and immediate child nodes)
root = class_definitions.Node(cast_type(data_root[0]))
print(type(cast_type(data_root[0])))

#tree = BinarySearchTree(root)

for item in data_tree:
  print type(cast_type(item))
  #tree.add(cast_type(item))
