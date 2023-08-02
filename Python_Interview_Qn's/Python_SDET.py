# ===>>>        Swapping of two Elements

# Note :: Swapping / Item Assignment can be done on Only List Data Type.
# Question :: Why we can't Perform Swapping / Item Assignment on other Data Types.
# Ans :: Swapping / Item Assignment Operation can be done on Mutable and Ordered Objs Only.

# n1 = int(input("Enter Some Number :: "))
# n2 = int(input("Enter Some Number :: "))
# print("Before Swapping n1 is -->> {}, and n2 is -->> {} ".format(n1, n2))
# n1, n2 = n2, n1
# print("After Swapping n1 is -->> {}, and n2 is -->> {} ".format(n1, n2))

# lst = [10, 20, 45, 60, 38, 50]
# print("Before Swapping :: ", lst)
#
# pos1 = len(lst) - 4
# pos2 = len(lst) - 2
#
# get = (lst[pos1], lst[pos2])
# (lst[pos2], lst[pos1]) = get
# print("After Swapping :: ", lst)

# t = (10, 20, 45, 60, 38, 50)
#
# pos1 = len(t) - 4
# pos2 = len(t) - 2
#
# get = (t[pos1], t[pos2])
# (t[pos2], t[pos1]) = get

# print("After Swapping :: ", t)
# TypeError: 'tuple' object does not support item assignment -->> Because, Tuple is Immutable Obj. so, we cant perform
# changes on it. So Final Consultation is we can't perform changes in Immutable Obj's.

# s = {10, 20, 45, 60, 38, 50}
#
# pos1 = len(s) - 4
# pos2 = len(s) - 2
#
# get = (s[pos1], s[pos2])
# (s[pos2], s[pos1]) = get
# print("After Swapping :: ", s)

# TypeError: 'set' object is not subscriptable, Because, Even Though Set Onj is Mutable, but it is UnOrdered.
# So, we can't perform Item Assignment on Set Obj.

# ===>>> Prime Number Check
# A Number which is Dividable by 1 and itself is called Prime Number

# n = int(input("Enter Some Number :: "))
# c = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         c = c + 1
# if c == 2:
#     print("It's a Prime Number :: ", n)
# else:
#     print("It's Not a Prime Number ::", n)

# ===>>>        Prime Numbers B/W 1 to 10

# n = int(input("Enter Some Number :: "))
#
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)


# ===>>>        Prime Numbers B/W 100 to 1000

# n = int(input("Enter Some Number :: "))
#
# for i in range(101, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# ===>>>        Factorial of a Given Number

# n = int(input("Enter Some Number :: "))
# factorial = 1
# if n < 0:
#     print("For -ve Values, Factorial is Not Applicable ::")
# elif n == 0 & n == 1:
#     print("Factorial for 0 and 1 is 1")
# else:
#     for i in range(2, n + 1):
#         factorial = factorial * i
# print(factorial)

# n = int(input("Enter Some Number :: "))
#
#
# def factorial(n):
#     if (n == 0) or (n == 1):
#         return 1
#     else:
#         for i in range(2, n + 1):
#             return n * factorial(n - 1)
#
#
# print(factorial(n))


# ===>>>        Fibonacci Series B/W 1 to 10

# n1 = 1
# n2 = 2
# total = 0
# for i in range(2, 11):
#     total = n1 + n2
#     print(total, end=' ')
#     n1 = n2
#     n2 = total


# ===>>>        Fibonacci Series B/W 10 to 100

# n1 = 10
# n2 = 11
# total = 0
# for i in range(12, 101):
#     total = n1 + n2
#     print(total, end=' ')
#     n1 = n2
#     n2 = total


# ===>>>        Find Sum of a List of Elements

# lst = [10, 20, 30, 40, 50]
# total = 0
#
# for i in range(0, len(lst)):
#     total = total + lst[i]
# print(total)


# ===>>>        Find Second Largest and Second Smallest Number in a given List

# lst = [10, 36, 20, 30, 45, 40, 50, 60, 12, 56]
# print("Before Sorting ::", lst)

# for i in range(0, len(lst)):
#     for j in range(i, len(lst)):
#         if lst[i] > lst[j]:
#             get = (lst[i], lst[j])
#             (lst[j], lst[i]) = get
# print("After Sorting with small to Large :: ", lst)
# print("Second Largest Number is :: ", lst[len(lst) - 2])
#
# for i in range(0, len(lst)):
#     for j in range(i, len(lst)):
#         if lst[i] < lst[j]:
#             get = (lst[i], lst[j])
#             (lst[j], lst[i]) = get
# print("After Sorting with Large to Small :: ", lst)
# print("Second Largest Number is :: ", lst[len(lst) - 2])

# ===>>>        Find Length of given List, Tuple, Set, Dict
# lst = [10, 36, 20, 30, 45, 40, 50, 60, 12, 56]
# c = 0
#
# for i in range(0, len(lst)):
#     c = c + 1
# print("Length of a Given List is :: ", c)

# t = (10, 36, 20, 30, 45, 40, 50, 60, 12, 56)
# c = 0
#
# for i in range(0, len(t)):
#     c = c + 1
# print("Length of a Given Tuple is :: ", c)

# set1 = {10, 36, 20, 30, 45, 40, 50, 60, 12}
# c = 0
#
# for i in range(0, len(set1)):
#     c = c + 1
# print("Length of a Given Set is :: ", c)

# d = {10: 'raja', 36: 'uma', 50: 'teja', 60: 'Sony', 12: 'Google', 56: 'CGI'}
# c = 0
#
# for i in range(0, len(d)):
#     c = c + 1
# print("Length of a Given Dict is :: ", c)

# s = 'PythonAutomationTesting'
# c = 0
#
# for i in range(0, len(s)):
#     c = c + 1
# print("Length of a Given String is :: ", c)

# ===>>>        Swapping 1st and Last Elements in a given List

# lst = [10, 36, 20, 30, 45, 40, 50, 60, 12, 56]
# print("Before Swapping :: ", lst)
# for i in range(0, len(lst)):
#     if i == 0:
#         for j in range(0, len(lst)):
#             if j == len(lst) - 1:
#                 get = (lst[i], lst[j])
#                 (lst[j], lst[i]) = get
# print("After Swapping :: ", lst)

# ===>>>        Remove Nth Occurrence from a given List

# lst = ['raja', 'uma', 'teja', 'sony', 'Google', 'CGI']
# n = int(input("Enter Nth Occurrence Number :: "))
# print("Before Removing the Nth Occurrence element form a given List :: ", lst)
# print("Before Removing Length of the given List is :: ", len(lst))
# if n < len(lst):
#     for i in range(0, len(lst)):
#         if i == n:
#             lst.pop(i)
# else:
#     print("Pls Enter Nth Occurrence value less than {}".format(len(lst)))
# print("After Removing the Nth Occurrence element form a given List :: ", lst)
# print("After Removing Length of the given List is :: ", len(lst))

# lst = ['raja', 'uma', 'teja', 'sony', 'Google', 'CGI']
# lst.reverse()
# print("After Reversing :: ", lst)
# rev_lst = lst[::-1]
# print("After Reversing :: ", rev_lst)

# i = len(lst) - 1
# output = []
# while i >= 0:
#     output.append(lst[i])
#     i = i - 1
# print(output)

# lst = ('raja', 'uma', 'teja', 'sony', 'Google', 'CGI')
# i = len(lst) - 1
# t = []
# while i >= 0:
#     t.append(lst[i])
#     i = i - 1
# output = tuple(t)
# print(output)


# ===>>>        Shallow Copy

# In Shallow Copy, Different Obj will be Created For Mutable Obj's
# In Shallow Copy, Same Obj will be Created For Immutable Obj's

# lst1 = [10, 20]
# # lst2 = [10, 20]
# # lst2 = lst1.copy()
# # lst2 = list(lst1)
# # lst2 = lst1
# print("Id for lst1 is :: ", id(lst1))
# print("Id for lst2 is :: ", id(lst2))
#
t1 = (10, 20)
# t2 = (10, 20)
# t2 = tuple(t1)
t2 = t1
print("Id for t1 is :: ", id(t1))
print("Id for t2 is :: ", id(t2))

# ===>>>        Deep Copy

# In Deep Copy, Different Obj will be Created For Mutable Obj's
# In Shallow Copy, Same Obj will be Created For Immutable Obj's

import copy
# lst1 = [10, 20]
# lst2 = copy.copy(lst1)
# print("Id for lst1 is :: ", id(lst1))
# print("Id for lst1 is :: ", id(lst2))

# t1 = (10, 20)
# t2 = copy.copy(t1)
# print("Id for t1 is :: ", id(t1))
# print("Id for t2 is :: ", id(t2))











