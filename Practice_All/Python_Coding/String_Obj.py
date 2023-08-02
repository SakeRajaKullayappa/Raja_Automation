# Write a Program to Remove Punctuations from a Given String
# i/p : $S@O#N*%Y!!~I&*N#&D!@I^$A$P@R#I*%V!!~A&*T#&E!@L^$I$M@I#T*%E!!~D&
# o/p : SONYINDIAPRIVATELIMITED

# s = input("Enter Some String :: ")
# punctuations = "!@#$%^&*()_-+={}[]:"'<>?,./`~'
# output = ""
#
# for i in s:
#     if i not in punctuations:
#         output = output + i
#
# print(output)

# Write a Program to Remove all WhiteSpaces from a Given String
# i/p: SONY INDIA PRIVATE LIMITED
# o/p: SONYINDIAPRIVATELIMITED

# s = input("Enter Some String :: ")
# punctuations = " "
# output = ""
#
# for i in s:
#     if i not in punctuations:
#         output = output + i
#
# print(output)

# Write a Program to Count the occurrence of each word in a given String
# i/p: Python Automation Testing in both Manual and Automation Testing
# o/p: {'Python': 1, 'Automation': 2, 'Testing': 2, 'in': 1, 'both': 1, 'Manual': 1, 'and': 1}

# s = input("Enter Some String :: ")
# s_lst = s.split()
# count = {}
#
# for word in s_lst:
#     if word not in count:
#         count[word] = 1
#     else:
#         count[word] = count[word] + 1
#
# print(count)

# Write a Program to Count the occurrence of each char in a given String
# i/p: PythonAutomationTesting
# o/p: {'A': 1, 'u': 1, 't': 3, 'o': 2, 'm': 1, 'a': 1, 'i': 2, 'n': 2, 'T': 1, 'e': 1, 's': 1, 'g': 1}


# s = input("Enter Some String :: ")
# count = {}
#
# for char in s:
#     if char not in count:
#         count[char] = 1
#     else:
#         count[char] = count[char] + 1
#
# print(count)


# Write a Program to count no.of Upper and Lower case letters in a given String

# s = input("Enter Some String :: ")
# upper = 0
# lower = 0
# up_char = ""
# lo_char = ""
#
# for i in s:
#     if i.isupper():
#         upper = upper + 1
#         up_char = up_char + i
#     else:
#         lower = lower + 1
#         lo_char = lo_char + i
# print(upper, up_char)
# print(lower, lo_char)


# Write a Program to Check Given String is Palindrome or Not ??

# s = input("Enter Some String :: ")
# i = len(s) - 1
# rev = ""
#
# while i >= 0:
#     rev = rev + s[i]
#     i = i - 1
#
# # for i in s:
# #     rev = i + rev
# #
# print(rev)
# if rev == s:
#     print("Given String is a Palindrome")
# else:
#     print("Given String is Not a Palindrome")


# Write a Program to check given Strings are Anagram or not??

# s1 = input("Enter Some String :: ")
# s2 = input("Enter Some String :: ")

# if sorted(s1) == sorted(s2):
#     print("Given Two Strings are Anagrams")
# else:
#     print("Given Two Strings are Not a Anagrams")
#
# s1_lst = list(s1)
# s2_lst = list(s2)
# print("Before Sorting s1:: ", s1_lst)
# print("Before Sorting s2:: ", s2_lst)
#
# for i in range(0, len(s1_lst)):
#     for j in range(i + 1, len(s1_lst)):
#         if s1_lst[i] > s1_lst[j]:
#             get = (s1_lst[i], s1_lst[j])
#             (s1_lst[j], s1_lst[i]) = get
# print("After Sorting s1:: ", s1_lst)
#
# for x in range(0, len(s2_lst)):
#     for y in range(x + 1, len(s2_lst)):
#         if s2_lst[x] > s2_lst[y]:
#             get = (s2_lst[x], s2_lst[y])
#             (s2_lst[y], s2_lst[x]) = get
# print("After Sorting s2:: ", s2_lst)
#
# if ''.join(s1_lst) == ''.join(s2_lst):
#     print("Given Two Strings are Anagrams")
# else:
#     print("Given Two Strings are Not Anagrams")


# Write a program to print common letters b/w given two Strings

# s1 = input("Enter Some String :: ")
# s2 = input("Enter Some String :: ")
#
# output = ''
#
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j] and s1[i] not in output:
#             output = output + s1[i]
# print("CommonLetters b/w Given Two Strings are :: ", output)

# Write a Program to Print reverse of a given String with removal of duplicate

# s = input("Enter Some String :: ")
# rev = ''
#
# # for i in s:
# #     if i not in rev:
# #         rev = i + rev
# # print(rev)
#
# i = len(s) - 1
#
# while i >= 0:
#     if s[i] not in rev:
#         rev = rev + s[i]
#     i = i - 1
# print(rev)

# Write a Program to Print reverse order of words from a given String

# s = input("Enter Some String :: ")
# s_lst = s.split()
# i = len(s_lst) - 1
# rev = []
# output = ''
#
# while i >= 0:
#     rev.append(s_lst[i])
#     i = i - 1
# print(rev)
# output = " ".join(rev)
# print(output)

# Write a Program to Print Internal Content reverse order of each words from a given String

# s = input("Enter Some String :: ")
# s_lst = s.split()
# i = len(s_lst) - 1
# rev = []
# output = ''
#
# while i >= 0:
#     rev.append(s_lst[i][::-1])
#     i = i - 1
# print(rev)
# output = " ".join(rev)
# print(output)


# Write a Program to Print Internal Content reverse order of each first words from a given String

# s = input("Enter Some String :: ")
# s_lst = s.split()
# first_rev = []
# output = ''
#
# for i in range(0, len(s_lst)):
#     if i % 2 == 0:
#         first_rev.append(s_lst[i][::-1])
#     else:
#         first_rev.append(s_lst[i])
# print(first_rev)
# output = " ".join(first_rev)
# print(output)

# Write a Program to Print Internal Content reverse order of each second words from a given String

# s = input("Enter Some String :: ")
# s_lst = s.split()
# first_rev = []
# output = ''
#
# for i in range(0, len(s_lst)):
#     if i % 2 == 0:
#         first_rev.append(s_lst[i])
#     else:
#         first_rev.append(s_lst[i][::-1])
# print(first_rev)
# output = " ".join(first_rev)
# print(output)


# Write a Program to print Vowels and Constants in a given String

# s = input("Enter Some String :: ")
# v = "aeiouAEIOU"
# vowels = ""
# constants = ""
# v_count = 0
# c_count = 0
#
# for i in s:
#     if i in v:
#         v_count = v_count + 1
#         vowels = vowels + i
#     else:
#         c_count = c_count + 1
#         constants = constants + i
#
# print(vowels, v_count)
#
# print(constants, c_count)


# Write a Program to print a String without having specified index char

# s = input("Enter Some String :: ")
# specified_index_char = 5
# output = ''
#
# for i in range(0, len(s)):
#     if i != specified_index_char:
#         output = output + s[i]
# print(output)


# Write a Program to find out common letters b/w given two Strings

# s1 = input("Enter Some String :: ")
# s2 = input("Enter Some String :: ")
# common = ''
#
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j]:
#             common = common + s1[i]
# print(common)


# Write a Program to find out common letters b/w given two Strings without duplicates

# s1 = input("Enter Some String :: ")
# s2 = input("Enter Some String :: ")
# common = ''
#
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j] and s1[i] not in common:
#             common = common + s1[i]
# print(common)


# Write a Program to find out common letters b/w given two Strings with no. of times

# s1 = input("Enter Some String :: ")
# s2 = input("Enter Some String :: ")
# common = ''
# common_count = 0
#
# for i in range(0, len(s1)):
#     for j in range(0, len(s2)):
#         if s1[i] == s2[j] and s1[i]:
#             common_count = common_count + 1
#             common = common + s1[i]
# print(common, common_count)


# Write a Program to find out common words b/w given two Strings

# s1 = input("Enter Some String :: ")
# s2 = input("Enter Some String :: ")
# s1_lst = s1.split()
# s2_lst = s2.split()
# print(s1_lst)
# print(s2_lst)
# common = []
# output = ''
#
# for i in range(0, len(s1_lst)):
#     for j in range(0, len(s2_lst)):
#         if s1_lst[i] == s2_lst[j]:
#             common.append(s1_lst[i])
# print(common)
# output = " ".join(common)
# print(output)


# Write a Program to find out common words b/w given two Strings without Duplicates

# s1 = input("Enter Some String :: ")
# s2 = input("Enter Some String :: ")
# s1_lst = s1.split()
# s2_lst = s2.split()
# print(s1_lst)
# print(s2_lst)
# common = []
# output = ''
#
# for i in range(0, len(s1_lst)):
#     for j in range(0, len(s2_lst)):
#         if s1_lst[i] == s2_lst[j] and s1_lst[i] not in common:
#             common.append(s1_lst[i])
# print(common)
# output = " ".join(common)
# print(output)


# Write a Program to Print Following Requirement

# i/p:  B4A1D3
# o/p:  ABD134

# s = input("Enter Some String :: ")
# string = []
# digit = []
#
# for ch in s:
#     if ch.isalpha():
#         string.append(ch)
#     else:
#         digit.append(ch)
#
# for i in range(0, len(digit)):
#     for j in range(i + 1, len(digit)):
#         if digit[i] > digit[j]:
#             get = (digit[i], digit[j])
#             (digit[j], digit[i]) = get
# output_digit = ''.join(digit)
# print(output_digit)
#
# for x in range(0, len(string)):
#     for y in range(x + 1, len(string)):
#         if string[x] > string[y]:
#             get = (string[x], string[y])
#             (string[y], string[x]) = get
# output_string = ''.join(string)
# print(output_string)
#
# output = output_string + output_digit
# print(output)

# Write a Program to Print Following Requirement

# i/p:  a4b3c2
# o/p:  aaaabbbcc

# s = input("Enter Some String :: ")

# output = ''
# for i in range(0, len(s)):
#     if s[i].isalpha():
#         ch = s[i]
#     else:
#         digit = int(s[i])
#         output = output + (ch * digit)
# print(output)

# char = []
# digit = []
# for i in range(0, len(s)):
#     if s[i].isalpha():
#         char.append(s[i])
#     else:
#         digit.append(s[i])
# print(char)
# print(digit)
#
# output = []
# for i in range(0, len(char)):
#     for j in range(i, i + 1):
#         output.append(char[i] * int(digit[j]))
# print(output)
# final_output = ''.join(output)
# print(final_output)

# Write a Program to Print Following Requirement

# i/p:  4a3b2c
# o/p:  aaaabbbcc

# s = input("Enter Some String :: ")
# digit = []
# char = []
#
# for i in range(0, len(s)):
#     if s[i].isnumeric():
#         digit.append(s[i])
#     else:
#         char.append(s[i])
# print(digit)
# print(char)
# output = []
#
# for i in range(0, len(char)):
#     for j in range(i, i + 1):
#         output.append(char[i] * int(digit[j]))
# print(output)
# final_output = ''.join(output)
# print(final_output)

# s = input("Enter Some String :: ")
# result = ''
# for i in range(0, len(s)):
#     if s[i].isnumeric():
#         digit = int(s[i])
#     else:
#         char = s[i]
#         result = result + (char * digit)
# print(result)


# Write a Program to Print Following Requirement

# i/p:  a3z2b4
# o/p:  aaabbbbzz

# s = input("Enter Some String :: ")
# char = []
# digit = []
#
# for i in range(0, len(s)):
#     if s[i].isalpha():
#         char.append(s[i])
#     else:
#         digit.append(s[i])
# print(char)
# print(digit)
#
# output = []
# for x in range(0, len(char)):
#     for j in range(x, x + 1):
#         output.append(char[x] * int(digit[j]))
# print(output)
# final_output = ''.join(sorted(output))
# print(final_output)

# s = input("Enter Some String :: ")
# output = ''
# for i in range(0, len(s)):
#     if s[i].isalpha():
#         char = s[i]
#     else:
#         digit = int(s[i])
#         output = output + (char * digit)
# print(output)
# final_output = ''.join(sorted(output))
# print(final_output)

# Write a Program to Print Following Requirement

# i/p: aaaabbbccz
# o/p: 4a3b2c1z

# s = input("Enter Some String :: ")
#
# output = ''
# previous = s[0]
# c = 1
# i = 1
#
# while i < len(s):
#     if s[i] == previous:
#         c = c + 1
#     else:
#         output = output + str(c) + previous
#         previous = s[i]
#         c = 1
#     if i == len(s) - 1:
#         output = output + str(c) + previous
#     i = i + 1
# print(output)

# Write a Program to Print Following Requirement
# i/p: a4k3b2
# o/p: aeknbd

# s = input("Enter Some String :: ")
# output = ''
#
# for i in range(0, len(s)):
#     if s[i].isalpha():
#         output = output + s[i]
#         ch = s[i]
#     else:
#         digit = int(s[i])
#         new_ch = chr(ord(ch) + digit)
#         output = output + new_ch
# print(output)

# Write a Program to remove duplicates from a given String

# s = input("Enter Some String :: ")
# output = ''
# for ch in s:
#     if ch not in output:
#         output = output + ch
# print(output)


# s = input("Enter Some String :: ")
# s_lst = list(s)
# print(s_lst)
# output = []
#
# for i in range(0, len(s_lst)):
#     for j in range(i + 1, len(s_lst)):
#         if s_lst[i] == s_lst[j] and s_lst[i] not in output:
#             output.append(s_lst[i])
# print(output)
# final_output = ''.join(output)
# print(final_output)


# Write a Program to Print following Requirement
# i/p: ABAABBCA
# o/p: 4A3B1C

# s = input("Enter Some String :: ")
# count = {}
# output = ''
#
# for ch in s:
#     if ch not in count:
#         count[ch] = 1
#     else:
#         count[ch] = count[ch] + 1
# print(count)
#
# for k, v in count.items():
#     output = output + str(v) + k
# print(output)

# Write a Program to Print following Requirement
# i/p: ABAABBCA
# o/p: A4B3C1

# s = input("Enter Some String :: ")
# count = {}
# output = ''
#
# for ch in s:
#     if ch not in count:
#         count[ch] = 1
#     else:
#         count[ch] = count[ch] + 1
# print(count)
#
# for k, v in count.items():
#     output = output + k + str(v)
# print(output)

# Write a Program to Print following Requirement
# i/p: ARAARRCADD
# o/p: 4A1C2D3R

# s = input("Enter Some String :: ")
# count = {}
# output = ''
#
# for ch in s:
#     if ch not in count:
#         count[ch] = 1
#     else:
#         count[ch] = count[ch] + 1
# print(count)
#
# for k, v in sorted(count.items()):
#     output = output + str(v) + k
# print(output)

# Write a Program to Print following Requirement
# i/p: ARAARRCADD
# o/p: A4C1D2R3

# s = input("Enter Some String :: ")
# count = {}
# output = ''
#
# for ch in s:
#     if ch not in count:
#         count[ch] = 1
#     else:
#         count[ch] = count[ch] + 1
# print(count)
#
# for k, v in sorted(count.items()):
#     output = output + k + str(v)
# print(output)

# Write a Program to count of vowels and constants in a given String

# s = input("Enter Some String :: ")
# v = 'a, e, i, o, u, A, E, I, O, U'
# v_c = 0
# c_c = 0
# vowels = ''
# constants = ''
# for ch in s:
#     if ch in v:
#         vowels = vowels + ch
#         v_c = v_c + 1
#     else:
#         constants = constants + ch
#         c_c = c_c + 1
# print("Vowels are :: ", vowels)
# print("Constants are :: ", constants)
# print("Vowel Count is :: ", v_c)
# print("Constants Count is :: ", c_c)
#
# each_v_c = {}
#
# for eav_v in vowels:
#     if eav_v not in each_v_c:
#         each_v_c[eav_v] = 1
#     else:
#         each_v_c[eav_v] = each_v_c[eav_v] + 1
# print("Each Vowel Count is :: ", each_v_c)
