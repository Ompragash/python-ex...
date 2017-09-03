#Python Program to find H.C.F of a given number

def compute(x, y):
    if x < y:
        smaller = x
    else:
        smaller = y

    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("The H.C.F of a given number",n1,"and",n2,"is",compute(n1, n2))
