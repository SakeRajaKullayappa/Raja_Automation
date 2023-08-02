import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(upper)






















#
# class Password_Set:
#
#     def __init__(self, password=''):
#         self.password = password
#
#     def _lower(self):
#         lower = any(c.islower() for c in self.password)
#         return lower
#
#     def _upper(self):
#         upper = any(c.isupper() for c in self.password)
#         return upper
#
#     def _digit(self):
#         digit = any(c.isdigit() for c in self.password)
#         return digit
#
#     def pwdValidation(self):
#         lower = self._lower()
#         upper = self._upper()
#         digit = self._digit()
#
#         length = len(self.password)
#
#         report = lower and upper and digit and length >= 8
#         if report:
#             return True
#
#         elif not lower:
#             print("please enter at-least one lower case :: ")
#
#         elif not upper:
#             print("please enter at-least one upper case :: ")
#
#         elif not digit:
#             print("please enter at-least one digit :: ")
#
#         elif length >= 8:
#             print("please enter more than 8 characters :: ")
#
#         else:
#             pass
#
#
# pwd = Password_Set("Raja1234")
# print(pwd.pwdValidation())

