# cash = 10
# print(cash)

# ca$h = 10
# print(ca$h)
# Error:: Invalid Syntax (Python Allows _ Special Char only)


# import keyword
# print(keyword.kwlist)
# c = 0
# for k in keyword.kwlist:
#     c = c + 1
# print(c)

# a = 10
# b = 20
# c = a < b
# print(c)
# print(type(c))

# s = 'raja'
# print(id(s))
# print(type(s))

# s = '''raja
#      Python Automation'''
# print(id(s))
# print(type(s))

# s = 'rajaS'
# slice_code = s[1:4]
# print(slice_code)
# for i in range(0, len(slice_code)):
#     print(slice_code[i], 'its Position is :: ', i)

# s = 'PythonAutomation'
# print(s[3:8])
#
# start_ind = s[3]
# print(start_ind)
# end_ind = s[7]
# print(end_ind)

# s = "Raja Python Automation"
# r = reversed(s)
# output = ''.join(r)
# print(output)

# s = input("Enter Some String :: ")
# s_lst = s.split()
# i = len(s_lst) - 1
# rev = []
# output = ' '
#
# while i >= 0:
#     rev.append(s_lst[i])
#     i = i - 1
# print(rev)
# output = output.join(rev)
# print(output)

# s = input("Enter Some String :: ")
# s_lst = s.split()
# lst = []
# output = ' '
#
# for i in range(0, len(s_lst)):
#     lst.append(s_lst[i][::-1])
# print(lst)
# output = output.join(lst)
# print(output)

# s = input("Enter Some String :: ")
# s_lst = s.split()
# lst = []
# for i in range(0, len(s_lst)):
#     if i % 2 == 0:
#         lst.append(s_lst[i][::-1])
#     else:
#         lst.append(s_lst[i])
# print(lst)
# output = ' '.join(lst)
# print(output)

# s = input("Enter Some String :: ")
# s_lst = s.split()
# lst = []
# for i in range(0, len(s_lst)):
#     if i % 2 != 0:
#         lst.append(s_lst[i][::-1])
#     else:
#         lst.append(s_lst[i])
# print(lst)
# output = ' '.join(lst)
# print(output)

# s = input("Enter Some String :: ")
# i = 0
# output = ''
# output1 = ''
#
# while i < len(s):
#     output = output + s[i]
#     i = i + 2
# print("Even Index Chars :: ", output)
#
# j = 1
# while j < len(s):
#     output1 = output1 + s[j]
#     j = j + 2
# print("Odd Index Chars :: ", output1)

# # B4A1D3
# # ABD134
# string = []
# digit = []
#
# s = input("Enter Some String :: ")
#
# for ch in s:
#     if ch.isalpha():
#         string.append(ch)
#     else:
#         digit.append(ch)
# print(string)
# print(digit)
#
# for i in range(0, len(digit)):
#     for j in range(i + 1, len(digit)):
#         if digit[i] > digit[j]:
#             get = (digit[i], digit[j])
#             (digit[j], digit[i]) = get
# print(digit)
# output_digit = ''.join(digit)
# print(output_digit)
#
# for x in range(0, len(string)):
#     for y in range(x + 1, len(string)):
#         if string[x] > string[y]:
#             get = (string[x], string[y])
#             (string[y], string[x]) = get
# print(string)
# output_string = ''.join(string)
# print(output_string)
#
# output = output_string + output_digit
# print(output)



