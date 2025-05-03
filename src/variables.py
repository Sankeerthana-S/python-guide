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

# We will see about Global scope
