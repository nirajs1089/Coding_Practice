A core meltdown just happened at a local nuclear plant! They need to move all of their rods to lead isolation chambers using specialized, radiation hardened robots. There is a cost of moving the rods associated with the square root of the number of rods lifted. Lifting four rods costs twice the cost of lifting two rods because 41/2 = 2 and 11/2 = 1. Any remaining fraction, such as 31/2 ≈ 1.732 is raised to the next integer, i.e. ceiling(31/2) = 2.

 

In this challenge, you will be given a list of fused pairs of nuclear fuel rods. Once you have determined all of the fused groups, calculate the total cost of moving the rods to isolation.

 

For example, assume you have 10 fuel rods labeled 1 - 10. Pairs of rods are [1, 3], [1, 4] and [2, 6]. There are two groups of fused rods: {1, 3, 4} and {2, 6}. The first group costs ceiling(31/2) = 2 units to move. The second costs ceiling(21/2) = 2 units. The remaining 5 rods each cost ceiling(11/2) = 1 unit to move giving us a total of 2 + 2 + 5 = 9 units cost.

 

Function Description 

Complete the function minimalCost in the editor below. The function must return an integer denoting the cost of isolating all of the rods.

 

minimalCost has the following parameter(s):

    n: the number of rods

    pairs[pairs[1],...pairs[m]]:  an array of space-separated integer pairs denoting fused rod numbers, p and q

 

Constraints

2 ≤ n ≤ 105
1 ≤ m ≤ 105
1 ≤ p, q ≤ n
p ≠ q
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array a.

The next line contains an integer m, the size of the array pairs.

Each of the next m lines contains a string of two space-separated integers pairs[i] where 1 ≤ i ≤ m.

Sample Case 0
Sample Input 0

4
2
1 2
1 4
 

Sample Output 0

3
 

Explanation 0

 

The following arguments are passed to the function:

n = 4
pairs = [ [1 2], [1 4] ]
The diagram below depicts the configuration of rods:



 

The cost for removing each group is as follows:

Set {1, 2, 4}: c = ceil(sqrt(3)) = 2
Set {3}: c = ceil(sqrt(1)) = 1
 

When we sum all values of c, we get 2 + 1 = 3 as our answer.

 

Sample Case 1
Sample Input 1

8
4
8 1
5 8
7 3
8 6
 

Sample Output 1

6
 

Explanation 1

 

The following arguments are passed to the function:

n = 8
pairs = [ [8 1], [5 8], [7 3], [8 6] ]
The diagram below depicts the configuration of rods:



 

The cost for removing each group is as follows:

Set {2}: c = ceil(sqrt(1)) = 1
Set {4}: c = ceil(sqrt(1)) = 1
Set {1, 5, 6, 8}: c = ceil(sqrt(4)) = 2
Set {3, 7}: c = ceil(sqrt(2)) = 2
 

When we sum all values of c, we get 1 + 1 + 2 + 2 = 6 as our answer.
