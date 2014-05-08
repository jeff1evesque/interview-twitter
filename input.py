# input.py file is used to generate the binary tree 

'''
The following commands

root = Node(3)

tree = BinarySearchTree(root)

tree.add(55)
tree.add(2)
tree.add(3)
tree.add(30)
tree.add(100)
tree.add(45)
tree.add(1)
tree.add(43)
tree.add(48)
tree.add(25)
tree.add(21)

generates a tree structure as follows

                 3
                / \
               /   \
              /     \
             2      55
            / \    /  \
           1   3  30   100
                 /  \
               25   45
               /   /  \
             21   43   48
'''

root = Node(7)

tree = BinarySearchTree(root)

tree.add(23)
tree.add(1)
tree.add(14)
tree.add(53)
tree.add(22)
