#Integer 
a=5
#String
b="Tejas"
#Boolean 
c=False
#Float
d=5.63

#Print Data Types using input and if statements
question=input("Which of the following do you want to know the data type of?\n")
if question=="a":
    print(type(a))
elif question=="b":
    print(type(b))
elif question=="c":
    print(type(c))
elif question=="d":
    print(type(d))
else:
    print("Choose between a,b,c or d")

#Conversion of the above datatypes
a1=str(a)
b1=bool(b)
c1=int(c)
c2=str(c)
d1=str(d)