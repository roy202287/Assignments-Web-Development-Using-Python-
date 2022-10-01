#Print MysirG n times.
'''
n=int(input("Enter no. of times to be printed: "))
for i in range(1,n+1,1):
    print("MysirG",end='\n')
'''
#Print first n natural numbers
'''
n=int(input("Enter the value of n : "))
for i in range(1,n+1,1):
    print(i,end=' ')
'''
#Print first n natural numbers in reverse order.
'''
n=int(input("Enter the value of n : "))
for i in range(n,0,-1):
    print(i,end=' ')
'''
#Print first n odd natural numbers.
'''
n=int(input("Enter the value of n : "))
for i in range(1,((2*n)),2): #in the ending values substitute with Sum of odd number AP
    print(i,end=' ')
'''
#Print first n odd natural numbers in reverse order.
'''
n=int(input("Enter the value of n : "))
for i in range(((2*n)-1),0,-2):
    print(i,end=' ')
'''
#Print first n even natural numbers.
'''
n=int(input("Enter the value of n : "))
for i in range(2,(2*n)+1,2):
    print(i,end=' ')
'''
#Print first n even natural numbers in reverse order.
'''
n=int(input("Enter the value of n : "))
for i in range((2*n),1,-2):
    print(i,end=' ')
'''
#Print the squares of first n natural numbers.
'''
n=int(input("Enter the value of n : "))
for i in range(1,n+1,1):
    print((i**2),end=' ')
'''
#Print the cubes of first n natural numbers.
'''
n=int(input("Enter the value of n : "))
for i in range(1,n+1,1):
    print((i**3),end = ' ')
'''
#Print first 10 multiples of n.
'''
n=int(input("Enter the value of n : "))
for i in range(1,(10*(n+1)),1): #for multiples of n multiply by 10 then check.
    if i%n == 0:
        print(i,end=' ')
'''
    