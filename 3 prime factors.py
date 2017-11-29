# find the prime factors

def isPrime(num):

    isP = True

    for i in range(2,10):
        if (num % i == 0 and num != i) or (num % 2 == 0):
            # print(i)
            isP = False

    return isP

# print(isPrime(13))
# print(2 % 4)
multiples = 1
number = int(input("Enter the number"))
for k in range(1,number):
    if number % k == 0 and isPrime(k):
        multiples *= k
        print(k)
    if multiples == number:
        break