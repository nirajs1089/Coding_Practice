
Consider a pair of integers, Consider a (a, b). We can perform the following operations on (a, b) in any order, zero or more times:

 

(a, b) → (a + b, b)
(a, b) → (a, a + b)
 

For example, you can start with (1, 4), perform the operation (1 + 4, 4) to get (5, 4), perform the operation (5, 5 + 4) to get (5, 9), and perform the operation (5, 5 + 9) to get (5, 14). You could also start with (1, 1+4) to get (1,5) and so on.

 

Function Description 

Complete the function isPossible in the editor below. The function must return a string denoting whether or not you can convert (a, b) to (c, d) by performing zero or more of the operations specified above. If it is possible, return the string Yes. Otherwise, return No.

 

isPossible has the following parameter(s):

    a:  an integer

    b:  an integer

    c:  an integer

    d:  an integer

 

Constraints

1 ≤ a, b, c, d ≤ 1000
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer a.

The next line contains an integer b.

The next line contains an integer c.

The next line contains an integer d.

Sample Case 0
Sample Input 0

1
4
5
9
 

Sample Output 0

Yes
 

Explanation 0

We can convert (1, 4) to (5, 9) by performing the following sequence of operations: (1, 4) → (5, 4) → (5, 9).

 

Sample Case 1
Sample Input 1

1
2
3
6
 

Sample Output 1

No
 

Explanation 1

If we tried the operation (1, 2) → (3, 2), we can successfully match c = 3 but no subsequent possible operation will ever get us to d = 6. The only other option for our first operation is (1, 2) → (1, 3); we could certainly perform subsequent operations to get us to d = 6 but no operation would ever get us to c = 3 because any value added to a after this first operation would result in an a > c. We return No as our answer.
