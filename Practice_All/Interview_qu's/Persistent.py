# ========================= String ==============================

# # 1) Write a Program to Remove Punctuations from a Given String
# s = input("Enter Some String :: ")
# spe_chars = "!@#$%^&*()_-=+{}[]:;"'?/.>,<'
# output = ''
# for i in s:
#     if i not in spe_chars:
#         # print(i, end='')
#         output = output + i
# print(output)
#
# # 2) Write a Program to Remove all WhiteSpaces from a Given String
# s = input("Enter Some String :: ")
# spe_char = "' '"
# output = ''
# for i in s:
#     if i not in spe_char:
# #         print(i, end='')
#         output = output + i
# print(output)
#
#
# # 3) Write a Program to Count the occurrence of each word in a given String
#
# s = input("Enter Some String :: ")
# lst = s.split()
# n = len(lst)
# count = {}
#
# for word in lst:
#     if word not in count:
#         count[word] = 1
#     else:
#         count[word] = count[word] + 1
# print(count)
#
#
# # 4) Write a Program to Count the occurrence of each char in a given String
#
# s = input("Enter Some String :: ")
# count = {}
#
# for char in s:
#     if char not in count:
#         count[char] = 1
#     else:
#         count[char] = count[char] + 1
# print(count)
#
#
# # 5) Write a Program to count no.of Upper and Lower case letters in a given String
# s = input("Enter Some String :: ")
# upper = 0
# lower = 0
# spaces = 0
# for i in s:
#     if i.isupper():
#         upper = upper + 1
#         print(i, end='')
#     elif i.islower():
#         lower = lower + 1
#         print(i, end='')
#     else:
#         spaces = spaces + 1
#         print(i, end='')
# print()
# print("count no.of Upper case letters in a given String :: ", upper)
# print("count no.of lower case letters in a given String :: ", lower)
# print("count no.of WhiteSpaces in a given String :: ", spaces)

# # 6) Write a Program to Check Given String is Palindrome or Not ??
# s = input("Enter Some String :: ")
# i = len(s) - 1
# output = ''
# while i >= 0:
#     output = output + s[i]
#     i = i - 1
# print("Reverse of a Given String :: ", output)
# if s == output:
#     print("Given String is Palindrome :: ", s)
# else:
#     print("Given String is Not a Palindrome :: ", s)
#
#
# # 7) Write a Program to check given two Strings are Anagram or not??

# s = input("Enter first String :: ")
# s2 = input("Enter second String :: ")
#
# if sorted(s1) == sorted(s2):
#     print("given Strings are Anagram")
# else:
#     print("given Strings are Not Anagram")


# # 8) # Write a program to print common letters b/w given two Strings
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
#
# output = ''
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j]:
#             output = output + s1[i]
# print(output)

# for i in range(0, len(s1)):
#     if s1[i] in s2:
#         output = output + s1[i]
# print(output)
#
#
# # 9) #Write a Program to Print reverse of a given String
# # i/p = "Raja"
# # o/p = "ajaR"
#
# s = input("Enter Some String :: ")
# output = ''
# i = len(s) - 1
#
# while i >= 0:
#     output = output + s[i]
#     i = i - 1
# print("without duplicate removal :: ", output)
#
# 10) # Write a Program to Print reverse of a given String with removal of duplicate
# i/p = "Raja"
# o/p = "ajR"

# s = input("Enter Some String :: ")
# output = ''
# i = len(s) - 1
#
# while i >= 0:
#     if s[i] not in output:
#         output = output + s[i]
#     i = i - 1
#
# print("with duplicate removal :: ", output)
#
# # 11) # Write a Program to Print reverse order of words from a given String
# i/p = "Raja Python Automation Tester"
# o/p = "Tester Automation Python Raja"
#
# s = input("Enter Some String :: ")
# lst = s.split()
# lst1 = []
# i = len(lst) - 1
#
# while i >= 0:
#     lst1.append(lst[i])
#     i = i - 1
# print(lst1)
#
#
# # 12)# Write a Program to Print Internal Content reverse order of each words from a given String
# i/p = "Raja Python Automation Tester"
# o/p = "ajaR nohtyP noitamotuA retseT"
#
# s = input("Enter Some String :: ")
# lst = s.split()
# lst1 = []
# for word in lst:      # Raja
#     lst1.append(word[::-1])
#
# print(lst1)
#
# # 13)# Write a Program to Print Internal Content reverse order of each first words from a given String
# i/p = "Raja Python Automation Tester"
# o/p = "ajaR Python noitamotuA Tester"
#
# s = input("Enter Some String :: ")
# lst = s.split()
# lst1 = []
# i = 0
# while i < len(lst):
#     if i % 2 == 0:
#         lst1.append(lst[i][::-1])
#     else:
#         lst1.append(lst[i])
#     i = i + 1
# print(lst1)
#
#
# # 14)# Write a Program to Print Internal Content reverse order of each second words from a given String
# i/p = "Raja Python Automation Tester"
# o/p = "Raja nohtyP Automation retseT"
#
# s = input("Enter Some String :: ")
# lst = s.split()
# lst1 = []
# i = 0
# while i < len(lst):
#     if i % 2 == 0:
#         lst1.append(lst[i])
#     else:
#         lst1.append(lst[i][::-1])
#     i = i + 1
# print(lst1)
#
#
# # 15)# Write a Program to Print following requirement
# i/p = "AAAADDDBBBRR"
# o/p = "A4D3B3R2"
#
# s = input("Enter Some String :: ")
# previous = s[0]
# c = 0
# i = 0
# outcome = ''
# while i < len(s):
#     if s[i] == previous:
#         c = c + 1
#
#     else:
#         previous = s[i]
#         c = 1
#
#     i = i + 1
#     outcome = outcome + previous + str(c)
# print(outcome)
#

# s = input("Enter Some String :: ")
# v = "aeiouAEIOU"
# c = 0
# output = ''
# for i in s:
#     if i not in v:
#         output = output + i
# print(output)


# 16) # Write a Program to find out common letters b/w given two Strings
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# output = ''
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j]:
#             output = output + s1[i]
# print("common letters b/w given two Strings are :: ", output)


# 17) # Write a Program to find out common letters b/w given two Strings without duplicates
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# output = ''
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j] and s1[i] not in output:
#             output = output + s1[i]
# print("common letters b/w given two Strings are :: ", output)


# 18) # Write a Program to find out common letters b/w given two Strings without duplicates and  no. of times
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# output = ''
# count = {}
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j] and s1[i] not in output:
#             output = output + s1[i]
#             if s1[i] not in count:
#                 count[s1[i]] = 1
#             else:
#                 count[s1[i]] = count[s1[i]] + 1
# print("common letters b/w given two Strings are :: ", output)
# print("common letters b/w given two Strings are with no. of times ::", count)


# # 19) # Write a Program to find out common words b/w given two Strings
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# lst1 = s1.split()
# lst2 = s2.split()
# output = []
# for i in range(0, len(lst1)):
#     for j in range(0, len(lst2)):
#         if lst1[i] == lst2[j]:
#             output.append(lst1[i])
# print("common letters b/w given two Strings are :: ", output)


# # 20) # Write a Program to find out common words b/w given two Strings without duplicates
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# lst1 = s1.split()
# lst2 = s2.split()
# output = []
# for i in range(0, len(lst1)):
#     for j in range(0, len(lst2)):
#         if lst1[i] == lst2[j] and lst1[i] not in output:
#             output.append(lst1[i])
# print("common letters b/w given two Strings without duplicates are :: ", output)


# # 21) # Write a Program to find out common words b/w given two Strings without Duplicates and count of word

# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# lst1 = s1.split()
# lst2 = s2.split()
# output = []
# count = {}
# for i in range(0, len(lst1)):
#     for j in range(0, len(lst2)):
#         if lst1[i] == lst2[j] and lst1[i] not in output:
#             output.append(lst1[i])
#             if lst1[i] not in count:
#                 count[lst1[i]] = 1
#             else:
#                 count[lst1[i]] = count[lst1[i]] + 1
# print("common letters b/w given two Strings are :: ", output)
# print("common letters b/w given two Strings are with no. of times ::", count)

# # 22) # Write a Program to find out common words b/w given two Strings without Duplicates and count of word with
# length condition

# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# lst1 = s1.split()
# lst2 = s2.split()
# output = []
# count = {}
# for i in range(0, len(lst1)):
#     for j in range(0, len(lst2)):
#         if len(lst1[i]) > len(lst2[j]):
#             if lst1[i] == lst2[j] and lst1[i] not in output:
#                 output.append(lst1[i])
#                 if lst1[i] not in count:
#                     count[lst1[i]] = 1
#                 else:
#                     count[lst1[i]] = count[lst1[i]] + 1
#         else:
#             if lst1[i] == lst2[j] and lst1[i] not in output:
#                 output.append(lst1[i])
#                 if lst1[i] not in count:
#                     count[lst1[i]] = 1
#                 else:
#                     count[lst1[i]] = count[lst1[i]] + 1
#
# print("common letters b/w given two Strings are :: ", output)
# print("common letters b/w given two Strings are with no. of times ::", count)

# ================== Dict ===============================
#
# # 1) Write a Program to check weather given Value is already present in a Dict or Not??

# d = {'Raja': 'Python Tester', 'Uma': 'Business Analyst', 'Teja': 'Python Developer', 'Company': 'Sony'}
# exist_value = input("Enter Some String :: ")
# keys_lst = d.keys()
# values_lst = d.values()
# print("Length of Keys :: ", len(keys_lst))
# print("Length of Values :: ", len(values_lst))
#
# if exist_value in values_lst:
#     print("Existing Value is Presented in a Given String :: ", exist_value)
# else:
#     print("Existing Value is Not Presented in a Given String :: ", exist_value)


# for i, j in d.items():
#     print(i, j)
#     if j == exist_value:
#         print("given Value is already present")
#     else:
#         print("given Value is Not present")

# # 2) Write a Program to add given two Lists in to Dict
# lst1 = [10, 20, 30, 40]
# lst2 = ['Raja', 'Uma', 'Teja', 'Sony']
# d = {}
#
# for i in range(0, len(lst1)):
#     for j in range(i, i + 1):
#         d.__setitem__(lst1[i], lst2[j])
# print("two Lists in to Dict :: ", d)
#
# d1 = dict(zip(lst1, lst2))
# print(d1)
#
# 3) # Write a Program to print dictionary without having duplicate values
#
# d = {1: 'karthik', 2: 'raja', 3: 'capgemini', 4: 'balaiah', 5: 'raja'}
# empty = {}
# lst = []
#
# for i, j in d.items():
#     if j not in lst:
#         lst.append(j)
#         empty[i] = j
# print("List of Values from a given Dictionary :: ", lst)
# print("dictionary without having duplicate values :: ", empty)
#
#
# ============================== List =========================================
#
# 1) # Write a Program to check 1st and last ele's are same in given List
#
# lst = [10, 20, 40, 70, 20, 10, 20, 10]
#
# first = lst[0]
# last = lst[len(lst) - 1]
# if first == last:
#     print("{} and {}  ele's are same in given List".format(first, last))
# else:
#     print("{} and {}  ele's are Not same in given List".format(first, last))
#
#
# for i in range(0, len(lst)):
#     if i == 0:
#         for j in range(len(lst)-1, len(lst)):
#             if lst[i] == lst[j]:
#                 print("Same")
#             else:
#                 print("Not Same")
#     else:
#         break


# 2) # Write a Program to Extend List without using append/extend functions.
#
# lst1 = [10, 20, 30]
# lst2 = ['raja', 'teja', 'uma']
#
# lst1.append(lst2)
# print(lst1)
#
# lst1.extend(lst2)
# print(lst1)
#
# lst1[:0:] = lst2
# print(lst1)
#
# lst2[:0:] = lst1
# print(lst2)
#
# lst1[:0:] = lst2
# print(lst1)
#
# # 3) # Write a Program to separate Strings and int from a given list
#
# lst = [10, 'raja', 20, 'Capgemini', 'Interviews', 30]
# alpha = []
# number = []
# for i in range(0, len(lst)):
#     if type(lst[i]) == str:
#         alpha.append(lst[i])
#     else:
#         number.append(lst[i])
#
#
# print(alpha)
# print(number)
#
#
# # 4) # Write a Program to Search Element in a given List
#
# lst = [10, 20, 'raja', 'diamond', 30, 'programmer']
# s = input("Enter Some String :: ")
# ser_String = []
# for i in range(0, len(lst)):
#     if lst[i] == s:
#         ser_String.append(lst[i])
#
# print(ser_String)
#
#
# # 5) # Write a Program to Print  Length of a given List
#
# lst = [10, 20, 'raja', 'diamond', 30, 'programmer']
# # print(len(lst))
# c = 0
# for i in range(0, len(lst)):
#     c = c + 1
# print("Length of a given list is :: ", c)
#
#
# # 6) # Write a Program to Print List with "n" no.of Empty Dict's
#
# n = int(input("Enter Some Number :: "))
# lst_dic = [{} for _ in range(n)]
# print(lst_dic)
#
# # 7) # Write a Program to Print Last Element of a List
#
# lst = [10, 20, 'raja', 'diamond', 30, 'programmer']
# last_ele = len(lst) - 1
#
# for i in range(0, len(lst)):
#     if i == last_ele:
#         print(lst[i])
#
#
# # 8) # Write a Program to Sum of all the ele in a List
#
# lst = [10, 50, 30, 20, 70, 45, 25]
# total = 0
#
# for i in range(0, len(lst)):
#     total = total + lst[i]
# print("Sum of all elements in a given list are :: ", total)
#
#
# # 9) # Write a Program to Access Index of a List, Start the Index as 'Non Zero' in Acc-sending Order
#
# lst = [8, 4, 2, 6, 5, 7]
# output = []
# for index, val in enumerate(lst, start=1):
#     print(index, "-->>", val)
#
#
# # 10) # Write a Program to triple all the elements in a given List
#
# lst = [8, 4, 2, 6, 5, 7]
# output = []
# for i in range(0, len(lst)):
#     output.append(lst[i]**3)
# print(output)
#
# # 11) # Swapping Two Numbers in a given List without 3rd reference
#
# lst = [8, 4, 2, 6, 5, 7]
# pos1 = 1
# pos2 = len(lst) - 2
#
# print("Index of first ele is :: ", pos1)
# print("Index of second ele is :: ", pos2)
# print("Before Swapping :: ", lst)
#
# get = (lst[pos1], lst[pos2])
# lst[pos2], lst[pos1] = get
# print("After Swapping :: ", lst)
#
# for i in range(0, len(lst)):
#     if i == 1:
#         for j in range(0, len(lst)):
#             if j == len(lst) - 2:
#                 get = (lst[i], lst[j])
#                 (lst[j], lst[i]) = get
# print(lst)

# 12) # Write a Program to print the list without duplicates from a given list
#
# x = ['a', 'b', 'c', 'a', 'c', 'c']
# output = []
# output1 = []
# for i in range(0, len(x)):
#     for j in range(i + 1, len(x)):
#         if x[i] != x[j] and x[i] not in output:
#             output.append(x[i])
#
# print(output)

# # 13) # Write a Program to print duplicates from a given list
#
# x = ['a', 'b', 'c', 'a', 'c', 'c']
# output = []
# output1 = []
# for i in range(0, len(x)):
#     for j in range(i + 1, len(x)):
#         if x[i] == x[j] and x[i] not in output:
#             output.append(x[i])
#
# print(output)

# 14) # Write a Program to Print second-largest Number from a given list

# lst = [10, 50, 20, 60, 80, 30, 15, 40]
#
# for i in range(0, len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] > lst[j]:
#             get = (lst[i], lst[j])
#             (lst[j], lst[i]) = get
# print(lst)
# print("second largest number is :: ", lst[len(lst) - 2])

#
# # 15) # Write a Program to Print List with sum of each element from given two lists
#
# lst1 = [10, 20, 30, 40, 50]
# lst2 = [80, 30, 29, 48, 56, 78]
# lst3 = []
# for i in range(0, len(lst1)):
#     for j in range(i, i + 1):
#         lst3.append(lst1[i] + lst2[j])
# if len(lst2) - 1 > len(lst1) - 1:
#     lst3.append(lst2[len(lst2) - 1])
# print(lst3)


# =================================================================
#
# # 1) # Write a Program to Print Factorial of a given Number
#
# n = int(input("Enter Some Number :: "))
# factorial = 1
# if n < 0:
#     print("Factorial is Not applicable for -ve Numbers :: ")
# elif n == 0 & n == 1:
#     print("Factorial of 0 and 1 is 1 :: ")
# else:
#     for i in range(2, n + 1):
#         factorial = factorial * i
# print(factorial)
#
#
# 2) # Write a Program to Print Factorial of a given Number by using Recursive function

# n = int(input("Enter Some Number :: "))
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print("Factorial of a given Num is :: ", factorial(n))
#

# 3) # Write a Program to Check given Num is Prime or Not ??
# n = int(input("Enter Some Number :: "))
# c = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         c = c + 1
# if c == 2:
#     print("Prime Number :: ", n)
# else:
#     print("Not a Prime Number :: ", n)
#
#
# 4) # Write a Program to Print Prime Numbers b/w 1 - 10
#
# n = int(input("Enter Some Number :: "))
#
# for i in range(2, n + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#
#
# # 5) # Write a Program to Print Fibonacci Series b/w 0 to 10 ??
#
# n = int(input("Enter Some Number :: "))
#
# n1 = 0
# n2 = 1
# total = 0
# for i in range(2, n + 1):
#     total = n1 + n2
#     print(total, end=' ')
#     n1 = n2
#     n2 = total
#
#
# 6) # Write a Program to Print Largest Num from the given three inputs
#
# n1 = int(input("Enter n1 Number :: "))
# n2 = int(input("Enter n2 Number :: "))
# n3 = int(input("Enter n3 Number :: "))
#
# if n1 > n2 and n1 > n3:
#     print("max", n1)
# elif n2 > n1 and n2 > n3:
#     print("max", n2)
# else:
#     print("max", n3)
#
#
# 7) # Write a Program to check given Num is Armstrong or Not??
# Approach : 1

# n = int(input("Enter Some Number :: "))
# n1 = str(n)
# print(type(n1))
# b = len(n1)
# Armstrong = 0
# for i in n1:
#     Armstrong = Armstrong + (int(i) ** b)
#
# if n == Armstrong:
#     print("Given Number is Armstrong :: ")
# else:
#     print("Given Number is Not Armstrong :: ")

# Approach : 2
# n = int(input("Enter Some Number :: "))
# arm = n
# total = 0
# s = str(n)
# b = len(s)
# while n > 0:
#     r = n % 10
#     total = total + (r ** b)
#     n = n // 10
# print(total)
#
# if arm == total:
#     print("given num is Armstrong :: ")
# else:
#     print("given num is not Armstrong :: ")
#
# Approach :: 3
#
# num = int(input("Enter Some Number :: "))
# def armstrong_check(num):
#     result = 0
#     n = len(str(num))
#     act = num
#     while num > 0:
#         digit = num % 10
#         result = result + digit ** n
#         num = num // 10
#     if act == result:
#         return True
#     else:
#         return False
#
#
# if armstrong_check(num):
#     print("The give num is Armstrong :: ")
# else:
#     print("The give num is not Armstrong :: ")


# 7i) # Write a Program to Print Armstrong numbers b/w 1 - 1000

# n = int(input("Enter Some Number :: "))
# for num in range(1, n + 1):
#     Arm = num
#     num_s = str(num)
#     total = 0
#     b = len(num_s)
#     for j in num_s:
#         total = total + (int(j) ** b)
#     if total == Arm:
#         print(Arm)


# n = int(input("Enter Some Number :: "))
#
# for num in range(1, n + 1):
#     Arm = num
#
#     num_s = str(num)
#     length = len(num_s)
#     total = 0
#     for j in num_s:
#         total = total + (int(j) ** length)
#     if total == Arm:
#         print(Arm)


# # 9) # Write a Program to Reverse a Given Number
# i/p = 153
# o/p = 351

# n = int(input("Enter Some Number :: "))
# s = str(n)
# print(len(s))
# i = len(s) - 1
# rev = ''
# while i > 0:
#     rev = rev + s[i]
#     i = i - 1
# print(rev)

# 9i) # Write a Program to Reverse a Given Number without -ve
# i/p = -153
# o/p = -351

# n = int(input("Enter Some Number :: "))
# s = str(n)
# print(len(s))
# i = len(s) - 1
# rev = ''
# while i > 0:
#     rev = rev + s[i]
#     i = i - 1
#     if i == 0:
#         rev = s[i] + rev
# print(rev)


# # 10) # Write a Program to find all Numbers which are dividable by 7 and not multiple by 5
#
# n = int(input("Enter Some Number :: "))
# div = 7
# mul = 5
#
# for i in range(1, n + 1):
#     if (i % div == 0) and (i * mul != 0):
#         print(i, end=' ')
#
#
# 11) # Write a Program to Print Multiplication Table
#
# n = int(input("Enter Some Number :: "))
#
# for i in range(1, 11):
#     print(n, "*", i, "=", (n * i))
#
#
# # 12) # Write a Program to Print Leap 'Year'
#
# year = int(input("Enter Some Year :: "))
#
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print("It's a Leap Year :: ", year)
# else:
#     print("Not a Leap Year :: ", year)
