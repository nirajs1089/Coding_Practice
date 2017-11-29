# print fibonacci numbers and find the sun of even numbers

limit = 4000000

prev = 1
next = 2
sum  = 0
even_sum = 0

print("{},{}".format(prev,next),end=',')
while sum < limit:
    sum = prev + next
    if sum % 2 == 0:
        even_sum += sum
    print("{}".format(sum),end=',')
    prev = next
    next = sum

print("even ",even_sum+2)