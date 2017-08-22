
x = eval(input("Enter the value of x: "))

y = eval(input("Enter the value of y: "))

temp = x
x = y
y = temp

print("The value of x is after swapping: {}".format(x))
print("The value of y is after swapping: {}".format(y))
