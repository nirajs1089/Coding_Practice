Gandalf has challenged his old friend and new enemy Merlin to a duel at a place of Merlin's choosing. Merlin decides the best place to be is behind a lot of minor wizards that Gandalf will have to fight first. As each minor wizard is encountered, he will fight and lose power. Along the path, he also may find power packs. Given that his power must never drop below 1, what is the minimum power he must start out with so he can get to the duel?

 

For example, his path is described as p = [-2, 3, 1, -5] where a negative number represents an opponent and a positive value is a power pack. When he fights an opponent, his power drops by the absolute value of the opponent's value. When he picks up a power pack, his power is boosted by the value. The following shows Gandalf's energy level if he starts with 4 units of power.

Gandalf's   Enemy
Power       or boost
---------   --------
4           -2
2            3
5            1
6           -5
1
 

Function Description 

Complete the function minPower in the editor below. The function must return the minimum integer energy value Gandalf needs when he starts out.

 

minPower has the following parameter(s):

    p[p[0],...p[n-1]]:  an array of integers

 

Constraints

1 ≤ n ≤ 105
−100 ≤ p[i] ≤ 100
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array p.

Each of the next n lines contains an integer p[i].

 

Sample Case 0
Sample Input 0

10
-5
4
-2
3
1
-1
-6
-1
0
5
 

Sample Output 0

8
 

Explanation 0

Gandalf's   Enemy
Power       or boost
---------   --------
8           -5
3            4
7           -2
5            3
8            1
9           -1
8           -6
2           -1
1            0
1            5
6
Gandalf's minimum power level is 1.

Sample Case 1
Sample Input 1

5
-5
4
-2
3
1
 

Sample Output 1

6
 

Explanation 1

 

Gandalf's   Enemy
Power       or boost
---------   --------
6           -5
1            4
5           -2
3            3
4            1
5           
Sample Case 2
Sample Input 2

10
-5
4
-2
3
1
-1
-6
-1
0
-5
 

Sample Output 2

13
 

Explanation 2

 

Gandalf's   Enemy
Power       or boost
---------   --------
13          -5
8            4
12          -2
10           3
13           1
14          -1
13          -6
7           -1
6            0
6           -5
1
