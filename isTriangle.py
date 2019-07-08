Mary has three sticks and wants to determine whether she can use them to form a non-degenerate triangle.  That is, the three can be laid tip-to-tip to form a triangle with non-zero angles at each intersection.  For instance, sticks of lengths [3, 4, 5] will make a non-degenerate triangle while [1, 1, 5] will not.

Function Description

Complete the function triangleOrNot in the editor below. The function must return an array of n strings where the value at each index i is Yes if ai, bi, and ci can form a non-degenerate triangle; otherwise, it's No.

 

triangleOrNot has the following parameter(s):

    a[a[0],...a[n-1]]:  array of n integers where each index i describes the length of side a for triangle i

    b[b[0],...b[n-1]]:  array of n integers representing lengths of sides bi

    c[c[0],...c[n-1]]:  array of n integers representing lengths of sides ci

Constraints

1 ≤ n ≤ 105
1 ≤ a[i], b[i], c[i] ≤ 103 , where 0 ≤ i < n
Input Format For Custom Testing
Locked stub code reads input from stdin and passes it to the function.

 

The first line contains an integer, n, denoting the number of elements in a.

Each of the next n lines contains an integer a[i].

The next line contains an integer, n, denoting the number of elements in b.

Each of the next n lines contains an integer b[i].

The next line contains an integer, n, denoting the number of elements in c.

Each of the next n lines contains an integer c[i].

 
 

Sample Case 0
Sample Input 0

3
7
10
7
3
2
3
4
3
2
7
4
Sample Output 0

No
No
Yes
Explanation 0

We want to check the following n = 3 possible triangles using the values given by a = [7, 10, 7], b = [2, 3, 4], and c = [2, 7, 4]:

a[0] = 7, b[0] = 2, and c[0] = 2 don't form a valid, non-degenerate triangle, so we store No in index 0 of our return array.
a[1] = 10, b[1] = 3, and c[1] = 7 don't form a valid, non-degenerate triangle, so we store No in index 1 of our return array.
a[2]= 7, b[2]= 4, and c[2] = 4 do form a valid, non-degenerate triangle, so we store Yes in index 2 of our return array.
We then return the array ["No", "No", "Yes"] as our answer.
