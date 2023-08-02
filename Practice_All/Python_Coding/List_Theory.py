# List Lists are used to store multiple items in a single variable.
# used to store collections of data
# Lists are created using square brackets:

# List Items.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered.
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates.
# Since lists are indexed, lists can have items with the same value:

# List Length.
# To determine how many items a list has, use the len() function:

# List Items - Data Types
# A list can contain different data types:

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':


# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.


# ============================== Access Items ===================================================

# List items are indexed and you can access them by referring to the index number.

# lst = ['Raja', 27, 'Uma', 24, 'Sony', 'Oracle', 'B.Tech', 'MBA', 'Bangalore', 'Anantapur']
# length_lst = len(lst)
# print(length_lst)
#
# print("3 rd element :: ", lst[2])
# print("Last element :: ", lst[length_lst - 1])
#
# print("3 rd element :: ", lst[-8])
# print("Last element :: ", lst[-10])

# Slicing Concept also we can to Access List Elements.

# ======================= Check if Item Exists =======================================================

# To determine if a specified item is present in a list use the in keyword:

# lst = ['Raja', 27, 'Uma', 24, 'Sony', 'Oracle', 'B.Tech', 'MBA', 'Bangalore', 'Anantapur']
# if 'Uma' in lst:
#     print("Yes, Uma Name in the given List")

# ======================= Append/Add Items to List =======================================================

# To add an item to the end of the list, use the append() method.

# lst = ['Raja', 27, 'Uma', 24, 'Sony', 'Oracle', 'B.Tech', 'MBA', 'Bangalore', 'Anantapur']
# lst.append('Prasanna')
# print(lst)
#
# o/p:     ['Raja', 27, 'Uma', 24, 'Sony', 'Oracle', 'B.Tech', 'MBA', 'Bangalore', 'Anantapur', 'Prasanna']

# The insert() method inserts an item at the specified index:

# lst = ['Raja', 27, 'Uma', 24, 'Sony', 'Oracle', 'B.Tech', 'MBA', 'Bangalore', 'Anantapur']
# lst.insert(5, 'MoM')
# print(lst)
#
# o/p:    ['Raja', 27, 'Uma', 24, 'Sony', 'MoM', 'Oracle', 'B.Tech', 'MBA', 'Bangalore', 'Anantapur']

# To append elements from another list to the current list, use the extend() method.

lst = ['Raja', 27, 'Uma', 24, 'Sony', 'MoM', 'Oracle', 'B.Tech', 'MBA', 'Bangalore']
lst2 = ['name', 'age', 'wife', 'w_age', 'Mother']

lst.extend(lst2)
print(lst)

# lst.append(lst2)
# print(lst)


# ======================= Update/Change Items to List =======================================================

# To change the value of a specific item, refer to the index number:

# lst = ['Raja', 27, 'Uma', 24, 'Sony', 'MoM', 'Oracle', 'B.Tech', 'MBA', 'Bangalore']
# lst[0] = "SRK"
# print(lst)


# ======================= Remove/Delete Items to List =======================================================

# lst = ['Raja', 27, 'Uma', 24, 'Sony', 'MoM', 'Oracle', 'B.Tech', 'MBA', 'Bangalore']

# The remove() method removes the specified item.
# we can use remove() when ever we know the list of elements

# lst.remove('MBA')
# print(lst)

# The pop() method removes the specified index.

# lst.pop(1)
# print(lst)

# The del keyword also removes the specified index:

# del lst[0]
# print(lst)
# del lst[0]
# print(lst)

# If you do not specify the index, the pop() method removes the last item.

# lst.pop()
# print(lst)

# The del keyword can also delete the list completely. but it has No content.

# del lst
# print(lst)

# The clear() method empties the list.
# The list still remains, but it has no content.

# lst.clear()
# print(lst)

















