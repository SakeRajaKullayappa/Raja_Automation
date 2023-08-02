# Write a Program to check weather given Value is already present in a Dict or Not??

# d = {'Raja': 'Python Tester', 'Uma': 'Business Analyst', 'Teja': 'Python Developer', 'Company': 'Sony'}
# exist_value = input("Enter Some String :: ")
#
# # for k, v in d.items():
# #     if v == exist_value:
# #         print("Given Value is exist in a Dict")
# #     else:
# #         print("Given Value is Not exist in a Dict")
#
# values = d.values()
#
# if exist_value in values:
#     print("Given Value is exist in a Dict")
# else:
#     print("Given Value is Not exist in a Dict")

# Write a Program to add given two Lists in to Dict

# lst1 = ['Raja', 'Uma', 'Pullamma', 'Nallaiah']
# lst2 = ['Software', 'wife', 'Mother', 'Father', 'Tech M', 'Office']
# d = {}
#
# if len(lst1) < len(lst2):
#     lst1 = lst1 + [''] * (len(lst2) - len(lst1))
#     print(lst1)
#     for i in range(0, len(lst1)):
#         for j in range(i, i + 1):
#             d.__setitem__(lst1[i], lst2[j])
# else:
#     lst2 = lst2 + [''] * (len(lst1) - len(lst2))
#     print(lst2)
#     for i in range(0, len(lst1)):
#         for j in range(i, i + 1):
#             d.__setitem__(lst1[i], lst2[j])
# print(d)


# Write a Program to print dictionary without having duplicate values

# d = {1: 'uma', 2: 'raja', 3: 'capgemini', 4: 'balaiah', 5: 'raja'}
# empty = {}
# lst = []
#
# for k, v in d.items():
#     if v not in lst:
#         lst.append(v)
#         empty[k] = v
# print(empty)

# Write a Program to print sum of dictionary values

# d = {'uma': 1, 'raja': 2, 'capgemini': 3, 'balaiah': 4, 'sony': 5}
# total = 0
#
# for k, v in d.items():
#     total = total + v
# print(total)

# Write a Program to Print dictionary with age value is more than 25

# d = {'raja': 28, 'uma': 24, 'mom': 46, 'dad': 50, 'jt.ntr': 12}
# age = []
# person = {}
#
# for k, v in d.items():
#     if v >= 25:
#         age.append(v)
#         person[k] = v
# print(person)


# fruits = {'apple': 10, 'banana': 40, 'grap': 60, 'orange': 20}
# keys = {}
# values = []
#
# for k, v in fruits.items():
#     if v == 10:
#         fruits['apple'] = 100
#         # values.append(v)
#         keys[k] = v
# print(fruits)

# set1 = {1, 2, 3, 4, 5, 6, 7}
# set2 = {3, 4, 5, 8, 9, 11, 12}
# output = set()
# output = set1.intersection(set2)
# print(output)

# n = int(input("Enter Some Number :: "))
# n_s = str(n)
# rev_n_s = ''
# for i in n_s:
#     rev_n_s = i + rev_n_s
# print(rev_n_s, "and its type is ::", type(rev_n_s))
# rev_n = int(rev_n_s)
# print(rev_n, "and its type is ::", type(rev_n))
#
# if n == rev_n:
#     print("It's a Palindrome")
# else:
#     print("It's Not a Palindrome")

# d = {'k1': 10, 'k2': 20, 'k3': 30, 'k4': 40, }
#
# for key in d.keys():
#     d[key] = d[key] + 8
# print(d)

# lst = [10, 20]
# shallow_copy = lst
# deep_copy = [10, 20]
#
# print("ID for lst Obj is ::", id(lst))
# print("ID for shallow_copy Obj is ::", id(shallow_copy))
# print("ID for deep_copy Obj is ::", id(deep_copy))




