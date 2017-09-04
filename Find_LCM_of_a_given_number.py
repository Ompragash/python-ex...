#Python program to find LCM of two given number

def lcm(x, y):

    if x > y:
        greater = x
    else: 
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)) :
            lcm = greater
            break
        greater += 1

    return lcm

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("The L.C.M of",n1,"and",n2,"is",lcm(n1, n2))
