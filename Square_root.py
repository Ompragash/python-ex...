#Find square root of real or complex numbers
#Import the complex math module

import cmath

num = 1+2j

# Uncomment to give the user input

# num  =  eval(input("Enter the number: "))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}'.format(num, num_sqrt.real,num_sqrt.imag))

#print("The square root of" num "is" num_sqrt)

