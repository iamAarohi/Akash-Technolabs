# variable legth - non keyword arguments

def add(*num):
    sum = 0

    for i in num:
        sum = sum + i
    print("Sum is : ", sum)


add(20, 30)
add(50, 60, 70)
