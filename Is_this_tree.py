You are given a binary tree as a sequence of parent-child pairs. For example, the tree represented by the node pairs below:

(A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)
 

may be illustrated in many ways, with two possible representations below:

 

     

 

Below is the recursive definition for the S-expression of a tree:

 

S-exp(node) = ( node->val (S-exp(node->first_child))(S-exp(node->second_child))), if node != NULL = "", node == NULL
 

where, first_child->val < second_child->val (lexicographically smaller)

 

 

This tree can be represented in a S-expression in multiple ways. The lexicographically smallest way of expressing this is as follows:

(A(B(D)(G))(C(E(F))(H)))
 

Translate the node-pair representation into its lexicographically smallest S-expression or report any errors that do not conform to the definition of a binary tree.

 

The list of errors with their codes is as follows:

 

Error Code      Type of error

E1                 More than 2 children

E2                 Duplicate Edges

E3                 Cycle present

E4                 Multiple roots

E5                 Any other error   

 

Function Description 

Complete the function SExpression in the editor below. The function must return either the lexicographically lowest S-expression or the lexicographically lowest error code as a string.

 

SExpression has the following parameter(s):

    nodes:  a string of space-separated parentheticals, each containing the names of two connected nodes separated by a comma

 

Constraints:
 

All node names are single characters in the range ascii[A-Z]
The maximum node count is 26.
There is no specific sequence in which the input (parent,child) pairs are represented.
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains a string nodes.

 

Sample Case 0
Sample Input 0

(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)
 

Sample Output 0

 

(A(B(D(E(G))))(C(F)))
 

Explanation 0

A representation of the tree is as follows:

 



Sample Case 1
Sample Input 1

(A,B) (A,C) (B,D) (D,C)
 

Sample Output 1

E3
 

Explanation 1

 



Node D is both a child of B and a parent of C, but C and B are both child nodes of A. Since D tries to attach itself as parent to a node already above it in the tree, this forms a cycle.
