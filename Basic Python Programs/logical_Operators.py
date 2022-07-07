#logical Operators
#AND Operator

n1=int(input("Enter the first value:"))
n2=int(input("Enter the second value:"))
n3=int(input("Enter the Third value:"))

if n1>n2 and n1>n3:
    print(n1,"is the largest number")

if n2>n1 and n2>n3:
    print(n2,"is the largest number")

if n3>n2 and n3>n1:
    print(n3,"is the largest number")