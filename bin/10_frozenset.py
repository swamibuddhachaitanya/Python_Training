"""
- frozenset
    -- to keep list of values
    -- it keeps UNIQUE values only
    -- It will not maintain the order
    -- We can store only immutable values
"""

print("Frozenset PART-1")
print("How to store the values")
print("-"*20)
# ---------------

# We dont have shortcut for frozenset

my_frozenset = frozenset({10, 10, 10, "Python", "Python", "Java", "Java"})
print("my_frozenset:", my_frozenset)

print("#"*40, end="\n\n")
###########################


# About indexes
# ---------------
# - Since We don't have indexes to each values
#   we will not be able to access each value
#   instead we can also convert this to other type
#   like list/tuple etc to get index if we want
# - OR we can iterate using loops
###########################

print("Frozenset PART-2")
print("Methods inside frozenset class")
print("-"*20)
# ---------------

print(dir(my_frozenset))

# OR we can also pass class name
print(dir(frozenset))

print("#"*40, end="\n\n")
###########################


print("Frozenset PART-3")
print("'union', 'intersection', 'difference' methods")
print("-"*20)
# ---------------

java_batch = frozenset({'emp-1', 'emp-2', 'emp-3', 'emp-4'})
python_batch = frozenset({'emp-3', 'emp-4', 'emp-5', 'emp-6'})
print("java_batch:", java_batch, sep="\n", end="\n\n")
print("python_batch:", python_batch, sep="\n", end="\n\n")

# Total stregth
total_employees = java_batch.union(python_batch)

# Employees in both
employees_in_both = java_batch.intersection(python_batch)

# Employees attending only Java
only_java = java_batch.difference(python_batch)

print("total_employees:", total_employees)
print("employees_in_both:", employees_in_both)
print("only_java:", only_java)

print("#"*40, end="\n\n")
###########################