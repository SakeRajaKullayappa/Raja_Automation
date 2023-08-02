# 1) Fibonacci Series b/w 10 to 20?

# n1 = 10
# n2 = 11
# total = 0
# for i in range(12, 21):
#     total = n1 + n2
#     print(total, end=' ')
#     n1 = n2
#     n2 = total
# o/p ==>> 21 32 53 85 138 223 361 584 945

# def fibonacci(n1, n2):
#     total = 0
#     for i in range(12, 21):
#         total = n1 + n2
#         print(total, end=' ')
#         n1 = n2
#         n2 = total
#
#
# fibonacci(10, 11)
# o/p ==>> 21 32 53 85 138 223 361 584 945

# 2) Factorial for given number

n = int(input("Enter Some Number :: "))
factorial = 1
if n < 0:
    print("Factorial is not exist for -ve Numbers")
elif n == 0 & n == 1:
    print("Factorial for 0 and 1 is 1")
else:
    for i in range(2, n + 1):
        factorial = factorial * i
print(factorial)





