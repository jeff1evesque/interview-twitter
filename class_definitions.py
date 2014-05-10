'''
class_definitions.py

Jeffrey Levesque
05/09/2014

This file contains all the logic-component classes that get imported into the
least-common-ancester.py file.
'''

class Node:
  """ 
  Tree Node: contains three attributes left node, right node, and data
  """

  left = None
  right = None
  data = None

  def __init__(self, d=None, l=None, r=None):
    """
    Constructor
    """

    self.left = l
    self.right = r
    self.data = d

  def insert(self, data):
    """
    Insert new node with data into tree
    """

    if data < self.data:
      if self.left is None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    else:
      if self.right is None:
        self.right = Node(data)
      else:
        self.right.insert(data)

  def print_tree_breadth(self):
    """
    Print tree using breadth-first recursion
    """

    if self.left:
      self.left.print_tree_breadth()
    print self.data
    if self.right:
      self.right.print_tree_breadth()

  def lca_algorithm(self, value1, value2, root):
    """
    Given two nodes, determine the least common ancestor
    """

    node = root
    ancestor = node

    #print('hi', node.data)

    while node != None:
      if value1 < node.data and value2 > node.data:
        ancestor = node
        break
      elif value1 == node.data or value2 == node.data:
        break
      elif value1 < node.data and value2 < node.data:
        ancestor = node.data
        node = node.left
      elif value1 > node.data and value2 > node.data:
        ancestor = node.data
        node = node.right

    # root node is empty
    return ancestor
