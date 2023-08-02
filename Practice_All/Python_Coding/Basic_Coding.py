# Write a Program to Print Factorial of a given Number

# n = int(input("Enter Some Number :: "))
# factorial = 1
#
# if n < 0:
#     print("Factorial is not applicable for -ve Values")
# elif n == 0 or n == 1:
#     print("Factorial of 0 and 1 is :: 1")
# else:
#     for i in range(2, n + 1):
#         factorial = factorial * i
# print(factorial)

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
# print("Factorial of a given Num is ::", factorial(5))

# Write a Program to Check given Num is Prime or Not ??

# n = int(input("Enter Some Number :: "))
# c = 0
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         c = c + 1
#
# if c == 2:
#     print("It's a Prime Number :: ")
# else:
#     print("It's Not a Prime Number :: ")

# Write a Program to Print Prime Numbers b/w 1 - 10??

# n = int(input("Enter Some Number :: "))
#
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=' ')

# Write a Program to Print Fibonacci Series b/w 0 to 10 ??

# n = int(input("Enter Some Number :: "))
# n1 = 0
# n2 = 1
# fibonacci = 0
#
# for i in range(2, n + 1):
#     fibonacci = n1 + n2
#     print(fibonacci, end=' ')
#     n1 = n2
#     n2 = fibonacci

# Write a Program to Print Largest Num from the given three inputs/Numbers

# n1 = int(input("Enter Some Number :: "))
# n2 = int(input("Enter Some Number :: "))
# n3 = int(input("Enter Some Number :: "))
#
# if n1 > n2 and n1 > n3:
#     print("Max Value is :: ", n1)
# elif n2 > n1 and n2 > n3:
#     print("Max Value is :: ", n2)
# else:
#     print("Max Value is :: ", n3)

# Write a Program to check given Num is Armstrong or Not??

# n = int(input("Enter Some String :: "))
# n_s = str(n)
# b = len(n_s)
# total = 0
# armstrong = n
#
# for i in n_s:
#     total = total + (int(i) ** b)
# print(total)
#
# if total == armstrong:
#     print("Given Num is a Armstrong :: ", n)
# else:
#     print("Given Num is Not a Armstrong :: ", n)

# Write a Program to Print Armstrong numbers b/w 1 - 1000

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

# Write a Program to Reverse a Given Number

# n = int(input("Enter Some Number :: "))
# n_s = str(n)
# i = len(n_s) - 1
# rev = ''
#
# while i >= 0:
#     rev = rev + n_s[i]
#     i = i - 1
# print(rev)
#
# # for i in range(0, len(n_s)):
# #     rev = n_s[i] + rev
# # print(rev)

# Write a Program to Reverse a Given Number without -ve

# n = int(input("Enter Some Number :: "))
#
# s = str(n)
# # i = len(s) - 1
# rev = ''

# while i > 0:
#     rev = rev + s[i]
#     i = i - 1
#     if i == 0:
#         rev = s[i] + rev
# print(rev)


# lst = [12, 14, 3, 2, 56, 54, 2, 45]

# raja = 'Bangalore'
# uma = 'Bangalore'
# prasanna = 'Bangalore'
# swathi = 'Bangalore'
#
# print(id(raja))
# print(id(uma))
# print(id(prasanna))
#
# swathi = 'ATP'
# print(id(swathi))

# lst = [10, 'raja', 20, 10, 30, True]


# print(type(lst))
# print(lst)

# lst.append(30)
# print(lst)
#
# lst.extend([70, 80])
# print(lst)

# lst.pop(3)
# print(lst)

# lst.clear()
# print(lst)

# del lst[0]
# print(lst)

# lst.reverse()
# print(lst)

# s = 'raja' * 3
# print(s)

# s = 'raja' * 3.5
# print(s)        # TypeError: can't multiply sequence by non-int of type 'float'

# s = 'raja' * 0b1111
# print(s)

# s = 'raja' * 0o1111
# print(s)

# s = 'raja' * 0x1111
# print(s)

# s = input("Enter Some String :: ")
#
# for i in range(0, len(s)):
#     print("Each Char in a Given String is -->> {} ,and it's position is -->> {}".format(s[i], i))

# class Student:
#     """ This is a Student class to check self is a current object reference """
#     def __init__(self):
#         print(id(self))
#
#
# s = Student()
# print(id(s))
#
# print(Student.__doc__)
# help(Student)

# class Employee:
#
#     """ Constructor will be executed once for an Object creation"""
#
#     def __init__(self):
#         print("Constructor Execution")
#
#
# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
# e4 = Employee()

# class Student:
#     """Inside a Class we can declare any no.of constructors, but Python is always consider last one only."""
#
#     def __init__(self):
#         print("0-arg constructor")
#
#     def __init__(self, x):
#         print("1-arg constructor")
#
#
# s1 = Student(10)
# s2 = Student(20)

# class Student:
#     def __init__(self, name, rollNo):
#         print("Constructor Execution is for declare and initialize Instance Variables")
#         self.name = name
#         self.rollNo = rollNo
#
#     def display(self):
#         print("Method Execution is for to devlop Business Logic")
#         print("Hello my Name is :: ", self.name)
#         print("My RollNo is :: ", self.rollNo)
#
#
# s = Student('raja', 395)
# s.display()

# class Employee:
#     company = 'Google'
#
#     def __init__(self, eno, ename):
#         self.eno = eno
#         self.ename = ename
#
#     def display(self):
#         print("Hello Employee Name is :: ", self.ename)
#         print("Employee No is :: ", self.eno)
#
#
# e1 = Employee(ename='raja', eno=395)
# print(e1.company)
# print(id(e1))
# e2 = Employee(ename='uma', eno=116)
# print(e1.company)
# print(id(e2))
# print("company Class Variable Address for diff Objects is Same")
# print(id(e1.company))
# print(id(e2.company))

# class Student:
#     clgName = 'SVEC'
#
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         print("Hi, Your Name is :: ", self.name)
#         print("Your Marks are :: ", self.marks)
#
#     def grade(self):
#         if self.marks >= 60:
#             print("A Grade")
#         elif 50 <= self.marks < 60:
#             print("B Grade")
#         elif 35 <= self.marks < 50:
#             print("C Grade")
#         else:
#             print("Your Failed :: ")
#
#
# students = int(input("Enter No.Of Students :: "))
#
# for student in range(1, students + 1):
#     name = input("Enter Student Name :: ")
#     marks = int(input("Enter Student Marks :: "))
#     s1 = Student(name, marks)
#
#     s1.display()
#     s1.grade()

# class Employee:
#
#     def __init__(self, eno, ename, esal):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#
#     def display(self):
#         print("Employee Number is :: ", self.eno)
#         print("Employee Name is :: ", self.ename)
#         print("Employee Salary is :: ", self.esal)
#
#
# class Test:
#
#     @staticmethod
#     def modify(emp):
#         emp.esal = emp.esal + 10000
#         emp.display()
#
#
# e = Employee(eno=395, ename='Raja', esal=70000)
# Test.modify(e)

# class Outer:
#
#     def __init__(self):
#         print("Outer Class Constructor ::")
#
#     class Inner:
#
#         def __init__(self):
#             print("Inner Class Constructor ::")
#
#         def m1(self):
#             print("Inner Class Instance Method :: ")
#
#
# # o = Outer()
# # i = o.Inner()
# # i.m1()
#
# Outer().Inner().m1()


# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         self.dob = self.DOB()
#
#     def display(self):
#         print("Name of the Person is :: ", self.name)
#         self.dob.display()
#
#     class DOB:
#
#         def __init__(self):
#             self.dd = 15
#             self.mm = 3
#             self.yyyy = 1995
#
#         def display(self):
#             print("DOB is:: {} {} {} ".format(self.dd, self.mm, self.yyyy))
#
#
# p = Person('Raja')
# p.display()

# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
#     def __add__(self, other):
#         total = 0
#         total = self.pages + other.pages
#         b = Book(total)
#         return b
#
#     def __str__(self):
#         return "The Number of Pages are :: " + str(self.pages)
#
#
# b1 = Book(100)
# b2 = Book(200)
# b3 = Book(300)
# print(b1 + b2)
# print(b1 + b3)
# print(b1)
# print(b1 + b2 + b3)
# print(type(b1 + b2 + b3))

# s = 'hello'
# # print(s * 10)
#
# for x in range(0, 10):
#     print(s)

# for i in range(0, 11):
#     print(i)

# n = int(input("Enter Some Number :: "))
# even = []
# odd = []
# even_c = 0
# odd_c = 0
# for i in range(0, n + 1):
#     if i % 2 == 0:
#         even_c = even_c + 1
#         even.append(i)
#     else:
#         odd_c = odd_c + 1
#         odd.append(i)
# print("Even Numbers b/w 0 to 20 :: ", even, "and it's count is :: ", even_c)
# print("Odd Numbers b/w 0 to 20 :: ", odd, "and it's count is :: ", odd_c)

# n = int(input("Enter Some Number :: "))
# for i in range(n, 0,  -1):
#     print(i)

# lst = eval(input("Enter Some List :: "))
# total = 0
#
# for i in range(0, len(lst)):
#     if type(lst[i]) == int:
#         total = total + lst[i]
#     else:
#         total = total + ord(lst[i])
# print(total)

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# n = int(input("Enter Some Number :: "))
# total = 0
# i = 0
#
# while i <= n:
#     total = total + i
#     i = i + 1
# print(total)

# name = ''
# while name != 'raja':
#     name = input("Enter Some Name :: ")
# else:
#     print("Thanks for the Conformation")

# s1 = 'raja'
# s2 = 'raja'
# s1 = [10, 20, 30]
# s2 = [10, 20, 30]
# s1 = (10, 20, 30)
# s2 = (10, 20, 30)
# # for Immutable Objs, if Content is same in that case same obj will be reused.
# # for Immutable Objs, if Content is Not same in that case new Objs will be Created.
# # for Mutable Objs, Irrespective of Content different objs will be Created.
# print(id(s1))
# print(id(s2))
# print(s1 is s2)
# print(s1 == s2)

# import sys
# lst = [10,20, 30, 40, 50, 60, 70, 80, 90, 20]
# t = (10,20, 30, 40, 50, 60, 70, 80, 90, 20)
#
# print("Size of List is :: ", sys.getsizeof(lst))
# print("Size of tuple is :: ", sys.getsizeof(t))

# d = {[10, 20]: 'raja'}
# print(d)

# d = {'raja': [10, 20]}
# print(d)

# d = {(10, 20): 'raja'}
# print(d)

# d = {'raja': (10, 20)}
# print(d)

# class Human:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print("Name of a Person is :: ", self.name)
#         print("age of ", self.name, "is :: ", self.age)
#
#
# obj = Human('raja', 27)
# obj.display()
# print(obj.__dict__)

# import sys
# lst = [10,20, 30, 40, 50, 60, 70, 80, 90, 20]
# s = {10, 20, 30, 40, 50, 60, 70, 80, 90, 20}
# print(type(s))
# print("Size of List is :: ", sys.getsizeof(lst))
# print("Size of set is :: ", sys.getsizeof(s))


