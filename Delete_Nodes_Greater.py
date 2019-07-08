In this challenge, you will be given a singly-linked list of integers and a single integer to compare to. You must remove any values greater than that single integer value, maintaining the integrity and order of the list. You will return a pointer to the head of new list which will be printed by the code that is supplied.

 

For example, if you are given the list of integers [100, 105, 50] and a maximum value of 100, you would only insert 100 and 50 into your list, with 100 as the list head.

 

Function Description 

Complete the function removeNodes in the editor below. The function must return a reference to the root node of your list.

 

removeNodes has the following parameter(s):

    listHead:  a reference to the root node of the singly-linked list

    x:  integer, the maximum value to be included in new list

 

Constraints

1 ≤ n, x ≤ 105
1 ≤ Linked list node values ≤ 105
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the number of nodes in the linked list.

The next n lines each contain an element to insert into your linked list.

The last line contains x, the maximum value allowable in your linked list.

Sample Case 0
Sample Input 0

5
1
2
3
4
5
3
 

Sample Output 0

1
2
3
 

Explanation 0 

n = 5, x = 3

list = 1 → 2 → 3 → 4 → 5

After removing the nodes having value > 3, list = 1 → 2 → 3.

Sample Case 1
Sample Input 1

5
5
2
1
6
7
5
 

Sample Output 1

5
2
1
 

Explanation 1

n = 5, x = 5

list = 5 → 2 → 1 → 6 → 7.

After removing the nodes having value > 5, list = 5 → 2 → 1.
