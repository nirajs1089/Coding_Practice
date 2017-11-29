

# Get the sum of multiples of 3 and 5 within a range

lower_no = int(input("Enter the lower number"))
upper_no = int(input("Enter the upper number"))
upper_range = int(input("Enter the range"))

#get a var to get the sum

sum = 0

#run a loop for the range

for i in range(upper_range):
    print(i)
    if i % lower_no == 0 or i % upper_no == 0:
        sum += i

print(sum)
