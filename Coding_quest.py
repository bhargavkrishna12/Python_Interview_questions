# # Reverse a string:
# # Write a function that takes a string as input and returns the string in reverse order.

# # Example:
# # Input: "Hello"
# # Output: "olleH"

# def reverse_string(string):
#     return string[::-1]
# print(reverse_string('Hello'))

# # Find the factorial of a number:
# # Write a function that takes an integer as input and returns its factorial.

# # Example:
# # Input: 5
# # Output: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
#     return fact
# print(factorial(5))


# # Check if a string is a palindrome:
# # Write a function that takes a string as input and returns True if it is a palindrome, and False otherwise.

# # Example:
# # Input: "racecar"
# # Output: True

# def ply_string(string):
#     if string == string[::-1]:
#         return True
#     else:
#         return False
# print(ply_string("racecar"))

# # Find the common elements in two lists:
# # Write a function that takes two lists as input and returns a list of common elements between the two.

# # Example:
# # Input: [1, 2, 3, 4], [3, 4, 5, 6]
# # Output: [3, 4]

# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# list3 = []
# for i in list1:
#     if i in list2:
#         list3.append(i)
# print(list3)

# # Count the frequency of each element in a list:
# # Write a function that takes a list as input and returns a dictionary with the frequency of each element.

# # Example:
# # Input: [1, 2, 2, 3, 3, 3]
# # Output: {1: 1, 2: 2, 3: 3}

# list1 = [1,2,2,3,3,3]

# d = {}
# for i in list1:
#     d[i]=list1.count(i)
# print(d)

# d = {}
# for i in list1:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# d={}
# for i in list1:
#     d[i]=list1.count(i)
#     a=d.keys()
#     b=d.values()
# c=list(a)
# e=list(b)
# print(list(zip(c,e)))

# # Implement a stack using a list:
# # Write a class that implements a stack data structure using a list (or array) in Python.
# # It should have push(), pop(), and is_empty() methods.

# class Stack:
#     def __init__(self):
#         self.stack =[]
#     def push(self,item):
#         self.stack.append(item)
#     def pop(self):
#         if self.is_empty():
#             raise IndexError('Stack is Empty')
#         return self.stack.pop()
#     def is_empty(self):
#         return len(self.stack)==0
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.pop())
# print(stack.pop())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.is_empty())

# # Check if two strings are anagrams:
# # Write a function that takes two strings as input and returns True if they are anagrams (contain the same characters in any order), and False otherwise.

# # Example:
# # Input: "listen", "silent"
# # Output: True

# str1 = "listen"
# str2 = "silent"

# if sorted(str1)==sorted(str2):
#     print("True")
# else:
#     print("False")


# # Python program to display all the prime numbers within an interval

# lower = 900
# upper = 1000

# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)

# # Python program to check whther the number is prime or not.

# num = 29
# for i in range(2,num):
#     if num%i==0:
#         print('Not a prime number')
#         break
# else:
#     print('Prime')


# # Reverse a string

# string = "Ojas Innovative Technlgies"

# s = ''
# for i in string:
#     s=i+s
# print(s)


# # sort the array without builtin methods

# array = [1,-1,90,3,2,0,45,25,12,78,37]

# for i in range(len(array)):
#     for j in range(len(array)):
#         if array[i]<array[j]:
#             array[i],array[j]=array[j],array[i]

# print(array)

# # Recursive function

# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(5))

# #Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

# string = input('Enter a string:')
# if len(string)>=2 and string[:2]=='Is':
#     print(string) 
# print('Is'+string)

# # Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

# def sum(x,y,z):
#     sum = x+y+z
#     if x==y==z:
#         sum = sum*3
#     return sum
# print(sum(1,2,3))
# print(sum(3,3,3))


# #  Write a Python program to test whether a number is within 100 of 1000 or 2000

# num = 101

# for i in range(1,1000):
#     if num==i:
#         print('number found')
#         break
# else:
#     print('number not found')

# # Write a Python program to calculate number of days between two dates.

# from datetime import date
# x = date(2023,2,13)
# y = date(2022,3,15)
# print(x-y)

# # Write a Python program to print the calendar of a given month and year.

# import calendar
# year = 2023
# month = 5
# print(calendar.month(year,month))

# # Write a Python program to accept a filename from the user and print the extension of that.
# file_name = input("Enter any file name with extensin :")
# get_extensin = file_name.split(".")
# print(get_extensin[-1])

# # Ternary Operator
# x = 10
# y = 20
# print(x if x>y else y) 

# # python program to write arrange the string in order format.
# dic = {1:"Hello prasad",2:"hi",3:"Wel come to Cisco network"} 

# for i in dic.keys():
#     for j in dic.keys():
#         if len(dic[i])<=len(dic[j]):
#             dic[i],dic[j]=dic[j],dic[i]
# print(dic)

# # print all letters except c an t

# string = "copyassignment"
# for i in string:
#     if i=="c" or i=="t":
#         continue
#     else:
#         print(i)


# # find the number which consists of 1
# lst=[11,12,34,111,112]
# for i in lst:
#     if str(i).startswith("1"):
#         print(i)

# # count the Repeated words from the string
# string = 'ojas innovative ojas innovative'

# d = {}
# for i in string.split():
#     d[i]=string.count(i)
# print(d)


# # Python program to find the unique elements and count.

# a="abcdabcdbb"

# s = ""
# count=1
# for i in a:
#     if i not in s:
#         s+=i
#         count+=1
# print(s,count)

# # add the value t dict
# dictt = {'one':1,'two':2,'three':3}

# for i in dictt.keys():
#   dictt[i]=dictt[i]+1
# print(dictt)

# # find the highest number
# def highest_num(x,y,z):
#   if x>y and x>z:
#     print('x is highest number')
#   elif y>z:
#     print('y is highest number')
#   else:
#     print('z is highest number')
# highest_num(10,20,30)

# # split the list
# string = 'ojas innovative technologies'.split()
# print(string)
# print(' '.join(string))

# # Default string arguments 
# string = "{} {} and {}".format('ojas','innovative','tech')
# print(string)

# # positional string arguments 
# string = "{0} {1} and {2}".format('ojas','innovative','tech')
# print(string)

# # keyword arguments
# string = "{a} {b} and {c}".format(a='ojas',b='innovative',c='tech')
# print(string)

# # polyndrme
# num = int(input('Enter any number:'))
# temp = num
# rev = 0
# while temp>0:
#   dig = temp%10
#   rev = rev*10+dig
#   temp = temp//10
# if num == rev:
#   print('Polyndrome')
# else:
#   print('Not a Polyndrome')

# # Armstrong in python

# num = int(input('Enter any number:'))
# temp = num
# rev = 0
# while temp>0:
#   dig = temp%10
#   rev = rev+dig**4
#   temp = temp//10
# if num == rev:
#   print('armstrong')
# else:
#   print('Not a armstrong')


# # Django ORM queries

# # How to get all records from table
# #---------student.objects.all()

# # Retrieving single objects from Querysets

# #---------students.objects.get(pk=1)

# # fetch mobile Number
# #----------students.objects.get(mobile=90000000000)

# # filtering the records
# # students.objects.filter(first_name__startswith="R")
# # students.objects.filter(last_name__endswith="H")

# # using exclude method
# # students.objects.exclude(first_name__startswith="R")

# # How to make OR queries in Django ORM?
# # students.objects.filter(first_name__startswith='R') or students.objects.filter(first_name__startswith='R')
# # students.objects.filter(first_name__startswith='R') and students.objects.filter(first_name__startswith='R')
# #Creating Multiple Object in one shot
# # Student.objects.all().count()
# # students.objects.all()[:4]
# # Students.Objects.all()[1:6]

# #How to Order a querysets in asending or descending order?
# # Students.objects.all().order_by('mobile')
# # Students.objects.all().order_by('-mobile')


# # what is class?
# # --->> class is a cllection of objects.it is a logical entity that contains attributes and methods.

# # --->> object is an instance of a class

# # Inheritance 
# # --->> one class acquires the properties from another class
# # --->> we have diffrent types of inheritances such as 1.single inheritance
# #                                                      2.Multiple Inheritance
# #                                                      3.Multilevel Inheritance
# #                                                      4.hierarchial Inheritance
# #                                                      5.Hybrid Inheritance.



# Gather the all names in one list and all integers in one list.
# array = [{'name':'tejesh','age':28},{'name':'bhargav','age':27},{'name':'pavan','age':29}]

# result = {}
# for item in array:                                  
#     for key, value in item.items():                                                               
#         if key in result:                                        
#             result[key].append(value)
#         else:
#             result[key] = [value]
# print(result)


# Inheritance
# class first:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name,self.age)
# class second(first):
#     def get_methd(self):
#         print(self.name,self.age)
# obj = second('bhargav',23)
# obj1 = first('venkat',27)
# obj.get_methd()
# obj1.display()

# Method Overriding
# --->>> it means it has two different classes but only have same method is called Inheritance.
# class Bhargav:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
#     def display(self):
#         print(f'my name is {self.name} and age is {self.age}')
# class Man(Bhargav):
#     def display(self):
#          print("Hello")

# obj = Man('bhargav',23)
# obj.display()

# Super() methd is used to acceses the properties from parent class to child.
# class Bhargav:
#     def display(self):
#         print("Gd Mrning")
# class Man(Bhargav):
#     def display_sign(self):
#          super().display()
#          print("Hello")

# obj = Man()
# obj.display_sign()


# Given a list of integers, write a Python function to find the maximum product of any three numbers from the list.

# Example: Input: [1, 2, 3, 4, 5], Output: 60 (4 * 5 * 3)

li = [1,3,4,7,5,2,]
def max_prod_num(li):
    li.sort()
    return li[-1]*li[-2]*li[-3]
print(max_prod_num(li))

# Given a matrix represented as a 2D list of integers, write a Python function to rotate the matrix by 90 degrees clockwise.

# Example: Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]], Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
def rotate_matrix(matrix):
    length_of_matrix = len(matrix)
    for i in range(length_of_matrix):
        for j in range(i+1,length_of_matrix):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(length_of_matrix):
        matrix[i]=matrix[i][::-1]
    return matrix
print(rotate_matrix(matrix))


# Implement a Python class for a stack that supports the following operations: push, pop, and get_min (to retrieve the minimum element in O(1) time complexity).

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        self.stack.pop()
    # def get_min(self):
    #     self.stack.min()
obj = Stack()
obj.push(1)
obj.push(2)
obj.push(3)

# print(obj.pop())
# print(obj.get_min())


# Given two sorted lists of integers, write a Python function to merge them into a single sorted list.
# Example: Input: [1, 3, 5], [2, 4, 6], Output: [1, 2, 3, 4, 5, 6]

li1 = [1,3,5]
li2 = [2,4,6]
print(li1+li2)


# Implement a Python function to calculate the factorial of a given number recursively.

# Example: Input: 5, Output: 120 (5!)
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

string = "aabbccdeeffg"
def first_non_repeated_char(string):
    char_count = {}
    # Count the occurrences of each character in the string
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Find the first character with a count of 1
    for char in string:
        if char_count[char] == 1:
            return char

    # If no non-repeating character found, return None or an appropriate value
    return None
print(first_non_repeated_char(string))



# Given a list of integers li and a target value, write a Python function to find all unique pairs of numbers in the list that add up to the target. Implement the function find_number_pairs(li, target) that takes the list li and the target value as input and returns a list of tuples representing the pairs.
li = [4, 3, 1, 6, 8, 5, 2]
target = 7
result =[]
def unique_pairs(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i]+li[j]==target:
                result.append((li[i],li[j]))
    return result
print(unique_pairs(li))

# Given a list of integers, write a Python function to find the two numbers that add up to a specific target.
# Example Input:
numbers = [2, 7, 11, 15]
target = 9
res = []
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==target:
            res.append((numbers[i],numbers[j]))  
print(res)

# Given a string, write a Python function to find all possible permutations of the characters.
import itertools
def find_permutations(input_string):
    permutations = list(itertools.permutations(input_string))
    permutations = [''.join(perm) for perm in permutations]
    return permutations

input_string = "abc"
output = find_permutations(input_string)
print(output)

# Polymorphism
class car:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
    def move(self):
        print('drive')
class flight:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
    def move(self):
        print('drive')

obj = car('suzuki',100)
obj1 = flight('asisa',300)

for i in (obj,obj1):
    i.move()
   
# abstract method

from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def display(self):
        pass

# decorator

def check_login(login):
    def inner(username,passwrd):
        if username == 'Bhargav' and passwrd=="bhargav":
            return 'Valid user'
        else:
            return login(username,passwrd)
    return inner

@check_login
def login(username,passwrd):
    return 'Invalid Credntials'
print(login("bhargav","bhargav"))


# Explain the difference between a shallow copy and a deep copy in Python.
import copy

list1 = [1, 2, [3, 4]]

# Shallow copy
list2 = copy.copy(list1)

# Modifying the nested list in the shallow copy
list2[2][0] = 5

print(list1)  # Output: [1, 2, [5, 4]]
print(list2)  # Output: [1, 2, [5, 4]]

# Deepcopy
from copy import deepcopy

list1 = [1, 2, [3, 4]]

# Shallow copy
list2 = copy.deepcopy(list1)

# Modifying the nested list in the shallow copy
list2[2][0] = 5

print(list1)  # Output: [1, 2, [5, 4]]
print(list2)  # Output: [1, 2, [5, 4]]





# How can you efficiently read large files in Python?
# What are the differences between sets and frozensets in Python?

# Explain the concept of method resolution order (MRO) in Python.
# How can you measure the execution time of a Python program or a specific code segment?