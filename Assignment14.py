#Write a Python script to create a list of first N natural numbers.
'''
#Use case- input:5,Output:[1,2,3,4,5]
n=int(input("Enter number of elements : "))
l1=list(range(1,n+1,1))
print(l1)
'''

#Write a Python script to create a list of first N odd natural numbers.
'''
#usecase - input:5,output:[1,3,5,7,9]
n=int(input("Enter number of elements : "))
l1=list(range(1,2*n+1,2))
print(l1)
'''
#Write a Python script to create a list of first N even natural numbers.
'''
#usecase - input:5,output:[2,4,6,8,10]
n=int(input("Enter number of elements : "))
l1=list(range(2,(2*n)+2,2))
print(l1)
'''

#Write a Python script to find the greatest number in a given list of numbers.
'''
s=input("Enter a list of numbers seperated by commas : ")
l1=s.split(',')
l2=[int (e) for e in l1]
print("The greatest among the list is : ",max(l2))
'''
#Write a Python script to find the smallest number in a given list of numbers.
'''
s=input("Enter a list of numbers seperated by commas : ")
l1=s.split(',')
l2=[int (e) for e in l1]
print("The smallest among the list is : ",min(l2))
'''
#Write a Python script to calculate the sum of elements in a given list of numbers.
'''
s=input("Enter a list of numbers seperated by commas : ")
l1=s.split(',')
l2=[int (e) for e in l1]
print("The sum of the elements are : ",sum(l2))
'''
#Write a Python script to remove all non int values from a list.
'''
s=input("Enter elements seperated by comma : ")
l1=s.split(',')
l2=[eval(e) for e in l1]
l3=[]
for i in l2:
    if type(i)==int:
        l3.append(i)
print(l3)
'''
#Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
'''
s=input("Enter elements seperated by comma : ")
l1=s.split(',')
l2=[eval(e) for e in l1]
s=0
for i in l2:
    s=l2.count(i)
    print(i,s,sep=' ')
'''
#Write a Python script to print indices of all occurrences of a given element in a given list.

'''
my_list = [1, 5, 3, 1, 5, 4]
item = 5
 
indices = [i for i in range(len(my_list)) if my_list[i] == item]
 
print(indices)
'''











