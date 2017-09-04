#Python program to find the factorial of a given number

def fact(x):
    print("The factor of",x,"are:")
    for i in range(1, x+1):
        if x % i == 0:
            print(i)

n = int(input("Enter the number: "))

fact(n)
