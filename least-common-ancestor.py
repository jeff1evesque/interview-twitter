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
#root = Node(data_root[0])
print(type(data_root[0]))

#tree = BinarySearchTree(root)

for item in data_tree:
  print type(item)
  #tree.add(item)

class Node:
    """ A Node in the Binary Tree """
    
    """ Properties """
    # the data to store
    data = None
    # left and right nodes
    left = None
    right = None

    """ Constructor """
    def __init__(self, d=None, l=None, r=None):
        self.data = d
        self.left = l
        self.right = r
