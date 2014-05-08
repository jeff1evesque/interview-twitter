'''
least-common-ancestor.py

Jeffrey Levesque
05/08/2014

Receives input data from input.py in order to generate a binary tree.  Then,
prompts users for two nodes in order to determine a least common ancestor.
'''

# location of input file
filename = 'input.py'

# read data from input.py file
with open(filename) as f:
  print(f.readlines())

if __name__ == '__main__':
  print('hi')
