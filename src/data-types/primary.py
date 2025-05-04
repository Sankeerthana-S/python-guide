"""
   Declaration - Naming a variable
   Initialization - Storing/giving a value to the declared variable
   Unlike other programming languages, in Python declaration and initialization is done together
   ____________________________________________________________________________________________
"""

# Primary Built-in data types are listed below
# ____________________________________________________________________________________________

# String / Text Type

str1 = "Sankeerthana" # The stored data is a text
str2 = str("Sankeerthana") # specify the data type using the constructor function
str3 = str() # calling empty str constructor will produce value ""

# ____________________________________________________________________________________________

# Number Types

# int - The stored data is a fixed integer (number between -infinity and +infinity)
num1 = 10 # positive fixed integer
num2 = -10 # negative fixed integer
num3 = 10 + 10 # store the resultant value (20) of an arithmetic expression
num4 = int(100) # specify the data type using the constructor function
num5 = int() # calling empty int constructor will produce value 0

# Casting a string value to an integer
num6 = int("1") # string with only numbers can be converted number

# float - The stored data is a decimal value
float1 = 20.3 # positive decimal/floating integer
float2 = -20.3 # negative decimal/floating integer
float3 = 5 / 2 # store the resultant value (2.5) of an arithmetic expression
float4 = 3e2 # Exponential floating value 300.0
float5 = float(-24.7) # specify the data type using the constructor function
float6 = float() # calling empty float constructor will produce value 0.0

# Casting a string value to float
float6 = float("1") # string with only numbers can be converted number, value is 1.0

# Casting a floating value to fixed integer
num7 = int(91.3) # stored value is 91
num8 = int(5 / 2) # stored value is 2

# similarly a fixed integer can be cast to a floating value
float7 = float(32) # stored value is 32.0


# complex - The stored data is an imaginary value
complex1 = 4j # j is an imaginary value

# Casting int value to complex value
complex2 = complex(1) # specify the data type using the constructor function
# this will be 1 + 0j (where j is an imaginary value at point 0)

# complex data type cannot be cast to int or float

# ____________________________________________________________________________________________

# None Type
# None is a value less type, that can be assigned to a variable

noValue = None

"""
    A variable can be declared and initialized with None type
    When we want to update that variable in future
    The constructor function of None is not directly callable like other data types, and is not needed
"""
# ____________________________________________________________________________________________

# Boolean Type

# bool - The stored data is either "True" or "False"
bool1 = True # directly store the boolean value
bool2 = 4 < 2 # store the resultant value (True) of a comparison expression
bool3 = bool() # calling empty bool constructor will produce value False

# Casting any data type to boolean will provide the falsy or truthy nature of a value
# sample falsy values
bool4 = bool(0) # 0 is a falsy value
bool5 = bool("") # empty string is a falsy value
bool6 = bool(None) # None type is falsy value
bool7 = bool([]) # empty "list" is a falsy value, we will see about list data type in detail

# sample truthy values
bool8 = bool(1 - 2) # resultant value is -1 is a truthy value in Python
bool9 = bool("Name") # non-empty string
testVariable = 3 * 0 # 3 x 0 = 0
bool10 = bool(testVariable) # boolean of testVariable is False

# ____________________________________________________________________________________________

""" 
    Back to String
    Casting other data types to string type
    Any other primary data type passed to the str constructor will be converted to string
"""
str4 = str(3)
str5 = str(8.9)
str6 = str(False)
str7 = str(4 + 3j) # 4 + 3j is a complex value
str8 = str(None)

# ____________________________________________________________________________________________

# How to know the data type of variable?

# Python provides a built-in function type() to check data type of a value / variable
print( type(0) ) # print the type of value 0
print( type(complex1) ) # print the type of the defined variable

# ____________________________________________________________________________________________






