# Write a Program to check 1st and last ele's are same in given List

# lst = [10, 20, 40, 70, 20, 10, 20, 10]
# i = 0
#
# if lst[i] == lst[len(lst) - 1]:
#     print("First and Last elements in a given list are same :: ")
# else:
#     print("First and Last elements in a given list are not same :: ")

# for i in range(0, len(lst)):
#     if i == 0:
#         for j in range(len(lst)-1, len(lst)):
#             if lst[i] == lst[j]:
#                 print("Same")
#             else:
#                 print("Not Same")
#     else:
#         break

# Write a Program to check 4th and 5th ele's are same in given List
# lst = [10, 20, 40, 70, 20, 10, 20, 20]
# b = len(lst)  # 8
# for i in range(0, len(lst)):
#     if i == len(lst) - 2:
#         for j in range(len(lst) - 1, len(lst)):
#             if lst[i] == lst[j]:
#                 print("4th and 5th elements in a given list are same")
#             else:
#                 print("4th and 5th elements in a given list are not same")

# Write a Program to Extend Lists without using append/extend functions.

# lst1 = [10, 20, 30]
# lst2 = ['raja', 'uma', 'MBA']
#
# lst1[:0:] = lst2
# print(lst1)
#
# lst2[:0:] = lst1
# print(lst2)
#
# # lst1.append(lst2)
# # print(lst1)
#
# # lst1.extend(lst2)
# # print(lst1)


# Write a Program to separate String and int from a given list

# lst = [10, 20, 30, 'raja', 'uma', 'MBA']
# int_lst = []
# str_lst = []
#
# for i in range(0, len(lst)):
#     if type(lst[i]) == int:
#         int_lst.append(lst[i])
#     else:
#         str_lst.append(lst[i])
# print(int_lst)
# print(str_lst)

# Write a Program to Search Element in a given List

# lst = [10, 20, 30, 'raja', 'uma', 'MBA']
# search_ele = input("Enter Some String :: ")
# output = []
# for i in range(0, len(lst)):
#     if lst[i] == search_ele:
#         output.append(lst[i])
# print(output)

# Write a Program to Print Last Element of a List
# lst = [10, 20, 30, 'raja', 'uma', 'MBA']
# output = []
# for i in range(0, len(lst)):
#     if lst[i] == lst[len(lst) - 1]:
#         output.append(lst[i])
#     # print(lst[i])
# print(output)

# Write a Program to Sum of all the ele in a List
# lst = [10, 20, 30, 40, 50, 60]
# total = 0
#
# for i in range(0, len(lst)):
#     total = total + lst[i]
# print(total)

# Write a Program to triple all the elements in a given List

# lst = [8, 4, 2, 6, 5, 7]
# output = []
# for i in range(0, len(lst)):
#     output.append(lst[i]**3)
# print(output)

# Swapping Two Numbers in a given List without 3rd reference

# lst = [8, 4, 2, 6, 5, 7]
# print("Before Swapping :: ", lst)
#
# for i in range(0, len(lst)):
#     if i == 2:
#         for j in range(len(lst) - 1, len(lst)):
#             get = (lst[i], lst[j])
#             (lst[j], lst[i]) = get
# print("After Swapping :: ", lst)

# Write a Program to print the list without duplicates from a given list

# lst = [10, 20, 40, 70, 20, 10, 20, 10]
# output = []
# print("with duplicates :: ", lst)
# for i in range(0, len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] != lst[j] and lst[i] not in output:
#             output.append(lst[i])
# print("without duplicates :: ", output)

# Write a Program to print duplicates from a given list

# lst = [10, 20, 40, 70, 20, 10, 20, 10]
# output = []
#
# for i in range(0, len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j] and lst[i] not in output:
#             output.append(lst[i])
# print("duplicates :: ", output)

# Write a Program to Print Second Largest Number from a given list??

# lst = [10, 50, 20, 60, 80, 30, 15, 40]
#
# for i in range(0, len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] > lst[j]:
#             get = (lst[i], lst[j])
#             (lst[j], lst[i]) = get
# print("After Sorting :: ", lst)
# print("Second Largest Element :: ", lst[len(lst) - 2])

# Write a Program to Print List with sum of each elements from given two lists

# lst1 = [10, 20, 30, 40, 60, 20, 70, 20]
# lst2 = [90, 80, 70, 60, 50, 30]
# lst3 = []
# if len(lst1) < len(lst2):
#     lst1 = lst1 + [0] * (len(lst2) - len(lst1))
#     for i in range(0, len(lst1)):
#         for j in range(i, i + 1):
#             lst3.append(lst1[i] + lst2[j])
# else:
#     lst2 = lst2 + [0] * (len(lst1) - len(lst2))
#     for i in range(0, len(lst1)):
#         for j in range(i, i + 1):
#             lst3.append(lst1[i] + lst2[j])
# print(lst3)

# lst1 = ['raja', 'uma', 'mom', 'dad']
# lst2 = ['self', 'wife', 'mother', 'father', 'sindhu', 'ramesh']
# output = []
# if len(lst1) < len(lst2):
#     lst1 = lst1 + [''] * (len(lst2) - len(lst1))
#     print(lst1)
#     for i in range(0, len(lst1)):
#         for j in range(i, i + 1):
#             output.append(lst1[i] + lst2[j])
# else:
#     lst2 = lst2 + [''] * (len(lst1) - len(lst2))
#     print(lst2)
#     for i in range(0, len(lst1)):
#         for j in range(i, i + 1):
#             output.append(lst1[i] + lst2[j])
# print(output)

# Write a Program to Print List of elements are in reverse from specified index

# lst = [10, 20, 'raja', 60, 80, 30, 'uma']
# index = int(input("Enter Some Number :: "))  # 2
# j = len(lst) - 1
# lst_rev = []
# for i in range(0, len(lst)):
#     if i < index:
#         lst_rev.append(lst[i])
#     else:
#         while j >= index:
#             lst_rev.append(lst[j])
#             j = j - 1
# print(lst_rev)

# Write a Program to Print Sum of two elements which are presented inside a List is equal to 55

# lst = [23, 67, 85, 12, 9, 8, 43, 32]
# total = int(input("Enter Some Sum Value :: "))
# for i in range(0, len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] + lst[j] == total:
#             print(lst[i], lst[j], end=',')
