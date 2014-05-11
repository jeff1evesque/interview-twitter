Least Common Ancestor
=====================

I had an interactive interview with Twitter, and was given 15 minutes to write-up something that determined the least-common-ancestor for a binary search tree.  I am adjusting what I did for them -- but, feel free to use or improve what I have.

##Least Common Ancestor, written in Python

###Definition:

Suppose we let T be a rooted tree with n nodes. The lowest common ancestor between two nodes v and w is defined as the lowest node in T that has both v and w as descendants.

- http://en.wikipedia.org/wiki/Lowest_common_ancestor

###Overview:

This application will prompt users whether they want to input values interactively, or use default file to import values.  The default import file is currently called `input.txt`.

##Input file

The values in the `input.txt` file must follow a special format:

```
root = [7]
tree = [23, 1, 14, 53, 22]
lca = [14, 53]
```

where `root` must be a list containing just one value (root of the binary search tree), `tree` an unordered list of values (remaining part of the binary search tree), and `lca` which must only contain two node values that is defined within the tree (either the root, or a tree node value).

##Interactive input:

Note: when users elect to interactively input values, the first value inputted will be considered the root.  Thus, if users input the following:

```
Enter tree value (q - to quit): 3
Enter tree value (q - to quit): 55
Enter tree value (q - to quit): 2
Enter tree value (q - to quit): 3
Enter tree value (q - to quit): 30
Enter tree value (q - to quit): 100
Enter tree value (q - to quit): 45
Enter tree value (q - to quit): 1
Enter tree value (q - to quit): 43
Enter tree value (q - to quit): 48
Enter tree value (q - to quit): 25
Enter tree value (q - to quit): 21
Enter tree value (q - to quit): q
```

then, the binary tree will have a representation as follows:

```
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
```
