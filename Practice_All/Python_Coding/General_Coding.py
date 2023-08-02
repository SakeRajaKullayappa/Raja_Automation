# Write a Program to Print Factorial of a given Number

# n = int(input("Enter Some String :: "))
# factorial = 1
#
# if n < 0:
#     print("For -ve Numbers Factorial is not applicable")
# elif n == 0 & n == 1:
#     print("Factorial for 0 and 1 is always 1")
# else:
#     for i in range(2, n + 1):
#         factorial = factorial * i
# print("factorial of a given Num is ::", factorial)

# Write a Program to Print Factorial of a given Number by using Recursive function

# n = int(input("Enter Some Number :: "))
#
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(n))

# Write a Program to Check given Num is Prime or Not ??

# n = int(input("Enter Some Number :: "))
# c = 0
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         c = c + 1
# if c == 2:
#     print("It's a Prime Number")
# else:
#     print("It's Not a Prime Number")

# Write a Program to Print Prime Numbers b/w 1 - 10

# n = int(input("Enter Some Number :: "))
#
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# Write a Program to Print Fibonacci Series b/w 0 to 10 ??

# n = int(input("Enter Some Number :: "))
# n1 = 0
# n2 = 1
# total = 1
#
# for i in range(2, n + 1):
#     total = n1 + n2
#     print(total, end=' ')
#     n1 = n2
#     n2 = total

# Write a Program to Print Largest Num from the given three inputs/Numbers
# n1 = int(input("Enter First Number :: "))
# n2 = int(input("Enter Second Number :: "))
# n3 = int(input("Enter Third Number :: "))
#
# if n1 > n2 & n1 > n3:
#     print("Largest Number is :: ", n1)
# elif n2 > n3:
#     print("Largest Number is :: ", n2)
# else:
#     print("Largest Number is :: ", n3)

# Write a Program to check given Num is Armstrong or Not??
# n = int(input("Enter Some Number :: "))
# n_s = str(n)
# b = len(n_s)
# armstrong = n
# total = 0
#
# for i in range(0, len(n_s)):
#     total = total + (int(n_s[i]) ** b)
# print(total)
#
# if total == n:
#     print("It's a Armstrong Number :: ", n)
# else:
#     print("It's Not a Armstrong Number :: ", n)

# Write a Program to Print Armstrong numbers b/w 1 - 1000
# n = int(input("Enter Some Number :: "))
# for i in range(1, n + 1):
#     num = i
#     num_s = str(i)
#     b = len(num_s)
#     total = 0
#     armstrong = num
#
#     for j in range(0, len(num_s)):
#         total = total + (int(num_s[j]) ** b)
#     if total == armstrong:
#         print(num, end=' ')

# Write a Program to Reverse a Given Number
# n = int(input("Enter Some Number :: "))
# n_s = str(n)
# rev = ''
# for i in range(0, len(n_s)):
#     rev = n_s[i] + rev
# rev_n = int(rev)
# print(rev_n)
# print(type(rev_n))

# i = len(n_s) - 1
# while i >= 0:
#     rev = rev + n_s[i]
#     i = i - 1
# n_rev = int(rev)
# print(n_rev)
# print(type(n_rev))

# Write a Program to Reverse a Given Number without -ve
# n = int(input("Enter Some Negative Number :: "))
# n_s = str(n)
# rev = ''
# i = len(n_s) - 1
#
# while i > 0:
#     rev = rev + n_s[i]
#     i = i - 1
# if i == 0:
#     rev = n_s[i] + rev
#
# print(rev)
# print(type(rev))
# n_rev = int(rev)
# print(n_rev)
# print(type(n_rev))

# Write a Program to find all Numbers which are dividable by 7 and not multiple by 5
# n = int(input("Enter Some Number :: "))
# div = int(input("Enter Some Dividable Number :: "))
# mul = int(input("Enter Some Multi-cable Number :: "))
#
# for i in range(1, n + 1):
#     if (i % div == 0) and (i * mul != 0):
#         print(i)

# Write a Program to Print Multiplication Table

# n = int(input("Enter Some Number :: "))
#
# for i in range(0, 11):
#     print(n, '*', i, '=', (n * i))

# Write a Program to Print Leap Year
# n = int(input("Enter Some Year :: "))
#
# if (n % 4 == 0) and (n % 100 != 0) or (n % 400 == 0):
#     print("It's a Leap Year")
# else:
#     print("It's not a Leap Year")

# Write a Program to Check Given Number is Perfect Number or Not??

# n = int(input("Enter Some Number :: "))
# total = 0
#
# for i in range(1, n):
#     if n % i == 0:
#         total = total + i
# print(total)
#
# if n == total:
#     print("It's a Perfect Number ::", n)
# else:
#     print("It's Not a Perfect Number ::", n)

# Write a Program to Print Perfect Numbers b/w 1 to 100??
# n = int(input("Enter Some Number :: "))
# p_n = []
#
# for i in range(1, n + 1):
#     total = 0
#     for j in range(1, i):
#         if i % j == 0:
#             total = total + j
#     if total == i:
#         p_n.append(i)
# print("Perfect Numbers are :: ", p_n)

# Write a Program to Print Given Number is Strong Number or Not??
# ex :: 145 = 1! + 4! + 5!

# n = int(input("Enter Some Number :: "))
# n_str = str(n)
# total_fact = 0
#
# for i in n_str:
#     fact = 1
#     if int(i) == 1:
#         fact = fact * int(i)
#     else:
#         for j in range(2, int(i) + 1):
#             fact = fact * (int(j))
#     total_fact = total_fact + fact
# print(total_fact)
#
# if n == total_fact:
#     print("It's a Strong Number :: ")
# else:
#     print("It's Not a Strong Number :: ")

# n = int(input("Enter Some String :: "))
# factorial = 1
#
# if n < 0:
#     print("For -ve Numbers Factorial is not applicable")
# elif n == 0 & n == 1:
#     print("Factorial for 0 and 1 is always 1")
# else:
#     for i in range(2, n + 1):
#         factorial = factorial * i
# print("factorial of a given Num is ::", factorial)