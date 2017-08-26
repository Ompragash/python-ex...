''' Python program to find the
multiplication table(1, 10)'''

num = eval(input("Display multiplication table of? "))

for i in range(1, 11):
    print(num , 'x' ,i, '=' ,num*i)
