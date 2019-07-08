Given an array, you must increment any duplicate elements until all its elements are unique. In addition, the sum of its elements must be the minimum possible within the rules. For example, if arr = [3, 2, 1, 2, 7], then arrunique = [3, 2, 1, 4, 7] and its elements sum to a minimal value of 3 + 2 + 1 + 4 + 7 = 17.

 

Function Description

Complete the getMinimumUniqueSum function in the editor below to create an array of unique elements with a minimal sum. Return the integer sum of the resulting array.

 

getMinimumUniqueSum has the following parameter(s):

    arr:  an array of integers to process

 

 

Constraints

1 ≤ n ≤ 2000
1 ≤ arr[i] ≤ 3000 where 0 ≤ i < n
Input Format For Custom Testing
Input from stdin will be processed as follows and passed to the function:

 

The first line contains an integer, n, denoting size of array arr.

Each of the next n lines contains an integer describing element arr[i] where 0 ≤ i < n.

Sample Case 0
Sample Input 0

3
1
2
2
 

Sample Output 0

6
 

Explanation 0

arr = [1, 2, 2]

The duplicate array elements 2 must be addressed. The minimum unique array will be achieved by incrementing one of the twos by 1, creating the array [1, 2, 3]. The sum of elements in the new array is 1 + 2 + 3 = 6.

Sample Case 1
Sample Input 1

3
1
2
3
 

Sample Output 1

6
 

Explanation 1

arr = [1, 2, 3]

Each number in arr is unique, so we do not need to modify any of its elements (i.e., arr ≡ arrunique). We return the sum of all elements in the array, which is 1 + 2 + 3 = 6.

Sample Case 2
Sample Input 2

4
2
2
4
5
 

Sample Output 2

14
 

Explanation 2

arr = [2, 2, 4, 5]

Because arr[0] and arr[1] are duplicates, we increment one of the two elements to 3. When we do this, we get arrunique = [2, 3, 4, 5].

The sum of these elements is 2 + 3 + 4 + 5 = 14.
