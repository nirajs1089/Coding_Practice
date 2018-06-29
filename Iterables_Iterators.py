#
# Sample Input
#
# 4
# a a c d
# 2
# Sample Output
#
# 0.8333
# Explanation
#
# All possible unordered tuples of length  comprising of indices from  to  are:
#
#
# Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.
#
# Hence, the answer is .



import itertools as iter

# print(list(iter.combinations('1234',2)))


# gives non duplicate combinations Nc2 for a sequence
comb = list(iter.combinations('1234',2))
total_len = len(comb)

str_lst = ['a','a','c','d']
idx_lst = []
cntr = 0


for i in range(len(str_lst)):
    if str_lst[i] == 'a':
        idx_lst.append(str(i+1))


for c in comb:
    status = False
    for i in idx_lst:
        if i in list(c):
            status = True

    if status == True:
        cntr += 1


print(cntr/total_len)
