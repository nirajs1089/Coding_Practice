
# You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.
# 
# image
# 
# Note that  is indexed from  to , where  is the number of attributes.
# 
# Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.
# 
# Input Format
# 
# The first line contains  and  separated by a space.
# The next  lines each contain  elements.
# The last line contains .
# 
# Constraints
# 
# 
# 
# Each element
# 
# Output Format
# 
# Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
# 
# Sample Input 0
# 
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
# Sample Output 0
# 
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
# Explanation 0
# 
# The details are sorted based on the second attribute, since  is zero- indexed.
import math

file_lst1 = []
file_lst2 = []
with open('./athlete_sort.txt',mode='r') as sort_file:
    file_lst1 = sort_file.readlines()
    # m = list(map(int, str(row).split(sep=' ')))

#columns

m = list(map(int,str(file_lst1[0]).split(sep=' ')))[1]

for i in range(1,len(file_lst1)-1):
        file_lst2.append(list(map(int,str(file_lst1[i]).split(sep=' '))))


k = int(file_lst1[-1])


arr = file_lst2
# lst = ['2','1','9','3','2']
# arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
# lst = list(map(int,lst))
# print(lst)
# m = 3 # columns
# k =1 # sort index
dict = {}
non_key_list = []
ky = 0.0
dec = 0.01

for rw in arr:
    for cl in range(m):
        if cl == k:
            ky = rw[cl]
        else:
            non_key_list.append(rw[cl])

    if ky in list(dict.keys()):
        ky += dec
        dec += 0.01

    dict[ky] = non_key_list.copy()

    non_key_list.clear()

print(dict)
sorted_list = sorted(dict.items(),key=lambda x: (x[0],x[1]))
print(sorted_list)

final_matrix = []


for key,v in sorted_list:

    temp = list(v).copy()
    temp.insert(k,math.floor(key))

    for x in temp:
        print("{} ".format(x),end=' ')
    print(end='\n')

