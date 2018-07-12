Sarah loves to go to Zillycakes to buy cupcakes. They are running a promotion that gives a customer a free cupcake after they collect enough wrappers from previous purchases. Determine the maximum number of cupcakes Sarah can enjoy.

 

She starts with a budget of n dollars. Each cupcake costs c dollars. The promotion provides 1 free cupcake for every m wrappers collected.

 

For example, Sarah starts with n=4 dollars to buy cupcakes at c=1 dollar each. The number of wrappers for an award is m=2. She buys 4 cupcakes, turns in those 4 wrappers for 2 more cupcakes. She turns in those 2 wrappers for another cupcake. At this point, her snacking ends. She only has one wrapper, but she has enjoyed 7 cupcakes.

 

Function Description 

Complete the function maximumCupcakes in the editor below. For each test case the function must print an integer, the maximum cupcakes Sarah can eat, on a new line.

 

maximumCupcakes has the following parameter(s):

    n:  an integer, Sarah's starting budget

    c:  an integer, the cost of a cupcake

    m:  an integer, the number of wrappers required for a free cupcake

 

Constraints

1 ≤ t ≤ 103
2 ≤ n ≤ 105
1 ≤ c ≤ n
2 ≤ m ≤ n
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer t, the number of test cases.

Each of the next t lines contains three space-separated integers, n, c, and m.

Sample Case 0
Sample Input 0

3
10 2 5
12 4 4
6 2 2
 

Sample Output 0

6
3
5
 

Explanation 0

 

There are 3 test cases:

Spend 10 dollars on 5 cupcakes at 2 dollars. Turn in 5 wrappers for another cupcake.
Spend 12 dollars on 3 cupcakes at 4 dollars. There aren't enough wrappers to turn in.
Spend 6 dollars on 3 cupcakes at 2 dollars. Turn in 2 of her wrappers for her 4th cupcake, leaving 1 old and one new wrapper. turn those 2 wrappers in for 1 more cupcake.
Sample Case 1
Sample Input 1

2
8 4 2
7 2 3
 

Sample Output 1

3
4
 

Explanation 1

 

There are 2 test cases:

Spend 8 dollars on 2 cupcakes at 4 dollars. Turn in 2 wrappers for another cupcake.
Spend 6 dollars on 3 cupcakes at 2 dollars. Turn in 3 wrappers for another cupcake. A dollar is left over.
