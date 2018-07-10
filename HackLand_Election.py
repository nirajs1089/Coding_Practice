In elections that use the ballot box system for voting, each voter writes the name of a candidate on a ballot and places it in the ballot box. The candidate with the highest number of votes wins the election. If two or more candidates have the same number of votes, then the tied candidates' names are ordered alphabetically and the last name in the alphabetical order wins.

 

For example, votes are in the names ['Joe', 'Mary', 'Mary', 'Joe']. Each candidate received two votes, but Mary is alphabetically later than Joe, so she wins.

 

Function Description 

Complete the function electionWinner in the editor below. The function must return a string denoting the name of the winning candidate.

 

electionWinner has the following parameter(s):

    votes[votes[0],...votes[n-1]]:  an array of strings representing the names of the candidates as voted by the ith voter.

 

Constraints

1 ≤ n ≤ 104
 

Input Format For Custom Testing
Sample Case 0
Sample Input 0

10
Alex
Michael
Harry
Dave
Michael
Victor
Harry
Alex
Mary
Mary
Sample Output 0

Michael
Explanation 0

The votes tally is:

2 votes: Alex, Harry, Michael, Mary
1 vote: Dave, Victor
The highest vote count is 2, and among those receiving 2 votes, the last name alphabetically is Michael

Sample Case 1
Sample Input 1

10
Victor
Veronica
Ryan
Dave
Maria
Maria
Farah
Farah
Ryan
Veronica
Sample Output 1

Veronica
Explanation 1

The votes tally is:

2 votes: Farah, Maria, Ryan, Veronica
1 vote: Dave, Victor
The highest vote count is 2, and among those receiving 2 votes, the last name alphabetically is Veronica
