Two pairs of integers (a, b) and (c, d) are considered distinct if at least one element of (a, b) ∉ (c, d). For example given a list (1, 2, 2, 3), (1, 2) is distinct from (1, 3) and (2, 3) but not from (1, 2) with 2 chosen from a different index in the list. A pair is valid if a ≤ b.

 

You will be given an integer k and a list of integers. Count the number of distinct valid pairs of integers (a, b) in the list for which a + k = b.

 

For example, the array [1, 1, 1, 2] has two different valid pairs: (1, 1) and (1, 2). Note that the three possible instances of pair (1, 1) count as a single valid pair, as do the three possible instances of pair (1, 2). If k = 1, then this means we have a total of 1 valid pair which satisfies a + k = b ⇒ 1 + 1 = 2, the pair (1, 2).

 

Function Description 

Complete the function countPairs in the editor below. The function must return an integer denoting the count of valid (a, b) pairs in the numbers array that have a difference of k.

 

countPairs has the following parameter(s):

    numbers[numbers[0],...numbers[n-1]]:  an array of integers

    k: an integer

 

Constraints

2 ≤ n ≤ 2 × 105
0 ≤ numbers[i] ≤ 109, where 0 ≤ i < n
0 ≤ k ≤ 109
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array numbers.

Each of the next n lines contains an integer numbers[i] where 0 ≤ i < n.

The next line contains an integer k.

Sample Case 0
Sample Input 0

6
1
1
2
2
3
3
1
Sample Output 0

2
Explanation 0

There two valid pairs in [1, 1, 2, 2, 3, 3] that have a difference of k = 1:

(1, 2)
(2, 3)
Sample Case 1
Sample Input 1

6
1
2
3
4
5
6
2
Sample Output 1

4
Explanation 1

There are four valid pairs in [1, 2, 3, 4, 5, 6] that have a difference of k = 2:

(1, 3)
(2, 4)
(3, 5)
(4, 6)
Sample Case 2
Sample Input 2

6
1
2
5
6
9
10
2
Sample Output 2

0
Explanation 2

No valid (a, b) pair exists in [1, 2, 5, 6, 9, 10] that satisfies b − a = k = 2, so the function returns 0.
