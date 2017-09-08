#Python program to make a simple calculator

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("Select Operation.")
print("1.Add")
print("2.Subtrac")
print("3.Multiply")
print("4.Division")

choice = input("Enter the choice(1/2/3/4):")

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

if choice == '1':
    print(n1,'+',n2,'=', add(n1, n2))

elif choice == '2':
    print(n1,'-',n2,'=', sub(n1, n2))

elif choice == '3':
    print(n1,'*',n2,'=', mul(n1, n2))

elif choice == '4':
    print(n1,'/',n2,'=', div(n1, n2))

else:
    print("Invalid input")
