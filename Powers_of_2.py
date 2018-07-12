In this challenge, we want to determine if a given integer is a power of 2. For example, 20 = 1, 22 = 4, and 25 = 32 are powers of 2 but 5, 6, and 9 are not.

 

You will be given a list of integers to test named nums. Create a return array where each element of the array result[i] is a 1 if nums[i] is a power of 2. Otherwise, it should be a 0.

 

For example, if nums = [1,7,8,129], then result = [1 0 1 0]. That's 20 and 23 marked as true. Neither 7 nor 129 is a power of 2.

 

Function Description 

Complete the function isPowerOf2 in the editor below. The function must return an array of binary integers where each index i contains a 1 if nums[i] is a power of 2 or a 0 if it is not.

 

isPowerOf2 has the following parameter(s):

    nums[nums[0],...nums[n-1]]:  an array of integers

 

Constraints

1 ≤ n ≤ 100
0 ≤ nums[i] ≤ 5 × 107
 

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

 

The first line contains an integer n, the size of the array nums.

Each of the next n lines contains an integer nums[i] where 0 ≤ i < n.

 

Sample Case 0
Sample Input 0

3
2
3
4
Sample Output 0

1
0
1
Explanation 0

We evaluate the following n = 3 integers in nums = [2, 3, 4]:

nums0 = 2 = 21, so the answer for this index is 1.
nums1 = 3 is not a power of 2, so the answer for this index is 0.
nums2 = 4 = 22, so the answer for this index is 1.
We then return the array [1, 0, 1] as our answer.

Sample Case 1
Sample Input 1

3
1024
2048
1048576
Sample Output 1

1
1
1
Explanation 1

We evaluate the following n = 3 integers in nums = [1024, 2048, 1048576]:

nums0 = 1024 = 210, so the answer for this index is 1.
nums1 = 2048 = 211, so the answer for this index is 1.
nums2 = 1048576 = 220, so the answer for this index is 1.
We then return the array [1, 1, 1] as our answer.
