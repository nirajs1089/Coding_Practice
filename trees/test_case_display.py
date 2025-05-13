from BinaryTree import *
from TreeNode import *

input_trees = [
    [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(350)],
    [TreeNode(100), TreeNode(200), TreeNode(75), TreeNode(50), TreeNode(25), TreeNode(350)],
    [TreeNode(200), TreeNode(350), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(200), TreeNode(25)],
    [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(200), TreeNode(350)],
    [TreeNode(350), TreeNode(75), TreeNode(25), TreeNode(200), TreeNode(50), TreeNode(100)],
    [TreeNode(1), None, TreeNode(2), None, TreeNode(3), None, TreeNode(4), None, TreeNode(5)]
]

indx = 1
for i in input_trees:
    tree = BinaryTree(i)

    print(indx, ".\tBinary Tree:", sep="")
    indx += 1
    if tree.root is None:
        display_tree(None)
    else:
        display_tree(tree.root)
