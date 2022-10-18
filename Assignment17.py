# Write a python program to store all the programming languages known to you using Set.
'''
string=input("Enter list of elements seperated by commas : ")
set1={ e for e in string.split(',')}
print(set1,type(set1))
'''
# Write a python program to store your own information {name, age, gender, so on..}
'''
s1={"Sourav",22,"Male"}
print(s1,type(s1))
'''
# Write a python script to get the data type of a Set.
'''
s1={"Sourav",22,"Male"}
print(s1,type(s1))
'''
# Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}
'''
thisset = {"Java","Python", "Django"}
if "Python" in thisset:
    print("The element is present")
else:
    print("The element is not present")
'''
# Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"},secondset= {"C", "Cpp", "NoSQL"}
'''
thisset = {"Java","Python", "Django"}
secondset= {"C", "Cpp", "NoSQL"}
print("Final set is ",thisset.union(secondset))
'''
# Write a python program to add elements of list to a set
'''
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)
print(thisset)
'''
# Write a python program to remove last item of the given set
'''
thisset = {"Python", "Django", "JavaScript", "SQL"}
print("The last elemeent of the listh that is removed is : ",thisset.pop())
'''
# Write a python program to delete the set completely.
'''
thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.clear()
print(thisset)
'''
# Write a python program to loop through the set and print values
'''
thisset = {"Python", "Django", "JavaScript", "SQL"}
for e in thisset:
    print(e)
'''
# Write a python program to find the maximum and minimum value in a set.
'''
thisset = {"Python", "Django", "JavaScript", "SQL"}
print(max(thisset),min(thisset))
'''