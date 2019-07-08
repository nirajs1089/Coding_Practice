A line has formed to buy tickets for a concert.  In order to delay a shortage caused by brokers buying large blocks of tickets, venue management has decided to sell only one ticket at a time. Buyers have to wait through the line again if they want to buy more tickets.  Jesse is standing in line and has a number of tickets to purchase.

 

Given a list of ticket buyers with their numbers of desired tickets, determine how long it will take Jesse to purchase his tickets.  Jesse's position in line will be stated, and each transaction takes 1 unit of time.  For your purposes, no time is spent moving to the back of the line.

 

 

For example, if the zero indexed array of ticket requirements,  tickets = [1, 2, 5] , and Jesse's position p = 1, the first five seconds of ticket sales look like this:

Buying-Show-Tickets-PS1
Green denotes Jesse, and gray denotes a person that left the line.
Jesse finishes purchasing all tickets1 = 2 tickets at time t = 4.
 

Function Description 

Complete the function waitingTime in the editor below. The function must return an integer representing the units of time it takes Jesse to purchase his desired number of tickets.

 

waitingTime has the following parameter(s):

    tickets[tickets[0],...tickets[n-1]]:  an array of tickets desired by each person at position tickets[i]

    p: Jesse's position in line

 

Constraints

1 ≤ n ≤ 105
1 ≤ tickets[i] ≤ 109, where 0 ≤ i < n.
0 ≤ p < n
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array tickets.

The next n lines each contain an element tickets[i] where 0 ≤ i < n.

The next line contains an integer p, Jesse's position in line.

Sample Case 0
 

Sample Input 0

5
2
6
3
4
5
2
 

Sample Output 0

12
 

Explanation 0

Given tickets = [2, 6, 3, 4, 5], Jesse's position in line is marked in bold. His wait time looks like this:

window ← 2 ← 6 ← 3 ← 4 ← 5
window ← 6 ← 3 ← 4 ← 5 ← 1
window ← 3 ← 4 ← 5 ← 1 ← 5
window ← 4 ← 5 ← 1 ← 5 ← 2
window ← 5 ← 1 ← 5 ← 2 ← 3
window ← 1 ← 5 ← 2 ← 3 ← 4
window ← 5 ← 2 ← 3 ← 4 (the person at the head of the line in the previous step purchased their last ticket and does not re-enter the line)
window ← 2 ← 3 ← 4 ← 4
window ← 3 ← 4 ← 4 ← 1
window ← 4 ← 4 ← 1 ← 2
window ← 4 ← 1 ← 2 ← 3
window ← 1 ← 2 ← 3 ← 3
window ← 2 ← 3 ← 3 (Jesse purchased his last ticket and does not re-enter the line)
It took a total of 12 units of time to purchase 2 tickets.

Sample Case 1
Sample Input 1

4
1
1
1
1
0
 

Sample Output 1

1
 

Explanation 1

Given tickets = [1, 1, 1, 1], Jesse's wait time looks like this:

window ← 1 ← 1 ← 1 ← 1
window ← 1 ← 1 ← 1 (Jesse purchased his ticket and does not re-enter the line)
It took a total of 1 unit of time to purchase 1 ticket.

Sample Case 2
Sample Input 2

4
5
5
2
3
3
 

Sample Output 2

11
 

Explanation 2

Given tickets = [5, 5, 2, 3], Jesse's wait time looks like this:

window ← 5 ← 5 ← 2 ← 3
window ← 5 ← 2 ← 3 ← 4
window ← 2 ← 3 ← 4 ← 4
window ← 3 ← 4 ← 4 ← 1
window ← 4 ← 4 ← 1 ← 2
window ← 4 ← 1 ← 2 ← 3
window ← 1 ← 2 ← 3 ← 3
window ← 2 ← 3 ← 3 (the person at the head of the line in the previous step purchased their last ticket and does not re-enter the line)
window ← 3 ← 3 ← 1
window ← 3 ← 1 ← 2
window ← 1 ← 2 ← 2
window ← 2 ← 2 (Jesse purchased his last ticket and does not re-enter the line)
It took a total of 11 units of time to purchase 3 tickets.
