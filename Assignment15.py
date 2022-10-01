#Write a python script to create a String in 3 different possible ways
'''
s1="String"
s2=str("String123")
s3="""String"""
print(type(s1),type(s2),type(s3),s1,s2,s3,sep=' ')
'''
#Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
'''
s1="iNeuron"
print(s1[0:6:1])
'''
#Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
'''
s2="Hello Learners"
print(s2[2:6:1])
'''
#Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
'''
a="Learning"
b="Python"
l1=[a,b] #packing 
print(' '.join(l1)) #using join attribute of str class
'''
#Write a python script to get the count of total number of characters in String a=“iNeuron”
'''
a="iNeuron"
print(len(a))
'''
#Write a python script to reverse a String. (“iNeuron”)
'''
a="iNeuron"
print(a[::-1]) #if beg and end value is not specified it will take the first and last value respectively.
'''
#Write a python script to determine whether a string contains a specific substring.
'''
n=input("Enter a string : ")
n1=input("Enter a substring : ")
if n1 in n:
    print("The substring {} is in the string {}".format(n1,n))
else:
    print("The substring {} is not in the string {}".format(n1,n))
'''
#Write a python script to check if a string contains only numbers.
'''
n=input("Enter a numeric string : ")
if n.isdigit() == True:
    print("The string {} only contains number".format(n))
else:
    print("The string {} does not only contains number".format(n))
'''
#Write a python script to check if a string contains only characters of the alphabet.
'''
n=input("Enter a numeric string : ")
if n.isalpha() == True:
    print("The string {} only contains alphabet".format(n))
else:
    print("The string {} does not only contains alphabet".format(n))
'''
#Write a python script to convert an integer to a string.
'''
n=int(input('Enter a number : '))
s=str(n)
print(s,type(s))
'''