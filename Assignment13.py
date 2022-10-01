# Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
'''
l=["Java","Python","SQL","C"]
for i in l:
        print(i,end=' ')

print()     
print("The Length of the list is",len(l))
'''
# Write a python script to get the data type of a list.
'''
l=["Java","Python","SQL","C"]
print(type(l))
'''

# Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
'''
mylist = ["Java", "C", "Python"]
print("The last element of the list is ",mylist[-1])
'''
# Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
'''
thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
print("Initial list is",thislist)
thislist[1],thislist[3]="NoSQL","Flutter"
print("The list after substitution" ,thislist)
'''
# Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"])
'''
mylist = ["Java", "SQL", "C", "Reactnative"]
print("Initial list : ", mylist)
mylist.append("Python")
print("Final list : ",mylist)
'''
# Write a python program to append elements from another list to the current list.
'''
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
thirdlist= firstlist+secondlist #concatenation of lists using '+' operator.
print(type(thirdlist))
print("Resultant list is : ",thirdlist)
'''
# Write a python program to Print all items by referring to their index number.
'''
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
n=len(thislist)
for i in range(0,n,1):
        a=i
        print("Element: ",thislist[i], "\n" "Index number : ",a)
'''
'''
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
print(thislist[0],thislist[1],thislist[2],thislist[3],thislist[4],thislist[5],sep='\n')
'''
# Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
'''
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
print("Before sorting : ",thislist)
thislist.sort() #list object attribute
print("after sorting : ",thislist)
'''
# Write a Python script to create a list of city names taken from the user.
'''
l=eval(input("Enter list of cities : ")) # DOUBT
for i in l:
        print(i,end=' ')
'''
# Write a Python script to create a list, where each element of the list is a digit of a given number.
'''
n=input("Enter a number : ")
l=list(n)
print(l)
'''
