#Pyhton program to check the armstrong number

num = eval(input("Enter the number: "))

sum =0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

#Display thr result

if num == sum:
    print(num,"is an armstrong number.")

else:
    print(num,"is not an armstrong number.")
