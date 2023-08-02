"""
-->>    Dict is useful to store key, value pair date.
-->>    It is Mutable, Ordered and Allows Duplicates values, not keys
-->>    Dict Items are referred by using keys
-->>    Dict doesnt allow duplicate Keys, even though if we take in that time it will not through an Exception.


"""

# d = {"name": "Raja", "age": 27, "Company": "Sony India Pvt Ltd", "salary": 14.5}

# You can also use the del statement to delete an item from a dictionary.

# del d["salary"]
# print(d)

# You can specify and remove multiple items.

# del d["salary"], d["age"]
# print(d)

# If a non-existent key is specified, a KeyError is raised.

# del d["sony"]
# print(d)

# we can remove all elements

# d.clear()
# print("Dict data after removing all elements ::", d)

# By specifying a key to the pop() method, the item is removed and its value is returned

# removed_value = d.pop("salary")
# print(d)
# print(removed_value)

# By default, specifying a non-existent key raises a KeyError.

# removed_value = d.pop("Role")
# print(d)
# print(removed_value)

# If you pass the second argument as None, its value is returned if the key does not exist. The dictionary remains
# unchanged.

# removed_value = d.pop("Role", None)
# print(d)
# print(removed_value)

# The popitem() method removes an item from the dictionary and returns its key and value as a tuple, (key, value).

# (k, v) = d.popitem()
# print(d)
# print(k)
# print(v)


# ============================ Adding Item to Dict =======================================

# Adding an item to the dictionary is done by using a new index key and assigning a value to it

# d = {"name": "Raja", "age": 27, "Company": "Sony India Pvt Ltd", "salary": 14.5}
#
# d["Location"] = "Bangalore"
# print(d)


# ============================ Accessing Item to Dict =======================================

# d = {'name': 'Raja', 'age': 27, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}

# value = d.get("name")
# print(value)
#
# value1 = d["Location"]
# print(value1)

# ========================================= Copy a Dictionary ================================================

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# d = {'name': 'Raja', 'age': 27, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}

# dict = d
# d["age"] = 28
# print(d)
# print(dict)

# o/p ::    {'name': 'Raja', 'age': 28, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}
#           {'name': 'Raja', 'age': 28, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}

# dict = d.copy()
# d['age'] = 28
# print(d)
# print(dict)

# o/p ::    {'name': 'Raja', 'age': 28, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}
#           {'name': 'Raja', 'age': 27, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}

# Another way to make a copy is to use the built-in method dict().

# d = {'name': 'Raja', 'age': 28, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}
# dict = dict(d)
# d['age'] = 27
# print(d)
# print(dict)

# o/p ::    {'name': 'Raja', 'age': 28, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}
#           {'name': 'Raja', 'age': 27, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}


# You can loop through a dictionary by using a for loop.

# d = {'name': 'Raja', 'age': 27, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}
# for value in d:
#     print(value)

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return
# the values as well.

# ============================== Check if Key Exists in Dictionary ================================================

# To determine if a specified key is present in a dictionary use the in keyword:

# d = {'name': 'Raja', 'age': 27, 'Company': 'Sony India Pvt Ltd', 'salary': 14.5, 'Location': 'Bangalore'}
# if 'name' in d:
#     print(d['name'])



