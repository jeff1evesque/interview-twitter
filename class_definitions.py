'''
class-definitions.py

Jeffrey Levesque
05/09/2014

This file contains all the logic-component classes that get imported into the
least-common-ancester.py file.
'''

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

