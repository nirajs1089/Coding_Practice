You will be given a list of points described by their (x,y) coordinates on a two dimensional plane. You must construct a square surrounding at least a given number of points within the area enclosed. That area should be minimal and the square must meet the following conditions:

The x-coordinates and y-coordinates of the points should be integers.
The sides of the square should be parallel to coordinate axes.
At least k of the given n points should lie strictly inside the square drawn. By strictly inside, we mean that they cannot lie on a side of the square.
 

For example, given n=3 points (1,1), (1,2) and (2,1) and k=3, we want to surround all three points. The minimum area square is 9 units, going from the origin (0,0), to (3,3).

 



 

Function Description 

Complete the function minArea in the editor below. The function must return the minimum possible area of the square satisfying the constraints as an integer.

 

minArea has the following parameter(s):

    x[x[0],...x[n-1]]:  an array of integer x coordinates

    y[y[0],...y[n-1]]:  an array of integer y coordinates

    k:  an integer, the minimum number of points to surround

 

Constraints
 

2 ≤ n ≤ 100
-109 ≤ x[i],y[i] ≤ 109
1 ≤ k ≤ n
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array x.

Each of the next n lines contains an integer x[i] where 0 ≤ i < n.

The next line contains the integer n, the size of the array y.

Each of the next n lines contains an integer y[i] where 0 ≤ i < n.

The last line contains the integer k.

 

Sample Case 0
Sample Input 0

2
0
2
2
0
4
2
Sample Output 0

36
 

Explanation 0

The given points are:

(0, 0)
(2, 4)
Now we can choose following four points:

(-1, -1)
(-1, 5)
(5, 5)
(5, -1)
Thus we draw a square of side six, satisfying the three constraints given in the problem statement and the area of the square is possible minimum.

 



 

So, the function returns 36, as the area of the square is side x side (6 x 6 = 36).

 

Sample Case 1
Sample Input 1

2
0
3
2
0
7
2
 

Sample Output 1

81
 

Explanation 1

The given points are:

(0, 0)
(2, 7)
Now we can choose following four points:

(-1, -1)
(-1, 8)
(8, 8)
(8, -1)
Thus we draw a square of side nine, satisfying the three constraints given in the problem statement and the area of the square is possible minimum. So the function returns 81 (9 x 9).
