You are testing an experimental slot machine with multiple spinning number wheels that shift positions at random.  The wheel that was in position 1 in one turn may be in position 2 the next for example. To make it even more fun, the spinning wheels are not the same. Each wheel can have any number of stops from 1 to 9. If it has f stops, then its stops are numbered from 1 to f. After each spin, every wheel will show one stop number in the slot machine's window. You run a series of up to 50 test spins and write down all the digits visible in the window. Calculate the minimum number of stops on each of the wheels that can produce that particular series of results, then get their sum.

 

For example, spins on a three wheel slot machine are recorded as:

	7 1 2
	2 4 6
	3 6 5
	3 1 2
We see that the highest number of all is 7, so at least one wheel needs to have 7 stops. Since 7 is the highest value in any row, we can remove the highest value from each of the rows:

	1 2
	2 4
	3 5
	1 2
Now our highest value is 5, so the second wheel must have 5 stops. Our final wheel needs 3 stops. The total stops required are 7 + 5 + 3 = 15.

 

Function Description 

Complete the function slotGame in the editor below. The function must return an the integer sum of the minimum number of stops on the wheels.

 

slotGame has the following parameter(s):

    spins[spins[0],...spins[n-1]]:  an array of equal length strings of digits spun

 

Constraints:

1 ≤ |spins| ≤ 50
1 ≤ spins[i] ≤ 50
All spins[i] in a test case will be of equal length.
All characters in each spins[i] ∈ [0-9]
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array spins.

Each of the next n lines contains a string spins[i] where 0 ≤ i < n.

 

Sample Case 0
Sample Input 0    

4
137
364
115
724
Sample Output 0

14
 

Explanation 0

The numbers showing are:

1, 3 and 7 in the first spin

3, 6 and 4 in the second spin

1, 1 and 5 in the third spin

7, 2 and 4 in the fourth spin. 

There are three wheels on our slot machine. One wheel needs to have at least 7 stops to produce the first and the fourth spin. Another wheel needs to have at least 4 stops to produce the second and fourth spin. A third wheel needs at least 3 stops to produce the second spin. The answer is 7 + 4 + 3 = 14 minimum total stops across all the wheels.  Any fewer stops would have failed to give the results in the input.

 

Sample Case 1
Sample Input 1

4
1112
1111
1211
1111
Sample Output 1

5
Explanation 1

One wheel with 2 stops and three wheels with 1 stop each could produce the above results for a minimum total of 5 stops. 
 
