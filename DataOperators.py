import random
random_number=float(random.randint(1,10))
print(random_number)

#Input numbers
a=int(input("Enter a number\n"))
b=int(input("Enter another number\n"))

#Arithmatic Operators
c=float(a+b)
d=float(a*b)
e=float(a-b)
f=float(a/b)

#Logical Operators 
def gate(element):
    question=input("Choose between AND or OR\n").lower()
    if question == "and":
        if element and random_number >=25:
            print("Both the numbers are greater than 25")
        else:
            print("Either one number or both the numbers are lesser than 25")
    elif question == "or":
        if element or random_number >=25:
            print("Either of the two numbers are greater than 25")
        else:
            print("Both are lesser than 25")

#Print the results
g=input("What do you want to do?\n Add=Addition, Sub=Subtraction, Mul=Multiplication or Div=Division\n").lower()
if g=="add":
    print(c)
    gate(c)
elif g=="sub":
    print(e)
    gate(e)
elif g=="mul":
    print(d)
    gate(d)
elif g=="div":
    print(f)
    gate(f)
    