Psychometric testing is designed to find job-relevant information about an applicant that the traditional interview process wouldn't otherwise uncover. It typically includes a combination of online aptitude and personality tests that measure cognitive ability and personality traits.

 

A company has psychometric scores for n candidates, and it will only extend job offers to candidates with scores in the inclusive range given by [lowerLimit, upperLimit]. Given the list of scores and a sequence of score ranges, determine how many candidates the company will extend offers to for each range of scores.

 

Complete the jobOffers function in the editor below. It has three parameters:

 

An array of n integers, scores, denoting the list of candidate scores.
An array of q integers, lowerLimits, where each lowerLimitsi denotes the lowerLimit for score range i.
An array of q integers, upperLimits, where each upperLimitsi denotes the upperLimit for score range i.
 

The function must return an array of q integers where the value at each index i denotes the number of candidates in the inclusive range [lowerLimitsi, upperLimitsi] that the company will extend offers to.

 

Input Format

Locked stub code in the editor reads the following input from stdin and passes it to the function:

The first line contains an integer, n, denoting the number of elements in scores.

Each line j of the n subsequent lines (where 0 ≤ j < n) contains an integer describing scoresj.

The next line contains an integer, q, denoting the number of queries.

Each line i of the q subsequent lines (where 0 ≤ i < q) contains an integer describing lowerLimitsi.

The next line contains an integer, q, denoting the number of queries.

Each line i of the q subsequent lines (where 0 ≤ i < q) contains an integer describing upperLimitsi.

 

Constraints

1 ≤ n ≤ 105
1 ≤ scoresj ≤ 109
1 ≤ q ≤ 105
1 ≤ lowerLimitsi ≤ upperLimitsi ≤ 109
 

Output Format

The function must return an array of q integers where the value at each index i denotes the number of candidates in the inclusive range [lowerLimitsi, upperLimitsi] that the company will extend offers to.

 

Sample Input 0

5
1
3
5
6
8
1
2
1
6
 

Sample Output 0

3
 

Explanation 0

Given scores = [1, 3, 5, 6, 8], lowerLimits = [2], and upperLimits = [6], we perform the following q = 1 query:

 

Find all the scores in the inclusive range [2, 6]: there are three such candidates (i.e., scores 3, 5, and 6), so we store 3 in index 0 of our return array.
 

The function then returns the array [3].

 

Sample Input 1

3
4        
8
7
2
2
4
2
8
4
Sample Output 1

3
1
 

Explanation 1

Given scores = [4, 8, 7], lowerLimits = [2, 4], and upperLimits = [8, 4], we perform the following q = 2 queries:

 

Find all the scores in the inclusive range [2, 8]: there are three such candidates (i.e., scores 4, 7, and 8), so we store 3 in index 0 of our return array.
Find all the scores in the inclusive range [4, 4]: there is one such candidate (i.e., score 4), so we store 1 in index 1 of our return array.
 

The function then returns the array [3, 1].

 
