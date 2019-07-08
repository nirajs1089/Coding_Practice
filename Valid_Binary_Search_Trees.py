A binary tree is a multi-node data structure where each node has, at most, two child nodes and one stored value. It may either be:

An empty tree, where the root is null.
A tree with a non-null root node that contains a value and two subtrees, left and right, which are also binary trees.
 

A binary tree is a binary search tree (BST) if all the non-null nodes exhibit two properties:

Each node's left subtree contains only values that are lower than its own stored value.
Each node's right subtree contains only values that are higher than its own stored value.
 

A pre-order traversal is a tree traversal method where the current node is visited first, then the left subtree, and then the right subtree. The following pseudocode parses a tree into a list using pre-order traversal:

If the root is null, output the null list.
For a non-null node:
Make a list, left, by pre-order traversing the left subtree.
Make a list, right, by pre-order traversing the right subtree.
Output the stored value of the non-null node, append left to it, then append right to the result.
For more detail, see the diagram in the Explanation section below.

 

You have to write a program to test whether a traversal history could describe a path on a valid BST. For each query, it should print YES on a new line if the path could be in a valid BST, or NO if it could not.

 

Constraints

1 ≤ q ≤ 10
1 ≤ n ≤ 100
 

 

Input Format
The following parameters must be read from stdin:

 

The first line contains an integer q, the number of queries a.

The next q sets of lines are defined as:

    The first line contains an integer n, the number of nodes in the tree.

    The next line contains a[a[0],...a[n-1]]:  a list of space-separated integers describing values encountered in the traversal of a tree

Sample Case 0
Sample Input 0

5
3
1 3 2
3
2 1 3
6
3 2 1 5 4 6
4
1 3 4 2
5
3 4 5 1 2
 

Sample Output 0

YES
YES
YES
NO
NO
 

Explanation 0

The diagram below depicts the test for a valid binary search tree for the five queries. Figures (d) and (e) do not represent a valid BST.



 

We perform the following q = 5 queries:

Diagram (a)'s pre-order traversal matches the pre-order traversal in the first query, 1 3 2, so we print YES on a new line to indicate that the traversal matches a valid BST.
Diagram (b)'s pre-order traversal matches the pre-order traversal in the second query, 2 1 3, so we print YES on a new line to indicate that the traversal matches a valid BST.
Diagram (c)'s pre-order traversal matches the pre-order traversal in the first query, 3 2 1 5 4 6, so we print YES on a new line to indicate that the traversal matches a valid BST.
The fourth query, 1 3 4 2, is not a pre-order traversal of a binary search tree. We know that the root is 1 because that is the first value in the list. For the second value to be 3, it must be the right child of 1. For the third value to be 4, it must be the right child of 3. For 2 to be the last value in the traversal, it would have to be the left child of 4; however, this would break the order property of a binary search tree because a value less than 3 would be in 3's right subtree. Thus, we print NO on a new line.
The fifth quer
