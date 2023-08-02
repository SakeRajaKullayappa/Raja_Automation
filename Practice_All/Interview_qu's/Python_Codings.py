# # Write a Program to find out common letters b/w given two Strings
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# output = ''
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j]:
#             output = output + s1[i]
# print("common letters b/w given two Strings are :: ", output)


# # Write a Program to find out common letters b/w given two Strings without duplicates
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# output = ''
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j] and s1[i] not in output:
#             output = output + s1[i]
# print("common letters b/w given two Strings are :: ", output)


# # Write a Program to find out common letters b/w given two Strings with no. of times
# s1 = input("Enter First String :: ")
# s2 = input("Enter Second String :: ")
# output = ''
# count = {}
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j]:
#             output = output + s1[i]
#             if s1[i] not in count:
#                 count[s1[i]] = 1
#             else:
#                 count[s1[i]] = count[s1[i]] + 1
# print("common letters b/w given two Strings are :: ", output)
# print("common letters b/w given two Strings are with no. of times ::", count)


# # Write a Program to find out common words b/w given two Strings
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


# # Write a Program to find out common words b/w given two Strings without Duplicates
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
#             if lst1[i] == lst2[j]:
#                 output.append(lst1[i])
#                 if lst1[i] not in count:
#                     count[lst1[i]] = 1
#                 else:
#                     count[lst1[i]] = count[lst1[i]] + 1
#
# print("common letters b/w given two Strings are :: ", output)
# print("common letters b/w given two Strings are with no. of times ::", count)


# # Write a Program to print dictionary by adding given Two lists with same length
# lst1 = [10, 20, 30]
# lst2 = ['Raja', 'ComViva', 'Emphasis']
# d = {}
# for i in range(0, len(lst1)):
#     for j in range(i, i + 1):
#         d.__setitem__(lst1[i], lst2[j])
# print("dictionary by adding given Two lists with equal length :: ", d)
#
# d = dict(zip(lst1, lst2))
# print("dictionary by adding given Two lists with equal length :: ", d)


# # Write a Program to Find missing Number from a Given Array
# array = [1, 2, 4, 5, 6, 7]
# n = array[-1]
# print(n)
# sum1 = 0
#
# total = n * (n + 1) // 2
# print("sum of n no's is :: ", total)
# sum1 = sum1 + sum(array)
# print("sum of array elements is :: ", sum1)
# print("missing number from array is :: ", total - sum1)


# # Write a Program to Print Min Diff b/w two elements which are presented inside a List
# lst = [10, 45, 32, 74, 51, 18, 48, 25]
# min_diff = 999 * 99
# for i in range(0, len(lst)):
#     for j in range(i, len(lst)):
#         if lst[i] > lst[j]:
#             get = (lst[i], lst[j])
#             (lst[j], lst[i]) = get
# print("list of elements with shorting is :: ", lst)
#
# for x in range(0, len(lst) - 1):
#     if lst[x + 1] - lst[x] < min_diff:
#         min_diff = lst[x + 1] - lst[x]
# print("Min Diff b/w two elements is :: ", min_diff)


# Write a Program to Print Sum of two elements which are presented inside a List is equal to 55
lst = [23, 67, 85, 4, 9, 8, 43, 32]
sum1 = int(input("Enter Some Number :: "))
for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == sum1:
            print(lst[i], lst[j])

# right = lst[len(lst) - 1]
# print(right)
# left = lst[0]
# print(left)
#
# for x in range(0, len(lst)):
#     if (right + left) > sum1:
#         right = right - 1
#
#     elif (right + left) < sum1:
#         left = left - 1
#
#     elif (right + left) == sum1:
#         right = right - 1
#         left = left + 1


