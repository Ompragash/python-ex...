#Python Program to check armstrong number in certain interval

lower = eval(input("Enter the lower range: "))

upper = eval(input("Enter the upper range: ")) 

for num in range(lower, upper + 1):

    #order of number
    order = len(str(num))

    #initialize sum
    sum = 0

    #find the sum of the cude of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
