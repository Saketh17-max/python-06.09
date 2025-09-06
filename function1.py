def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error"
    return a/b
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
print(addition(a,b),subtraction(a,b),multiply(a,b),divide(a,b))