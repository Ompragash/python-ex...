#Python program to check whether the program is prime number or not

num = int(input("Enter the number: "))

if num > 1:

    for i in range(2, num):
        if (num%i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")

else:
    print(num,"is not a prime number")
