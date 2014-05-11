#!/usr/bin/python

'''
least_common_ancestor.py

Jeffrey Levesque
05/08/2014

Receives input data from input.py in order to generate a binary tree.  Then,
prompts users for two nodes in order to determine a least common ancestor.
'''

# import class and variable definitions
import definitions_class
import definitions_variable

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

if prompt_input_type in definitions_variable.possible_yes:
  data_tree = []

  while True:
    if sys.version_info >= (3,0,0):
      tree_value = input('Enter tree value (q - to quit): ')
    else:
      tree_value = raw_input('Enter tree value (q - to quit): ')

    if tree_value in definitions_variable.possible_quit:
      break
    else:
      data_tree.append(tree_value)

  data_root = list(data_tree[0])
  data_tree = list(data_tree[1:])

  data_lca = []

  if sys.version_info >= (3,0,0):
    data_lca.append(input('Enter the first LCA node value: '))
    data_lca.append(input('Enter the second LCA node value: '))
  else:
    data_lca.append(raw_input('Enter the first LCA node value: '))
    data_lca.append(raw_input('Enter the second LCA node value: '))

# parse root, and tree values from filename source
elif prompt_input_type in definitions_variable.possible_no:
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

else:
  print('Not a valid input.  Please enter \'yes\', or \'no\'')

# create binary search tree (root, and immediate child nodes)
root = definitions_class.Node(cast_type(data_root[0]))

for item in data_tree:
  root.insert(cast_type(item))

# return least common ancestor
lca = root.lca_algorithm(cast_type(data_lca[0]), cast_type(data_lca[1]), root)
print('least common ancestor: ', lca.data)

# print binary search tree
root.print_tree_breadth()
