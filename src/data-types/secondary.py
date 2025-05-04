"""
    Secondary data types are those having multiple primary data types within it
    ___________________________________________________________________________
"""

# List Type

# List of elements of same data type
list1 = [4,7,10]
list2 = ["apple", "orange", ""]
list3 = [False, False, True, False]

# List of elements of different data type
list4 = [1, "apple", True, 0, None]

print("\nList:")
print("_________________________________________________________________________________________________")
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("list4:", list4)
print("\n_________________________________________________________________________________________________")

"""
    Characteristics of List
    - A list starts with index of 0
    - Maximum length of a list is not fixed, it can take the available memory of the system
    - Negative index means referring the list in reverse order
"""

# List operations
print("\nList Operations:")
print("_________________________________________________________________________________________________")

# Accessing an element at index
print("Accessing an element:")
print("Item at index 0 of list1:", list1[0])
print("Item at index 1 of list1:", list1[1])
print("_________________________________________________________________________________________________")

# Add new element
#___________________________________________________
print("Add an element:")
# Add new element to the end of the list
list1.append(11)
print("Added element 11 at the end of the list1:", list1)

# Add new element at an index
list2.insert(2, "Mango")
print("Added element 'Mango' at index 2 of list2:", list2)

# Add elements of list1 to list2
list1.extend([2,5,3,6])
print("Added new list at the end of list1:", list1)
list2.extend(list1)
print("Added all elements of list1 at the end of list2:", list2)
# Although it can add elements this will show and warning message that
# Expected type 'Iterable[str]' (matched generic type 'Iterable[_T]'), got 'list[int]' instead
print("_________________________________________________________________________________________________")

# Remove an element
#___________________________________________________
print("Remove an element:")
# Remove an element with its value
list1.remove(4)
list3.remove(False)
print("Removed an element with value 4 in the list1:", list1)
print("Removed an element with value False in the list3:", list3)
# When a list as duplicate values remove function will delete the first found value
# When we try to remove an element which doesn't exist will through an error

# Remove an element with its index
list1.pop(1)
print("Removed an element at index 1 in the list1:", list1)
# When we try to remove an element which doesn't exist will through an error

# Remove all elements in a list / Empty a list
list1.clear()
print("Cleared the list1:", list1)

print("_________________________________________________________________________________________________")