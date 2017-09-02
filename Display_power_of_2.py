#Python program to display the power of 2 using anonymous function

term = int(input("How many terms? "))
result = list(map(lambda x:2 ** x, range(term)))

print("The total terms is:",term)
for i in range(term):
    print("2 raised to power", i,"is",result[i])

