#list(Take value from user)

#creating an empty list
lst=[]

#number of element as input
num=int(input("Enter the number of elements ="))

#iterating till the range
for i in range(0,num):
 ele=input("Enter value: ")

 #adding the element
 lst.append(ele)

 #print the list
print(lst)