"""
Exceptions Handling
"""
# print("Without handling exceptions")
# print("-"*20)
# # ---------------
#
# a = 10
# b = 0
# result = a/b # Program will terminate here abruptly
# print(result)
#
# print("#"*40, end="\n\n")
# ###########################

print("Handling exceptions")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a/b # Program will terminate here abruptly
    print("result:", result)
except:
    print("Reached except block")

print("Remaining execute till end of the program")
print("#"*40, end="\n\n")
###########################

print("try-except with class names")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a/b
    print("result:", result)
except ZeroDivisionError: # 1-way to mention class name
    print("Reached ZDE except block")
except NameError as ne: # 2-way to mention class name where we are storing thrown object
    print("Reached NE except block")
except (IndexError, KeyError): # 3-way to mention class name
    print("Reached IE or KE except block")

print("#"*40, end="\n\n")
###########################

print("try-except-else")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a/b
    print("result:", result)
except:
    print("Reached except block")

else:
    print("Reached Else Block")

# If 'try' success then skip 'except-block' and execute 'else-block'
# If 'try' failed then skip 'else-block' and execute 'except-block'

# Example:
#   if our task is to connect to db, execute queries etc
#   assume in except we need to handle only DBConnection error
#   then
#   we will keep DB connection part in 'try' block
#   then
#   we will keep execute queries etc in else block

print("#"*40, end="\n\n")
###########################

print("'Exception' class will accept all exceptions")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a/xyz
    print("result:", result)
except Exception as e:
    print("Reached except block and exception name is:", e)
    print("Reached except block and exception type is:", type(e))
else:
    print("Reached Else Block")

print("#"*40, end="\n\n")
###########################


print("try-except-finally")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a/xyz
    print("result:", result)
except Exception as e:
    # sadjksalk
    print("Reached except block and exception type is:", e)
    print("Reached except block and exception type is:", type(e))
else:
    print("Reached Else Block")
finally:
    print("In finally block")

# If 'try' success/failed 'finally' will execute
# If 'except' success/failed 'finally' will execute
# If 'else' success/failed 'finally' will execute

# Example: In some cases for example
#   irrespective of try/except success/failure we may need
#   flush() or close connection, commit etc need to do
#   so these code we are putting in finally block

print("#"*40, end="\n\n")
###########################

print("About 'assert' statement")
print("-"*20)
# ---------------

b = 10
assert b == 10
# - Check the condition, if fails then throw error called AssertionError
# - For any condition it will throw error called AssertionError
# -

print("#"*40, end="\n\n")
###########################


print("Handle 'AssertionError'")
print("-"*20)
# ---------------

try:
    b = 10
    assert b == 0
except AssertionError:
    print("Reached AssertionError Except Block")

print("#"*40, end="\n\n")
###########################


print("About 'raise' statement")
print("-"*20)
# ---------------

# In 'assert' we can give ANY-CONDITION
#   but if ANY-CONDITION failes
#   it will throw ONLY-ONE-TYPE-ERROR
#   i.e AssertionError
#
# Using 'raise', for each condition we can specify
#   what type of error we want to throw
#   - It can be builtin class
#   - It can be User Defined Class Error


a = 100
if a == 10:
    raise NameError
if a < 10:
    raise LookupError

print("#"*40, end="\n\n")
###########################


print("Handling 'raise' statement Error")
print("-"*20)
# ---------------


try:
    a = 10
    if a == 10:
        raise NameError
    if a < 10:
        raise LookupError
except NameError:
    print("NameError from raise")
except LookupError:
    print("LookupError from raise")

print("#"*40, end="\n\n")
###########################


print("User defined exception class example-1")
print("-"*20)
# ---------------

# Mandatory ONE Step:
# - user defined class should be sub-class of 'Exception' class
# - OR if some classes are already sub-class of 'Exception' class
#   then we can create sub-class that class as well

class MyError(Exception):
    pass
# Even though it is blank, it is valid exception class
#   where raise, try, except will be able to understand that
#   this is exception class


try:
    a = 10
    if a == 10:
        raise MyError
    if a < 10:
        raise MyError
except MyError:
    print("MyError from raise")


print("#"*40, end="\n\n")
###########################

print("User defined exception class example-2")
print("-"*20)
# ---------------

# Requirement:
# Wherever we are raising the exception,
#   Send some details about the error

class MyError(Exception):
    def __init__(self, m):
        self.error_message = m
    def __str__(self):
        return self.error_message

try:
    a = 10
    if a == 10:
        raise MyError("Here value is equal to 10 so raising this exception")
    if a < 10:
        raise MyError("Here value is lessthan 10 so raising this exception")
except MyError as me:
    print("MyError from raise and Details:", me)


print("#"*40, end="\n\n")
###########################