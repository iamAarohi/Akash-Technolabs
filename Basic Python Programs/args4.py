# variable legth -  keyword arguments

def fun(**args):
 for i,j in args.items():
     print(i,j)

fun(Name="Aarohi",Surname="Mistry")