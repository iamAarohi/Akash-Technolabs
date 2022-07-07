#no argument with multiple return type

def my_fun():
    name="Aarohi Mistry"
    contact="9537612871"
    email="aarohimistry814@gmail.com"
    return name,contact,email

name,contact,email=my_fun()
print("The name is: ",name)
print("The contact number is: ",contact)
print("The email is: ",email)