"""
    List of Arithmetic operations
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Modulus
    - Exponentiation
    - Floor division
"""
print("\nArithmetic operations")
print("_________________________________________________________________________________________________")

# Number Addition
print("\nAddition operation between numbers:")

# Add multiple values directly in print function
print("Add multiple values directly in print function: 2 + 5 + 4 = ", 2 + 5 + 4)

num1 = 2 + 1
num2 = 6 + 10 + num1
print("Add numbers to a number variable: num2 + 19 =", num2 + 19)

# String Addition / Concatenation
print("\nString concatenation through addition:")

str1, str2 = "San", "keerthana"
print("Add two or multiple strings /string concatenation (str1, str2 = 'San', 'keerthana'):", str1 + str2)

# List Addition / Concatenation
print("\nList concatenation through addition:")

list1, list2 = [1,2,3], ["apple", "kiwi"]
list1 += list2
# We will see about this operation in detail,
# this is nothing but list1 = list1 + list2
print("Add multiple lists: [1,2,3] + ['apple', 'kiwi'] =", list1)
# Addition overcomes the constraint of extend function
# where it doesn't support adding elements of another list with different data type

print("_________________________________________________________________________________________________")

# Number Subtraction
print("\nSubtraction operation between numbers:")

num3, num4, num5, num6 = 1.34, 4, -9.2, 10
print("Subtract multiple numbers:  10-4-1.34-(-9.2) =", num6 - num4 - num3 - num5)
# -(-9.2) becomes 9.2
print("_________________________________________________________________________________________________")

# Number Multiplication
print("\nMultiplication operation between numbers:")

print("Multiply multiple numbers:  2.0 * 2 * 10 =", 2.0 * 2 * 10)

# String Multiplication
print("\nMultiplication operation on strings:")

print("Multiply string with number:  'abc ' * 3 = ", "abc " * 3)
# But a string cannot be multiplied with a string like this "abc" * "def"
print("_________________________________________________________________________________________________")

# Number Division
# Resultant value is quotient of division (floating value)
print("\nDivision operation between two numbers 10 / 5:", 10 / 5)
# Resultant value is quotient of division (fixed value)
print("Floor Division operation between two numbers 10 / 5:", 10 / 5)
print("_________________________________________________________________________________________________")

# Number Modulus
# Resultant value is reminder of division (fixed value)
print("\nModulus operation between two numbers 11 % 5:", 11 % 5)
print("_________________________________________________________________________________________________")

# Number Exponential
print("\nExponential calculation 2 ** 3 is same as 2 * 2 * 2 =", 2 ** 3)
print("_________________________________________________________________________________________________")