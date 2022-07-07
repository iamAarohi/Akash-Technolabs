#default arguments
#this function will print the sum of two numbers
#if the arguments are not supplied 
#o/w it will add the default value which is 
#intialized as parameters

def sum(a=10,b=20):
 sum=a+b
 print("The sum is : ",sum)

sum(20,30)
sum()