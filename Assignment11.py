#Write a python script to calculate sum of first N natural numbers
'''
n=int(input("Enter a number :"))
i=0
a=0
while i<=n:
    a=a+i
    i=i+1
print('Sum is %d'%a)
'''
#Write a python script to calculate sum of squares of first N natural numbers
'''
n=int(input("Enter a number :"))
i=0
a=0
while i<=n:
    a=(a+(i**2))
    i=i+1
print('Sum is %d'%a)
'''
#Write a python script to calculate sum of cubes of first N natural numbers
'''
n=int(input("Enter a number : "))
sum=0
i=0
while i<=n:
    sum=(sum+(i**3))
    i+=1
print("Sum of cubes of first %d natural number is %d" %(n,sum))
'''
#Write a python script to calculate sum of first N odd natural numbers
'''
n=int(input("Enter a number : "))
i=0
sum=0
while i<=n:
    if i%2 != 0:
        sum=sum+i
    i=i+1
print("Sum of first odd %d natural numbers is %d"%(n,sum))
'''
#Write a python script to calculate sum of first N even natural numbers
'''
n=int(input("Enter a number : "))
i=0
sum=0
while i<=n:
    if i%2 == 0:
        sum=sum+i
    i=i+1
print("Sum of first %d even natural numbers is %d"%(n,sum))
'''
#Write a python script to calculate factorial of a given number
'''
n=int(input("Enter a number : "))
fact=1
for i in range(1,n+1,1):
    if n==1:
        fact=0
        fact=fact*i
    else:
        fact=fact*i
print("Factorial of %d is %d."%(n,fact))
''' 

#Write a python script to count digits in a given number
'''
n=int(input("Enter a number : "))
count=0
while n>0:
    count=count+1
    n=n//10
print(count)
'''
'''
n=int(input("Enter a number : "))
n1=str(n)
print("The number of digit is",len(n1))
'''
#Write a python script to calculate sum of digits of a given number
'''
n=input("Enter a number : ")
s=0
for i in n:
    s=s+int(i)
print(s)
'''
#Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
'''
n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")
'''
# Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
'''
decimal = int(input("Enter a decimal number: "))
octal = 0
ctr = 0
temp = decimal
while(temp > 0):
    octal += ((temp%8)*(10**ctr)) 
    temp = int(temp/8)             
    ctr += 1
       
print("Octal of {x} is: {y}".format(x=decimal,y=octal))
'''