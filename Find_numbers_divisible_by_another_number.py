#Python program to find the numbers divisible by another number

my_list = [12, 65, 54, 39, 102, 339, 221,]
 
oops = int(input("Enter the number: "))

result = list(filter(lambda x: (x % oops == 0), my_list))

print("The result is",result)


