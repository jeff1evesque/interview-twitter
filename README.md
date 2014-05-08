least-common-ancestor
=====================

Least Common Ancestor, written in Python

input.py contains the file that will be consumed by the least-common-ancestor.py file.  It has the following syntax:

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

It must define each 'root', and 'tree' only once -- but, can define as many nodes (tree.add()) we wish.  The above series of commands will generate a tree structure as follows:

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

