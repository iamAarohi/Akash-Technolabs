#takes value from user

d1={}
num=int(input("Enter the number of elements:"))

for i in range(0,num):
 a,b=input("Enter Key Value Pair Data: ").split()
 d1[a]=[b]

print(d1)