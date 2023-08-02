# # 1 1 1 1 1
# # 2 2 2 2
# # 3 3 3
# # 4 4
# # 5
# n = int(input("Enter Some Number :: "))
# for i in range(1, n + 1):
#     for j in range(i, i + 1):
#         print((str(j) + " ") * (n - i))
import time

# s = input("Enter Some String :: ")
# index = int(input("Enter Some Number :: "))
# output = ''
# output2 = ''
# for i in range(0, len(s)):
#     if i == index:
#         output = output + s[i]
#     else:
#         output2 = output2 + s[i]
# print(output)
# print(output2)

# d = {'a': 100, 'b': 200, 'c': 300}
# values = list(d.values())
# print(values)
# total = 0
# for i in range(0, len(values)):
#     total = total + values[i]
# print(total)

# s = input("Enter Some String :: ")
# vowels = "aeiouAEIOU"
# cons = ''
# vow = ''
# for i in s:
#     if i not in vowels:
#         cons = cons + i
#     else:
#         vow = vow + i
#
# print(vow)
# print(cons)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
#
# driver.get("https://www.google.com/")
# time.sleep(2)
#
# search = driver.find_element(By.XPATH, "//input[@type = 'text']")
# search.send_keys("Happy")
# time.sleep(4)
#
# search_auto = driver.find_elements(By.XPATH, "//div[@id = 'Alh6id']//li")
# print(len(search_auto))
#
# for search_auto_ele in search_auto:
#     if " anniversary wishes" in search_auto_ele.text:
#         time.sleep(3)
#         search_auto_ele.click()
#         break
#
# time.sleep(4)
# driver.close()


# n = int(input("Enter Some Number :: "))
#
# for i in range(2, n + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)


# lst = [10, 29, 30, 40, 50, 60]
# index = int(input("Enter Some Number :: "))
# j = len(lst) - 1
# print(j)
# output = []
# for i in range(0, len(lst)):
#     if i > index:
#         while j > index:
#             output.append(lst[j])
#             j = j - 1
#     else:
#         output.append(lst[i])
# print(output)


#
# s = input("Enter Some String :: ")
# i = len(s) - 1
# output = ''
# while i >= 0:
#     output = output + s[i]
#     i = i - 1
#
# print(output)

# s = input("Enter Some String :: ")
# rev = ''
# for i in s:
#     rev = i + rev
# print(rev)





















































































