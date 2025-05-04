"""
What is a Variable?
It's a store/container of data values
They are used to store data that we can use and manipulate later.
_____________________________________________________________________
"""
# Reason	                | Example
# To store values	        | year_born = 1997, current_year = 2025
# To reuse values	        | age = currentYear - yearBorn
# To make code readable	    | user_name = "Alice" is clearer than just "Alice"
# To change values easily	| You can update: age = age + 1
# To pass data to functions	| print(age) where age = 28

year_born = 1997
current_year = 2025
age = current_year - year_born
print(age)
print("____________________________________")

# You can also write arithmetic operations inside the Print function
print(current_year - year_born + 1)
print("____________________________________")

# Multiple variables can be initialized parallely
name, age = "Sankeerthana", current_year - year_born
print("Name:", name, "Age:", age)
print("____________________________________")

#_______________________________________________________________________________________

# Variable Naming Conventions in Python

# camel case
variableName = 0
numberVariableName = 0

# snake case
variable_name = 0
_variable_name = 0
variable_name_ = 0
_variable_name_ = 0

# pascal case
VariableName = 0

# Alpha-numeric and underscore combination
variableName1 = 0
variable_name_2 = 0
Variable1Name = 0

"""
    Variable Naming Rules 
     - Must start with a letter or the underscore character ( _ )
     - Cannot start with a number Ex. 1variableName
     - Can only contain alpha-numeric characters ( A-Z, a-z, 0-9) and underscore character ( _ )
     - Cannot be a python keyword Ex. str (name of the string class in python)
     - Python variables are case-sensitive Ex. variableName and VariableName are considered as different variables.
"""
