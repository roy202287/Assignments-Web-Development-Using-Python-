#1 Write a python script to remove the last digit from a given number.
'''
a=int(input("Enter a number : "))
b=str(a)
print("The number is ", int(b[:-1]))
'''
#2 Write a python script to get the last digit from a given number.
'''
a=int(input("Enter a number:" ))
b=a%10
print("The last digit is : ",b)
'''


#3 Program to swap values of the variables
'''
a=5
b=6
print("The value of a is %d and b is %d"%(a,b))
print (id(a),id(b),sep='\n')
a=6
b=5
print("The updated value of a is %d and b is %d"%(a,b))
print(id(a),id(b),sep='\n')
'''
#4 Program to calculate x power y
'''
x=int(input("Number : "))
y=int(input("Power : "))
print("%d power of %d is %d"%(x,y,x**y))
'''
#5 Print 1st digit of three digit number
'''
n=int(input("Enter a three digit number : "))
ns=str(n)
n=len(ns)
if n==3:
    print ("The first digit is ",int(ns[0]))
else :
    print ("Please enter a three digit number")
'''
#6 Print middle digit of three digit number.
'''
n=int(input("Enter a three digit number : "))
ns=str(n)
n=len(ns)
if n==3:
    print ("The middle digit is ",int(ns[1]))
else :
    print ("Please enter a three digit number")
'''
#7 Print the last digit number.
'''
n=int(input("Enter a three digit number : "))
ns=str(n)
n=len(ns)
if n==3:
    print ("The last digit is ",int(ns[2]))
else :
    print ("Please enter a three digit number")
'''
#8 Script to use IN operator to show that a element is in the list
'''
e=eval(input("Enter a element : "))
l=[1,'name','age',456,'gender']
if e in l :
    print("The the element is in the list ")
else:
    print("The elemnt is not in the list")
'''
#9 Script to use NOTIN operator to show that a element is not in the list.
'''
e=eval(input("Enter a element : "))
l=[1,'name','age',456,'gender']
if e not in l :
    print("The the element is not in the list ")
else:
    print("The elemnt is in the list")
'''
#10 Script to use IS operator to check if two  variables are pointing to the same object.
'''
n1=eval(input("Enter a value : "))
n2=eval(input("Enter the same value again : "))
if n1 is n2:
    print(id(n1),id(n2),sep='\n')
else :
    print("Please enter the same value!")
'''