
def getSmallestM(num):

    check = 1
    isDivByAll = False

    while not isDivByAll:
        for i in range(1,int(num)+1):
            if check % i == 0:
                isDivByAll = True
            else:
                isDivByAll = False
                check += 1
                break

    return check

print(getSmallestM(20))



