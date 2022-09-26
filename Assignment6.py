#1 Positive or non positive.
'''
a=int(input("Enter a number : "))
if a>0:
    print("Positive!")
else:
    print("Non-Positive!")
'''
#2 Divisible by 5 or not.
'''
a=int(input("Enter a number : "))
print("Divisible by 5") if a%2==0 else print("Not Divisible by 5")
'''
#3 Even or Odd.
'''
a=int(input("Enter a number : "))
print("Even") if a%2==0 else print("Odd")
'''
#4 greater between two numbers.
'''
a=int(input("Enter a number : "))
b=int(input("Enter second number : "))
if a>b:
    print("The greater number is %d"%a)
elif b>a:
    print("The greater number is %d"%b)
elif a==b:
    print("Both the numbers entered are the same %d"%a)
'''
#5 print given words in dictonary order.
'''
a=input("Enter word one : ")
b=input("Enter word two : ")
if a>b:
    print("The word in alphabetic order is %s , %s"%(b,a))
else:
    print("The word in alphabetic order is %s , %s"%(a,b))
'''
#6 check whether a number is 3 digit or not
'''
a=int(input("Enter a number : "))
b=len(str(a))
if b==3:
    print("The number %d is a three digit number"%a)
else:
    print("The number %d is not a three digit number"%a)
'''
#7 Positive,negative or Zero.
'''
a=int(input("Enter a number : "))
if a>0:
    print("Positive!")
elif a<0:
    print("Negative!")
else:
    print("Zero!")
'''
#8 Quadratic equation roots.
'''
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == 0:
    print("Enter the coefficients correctly.")
else:
    d = b * b - 4 * a * c  
    sqr = math.sqrt(abs(d))  
      
    if d > 0:  
        print("Real and different roots ")  
        print((-b + sqr)/(2 * a))  
        print((-b - sqr)/(2 * a))  
      
    elif d == 0:  
        print("Real and same roots")  
        print(-b / (2 * a))  
      
    else: 
        print("Complex Roots exist.")  
        print(- b / (2 * a), " + i", sqr)  
        print(- b / (2 * a), " - i", sqr)
'''


#9 Leap year or not.
'''
a=int(input("Enter a year :"))
b=len(str(a))
if b==4:
    if a%4==0 & a%100 & a%400:
        print("%d is a Leap year"%a)
    else:
        print("%d is not a Leap year"%a)
else:
    print("Please enter a Valid Year!")
'''
#10 Greatest of three numbers.
'''
a=int(input("Enter a number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
if a>b & a>c:
    print("The greater number is %d"%a)
elif b>a & b>c:
    print("The greater number is %d"%b)
elif c>a & c>b:
    print("The greater number is %d"%c)
elif a==b==c:
    print("All three numbers are same %d"%a)
'''
#11  Show the number of days of the given month in numeric format
'''
a=int(input("Enter month in numeric format : "))
b=int(input("Enter the year : "))
if a==1 | a==3 | a==5 | a==7 | a==8 | a==10 | a==12:
    print("The nymber of days is 31!")
elif a==2:
    if b%4==0 & b%100==0 & b%400==0:
        print("The number of days is 29!")
    else:
        print("The number of days is 28!")
else:
    print("The number of days is 30!")
'''
