# This is based on Chris Bailey's short course on real python for type checking.

# First one is static vs dynamic typing. Since in python types are checked at runtime. So it is a dynamically typed language.
# In other languages such as java and C, the type of variables is checked at compile time.
# In python the type of a variable can be changed during its lifetime.

if False:
    print(1 + "cool") # This line is never going to run, so no type error.
else:
    print(1)

thing = 18
print(type(thing))
thing = "Cool place"
print(type(thing))

# Apparently the course is not free so not gping forward with it.
