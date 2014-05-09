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
