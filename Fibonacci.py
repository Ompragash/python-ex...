#Python program to find the fibonacci of a given number

nterm = eval(input("Enter the number: "))

a, b = 0, 1

if nterm <= 0:
    print("Please enter a positive number")

elif nterm == 1:
    print("Fibonacci sequence upto",nterm,":")
    print(a)

else:
    print("Fibonacci sequence upto",nterm,":")
    while a < nterm:
        print(a,end=' ')
        nth = a + b

        a, b = b, a+b
