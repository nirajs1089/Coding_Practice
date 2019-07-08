You are working on a computer simulation of a mobile robot. The robot moves on an infinite plane, starting from position (0, 0). Its movements are described by a command string consisting of one or more of the following three letters:

G instructs the robot to move forward one step.
L instructs the robot to turn left.
R instructs the robot to turn right.
 

The robot performs the instructions in a command sequence in an infinite loop. You want to know whether or not there exists some circle such that the robot always moves within the circle and never leaves it.

 

Consider the commands R and G executed infinitely.  A diagram of the robot's movement looks like:

 

RG → RG

↑           ↓

RG ← RG

 

The robot will never leave the circle.

 

Function Description 

Complete the function doesCircleExist in the editor below. The function must return an array of n strings either YES or NO based on whether the robot is bound within a circle or not, in order of test results.

 

doesCircleExist has the following parameter(s):

    commands[commands0,...commandsn-1]:  An array of n commandsi where each represents a list of commands to test.

 

Constraints

1 ≤ |commands[i]| ≤ 2500
1 ≤ n ≤ 10
Each command consists of G, L, and R only.
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the number of elements in commands.

The next n lines each contain a string describing commands[i] where 0 ≤ i < n.

 

Sample Case 0
Sample Input 0

2

G

L

 

Sample Output 0

NO
YES
 

Explanation 0

We must consider the following n = 2 commands:

 

For commands[0] = "G", the robot will move forward forever ( G → G → G →... ) without ever turning or being restricted to a circle. Thus, we set index 0 of our return array to NO.
For commands[1] = "L", the robot will just turn 90 degrees left forever without ever moving forward (because there is no "G" instruction). The robot is effectively trapped at one spot, thus bound within a circle. We set index 1 of our return array to YES .
 

Sample Case 1
Sample Input 0

1
GRGL
 

Sample Output 1

NO
 

Explanation 1

Let's consider the robot's initial orientation to be facing north toward the positive y-axis. The robot performs the following four steps in a loop:

Go forward one step. The robot moves from (0, 0) to (0, 1).
Turn right. The robot turns eastward, facing the positive x-axis.
Go forward one step. The robot moves from (0, 1) to (1, 1).
Turn left. The robot turns northward, facing the positive y-axis again.  
                          ↑

             RG → LG

             ↑

RG → LG

↑

G

The robot then repeats these steps infinitely, following an endless zig-zagging path in the northeastern direction. Because the robot will never turn in such a way that it would be restricted to a circle, we set index 0 of our return array to NO.
