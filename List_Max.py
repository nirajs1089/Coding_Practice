In this challenge, you will start with an array initialized to zeros with indexes starting at 1.  You will then be given a series of operations to perform on segments of the list.  Each operation will consist of a starting and ending index within the array, and a number to add to each element within that range.

 

For example, start with an array of 5 elements: [0, 0, 0, 0, 0].  The variables a and b represent the starting and ending indexes inclusive.  Another variable k is the addend.  The first element is at index 1.

    a    b    k             list
                   [  0,  0,  0,  0,  0]
    1    2   10    [ 10, 10,  0,  0,  0]
    2    4    5    [ 10, 15,  5,  5,  0]
    3    5   12    [ 10, 15, 17, 17, 12]
 

The maximum value in the resultant array is 17. That is the value to be determined.

 

Note: Naive solutions will only pass the first few test cases. You must write an efficient solution if you wish to pass all test cases.

 

Function description 

Write a program to read inputs from stdin and perform the required operations. Print the largest value of the array after all operations have been performed.

 

Constraints

3 ≤ n ≤ 107
1 ≤ o ≤ 2 × 105
1 ≤ a ≤ b ≤ n
0 ≤ k ≤ 109
 

Input Format 
Input from stdin should be processed as follows and passed to the function.

 

The first line contains 2 space-separated integers, n and o: the size of your array and the number of operations

Each of the next o lines contains 3 space-separated integers, a, b and k: the starting index, ending index and value to add

Sample Case 0
Sample Input 0

5 3
1 2 100
2 5 100
3 4 100
 

Sample Output 0

200
 

Explanation 0

We perform the following sequence of o = 3 operations on list = [0, 0, 0, 0, 0]:

Add k = 100 to every element in the inclusive range [1, 2], resulting in list = [100, 100, 0, 0, 0].
Add k = 100 to every element in the inclusive range [2, 5], resulting in list = [100, 200, 100, 100, 100].
Add k = 100 to every element in the inclusive range [3, 4], resulting in list = [100, 200, 200, 200, 100].
We then print the maximum value in the final list, 200, as our answer.

Sample Case 1
Sample Input 1

4 3
2 3 603
1 1 286
4 4 882
 

Sample Output 1

882
 

Explanation 1

We perform the following sequence of o = 3 operations on list = [0, 0, 0, 0]:

Add k = 603 to every element in the inclusive range [2, 3], resulting in list = [0, 603, 603, 0].
Add k = 286 to every element in the inclusive range [1, 1], resulting in list = [286, 603, 603, 0].
Add k = 882 to every element in the inclusive range [4, 4], resulting in list = [286, 603, 603, 882].
We then print the maximum value in the final list, 882, as our answer.
