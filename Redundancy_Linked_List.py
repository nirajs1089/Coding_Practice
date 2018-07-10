We define a redundant node in a singly-linked list to be a node whose value matches the value of a previous node in the list. In other words, an earlier value recurs.

 

For example, consider the following linked list with one redundant node:

 

PS Example
A zero-indexed list in the form list = [3, 4, 3, 6] with a redundant node at index 2.
 

You will be given a reference to the head of a singly-linked list that may contain redundant nodes. You must create a singly-linked list containing only unique values as they first occur in the inputs.

 

Function Description 

Complete the function distinct in the editor below. The function must return a LinkedListNode which is the first node of a list that contains only the non-redundant nodes from the original list in the order encountered.

 

distinct has the following parameter(s):

    head:  the LinkedListNode which is the head of a singly-linked list of integers

 

Note:. A LinkedListNode has two attributes: val, an integer, and next, a reference to the next item in the list or the language equivalent of null at the tail.

 

Constraints

1 ≤ n ≤ 105
0 ≤ d[i] ≤ 1000
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array list.

Each of the next n lines contains an integer list[i] where 0 ≤ i < n.

Sample Case 0
Sample Input 0

8
3
4
3
2
6
1
2
6
Sample Output 0

3
4
2
6
1
Explanation 0
image
The list head = 3 → 4 → 3 → 2 → 6 → 1 → 2 → 6 → null looks like this:

Sample Case Initial
The linked list given as input.
From the diagram, we conclude the following:

list[2] = 3 is redundant to list[0] = 3
list[6] = 2 is redundant to list[3] = 2
list[7] = 6 is redundant to list[4] = 6
After removing all the redundant nodes, the list looks like this:

Sample Case Reduced
The reduced list.
We then return a LinkedListNode referencing head = 3 → 4 → 2 → 6 → 1 → null.
