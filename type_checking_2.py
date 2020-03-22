# Based on Type-Checking Python Programs With Type Hints and mypy

def add(a, b):
    return a+b

# We can run the above function with any types we want.
print(add(1, 4))
print(add("abc", "ghi"))


# Type checking basically allows us to specify the expected types in the arguments .
def add_ints(a: int, b: int) -> int: # Means that the function expects an int and will return an int.
    return a + b

# So, for checking the types, we will need a type checker which will check the types and give us the feedback
#  A popular type checker is mypy.  pip install mypy-lang
print(add_ints(1, 2))
print(add_ints("abc", "def")) # Now, when we will do mypy type_checking_2.py, this line will cause an error.