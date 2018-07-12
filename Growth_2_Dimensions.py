You'll start with an infinite two dimensional grid filled with zeros indexed from (1,1) at the bottom left corner. Given a series of coordinates (i, j), add 1 to each element in the range from (1,1) to (i,j). Once you have processed all coordinates, determine how many cells contain the maximal value in the grid.

For example, upRight = [(1,4), (2,3), (4,1)]. The following diagrams show each iteration starting at zero. We see that the maximal value in the grid is 3. We return 1, the number of occurrences of 3.

 


 

 

Function Description 

Complete the function countMax in the editor below. The function must return the long integer count of the occurrences of the grid's maximal element.

 

countMax has the following parameter(s):

    topRight[topRight[0],...topRight[n-1]]:  an array of strings made of two space-separated integers, i and j.

 

Constraints

1 ≤ n ≤ 100
1 ≤ r, c ≤ 106
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array topRight.

Each of the next n lines contains a string of two space-separated integers, topRight[i].

 

Sample Case 0
Sample Input

3
2 3
3 7
4 1
Sample Output

2
Explanation

Given steps = ["2 3", "3 7", "4 1"]:

 

Sample 0
The portion of the infinite grid corresponding to cells (i, j) where 1 ≤ i ≤ 4 and 1 ≤ j ≤ 7
After performing all n = 3 steps, the maximum x value in any cell is 3. Because there are two such cells with this maximal value, we return 2 as our answer.
