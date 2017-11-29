

def isPalindrome(num):
    isP = False
    # num = 123321
    if len(str(num)) % 2 == 0:
        lst = [str(num)[i] for i in range(0,len(str(num)))]
        # print(sorted(lst))
        # print(lst[-1])
        #
        isP = True

        for i in range(0,len(str(num))//2):
            if int(lst[i]) != int(lst[-(i+1)]):
                isP = False

    return isP

ans = []

for frst in range(100,1000):
    for scnd in range(100, 1000):
        prod = frst * scnd
        if isPalindrome(prod):
            ans.append(prod)

print(sorted(ans)[-1])






