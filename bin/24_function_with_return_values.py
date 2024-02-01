"""
2 cases
case-1: How to access values outside the function
    - in this case, how to access name and company outside the function
case-2: How to pass values to variables present inside the function
    - in this case, how to pass values to name and company

Here, we will discuss
case-1: How to access values outside the function
    - in this case, how to access name and company outside the function
"""


print("Function with one return value")
print("-"*20)
# ---------------

# 2 steps
# step-1: mention values in 'return' statement inside the function
# Step-2: Assign function call to variable

def employee():
    name = "emp-1"
    company="comp-1"
    print("Name:", name)
    print("Company:", company)
    return name # Step-1
    # after return, if we have some statements then it will never execute
    # below line will never execute
    print("some message")

received_value = employee() # step-2
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################


print("Function with more than 1 return value in TUPLE")
print("-"*20)
# ---------------

# 2 steps
# step-1: mention values in 'return' statement inside the function
# Step-2: Assign function call to variable

def employee():
    name = "emp-1"
    company="comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1
    return name, company # return in tuple
    # after return, if we have some statements then it will never execute
    # below line will never execute
    print("some message")

received_value = employee() # step-2
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################

print("Function with more than 1 return value in LIST")
print("-"*20)
# ---------------

# 2 steps
# step-1: mention values in 'return' statement inside the function
# Step-2: Assign function call to variable

def employee():
    name = "emp-1"
    company="comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1
    return [name, company]
    # after return, if we have some statements then it will never execute
    # below line will never execute
    print("some message")

received_value = employee() # step-2
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################

print("Function with more than 1 return value in Dictionary")
print("-"*20)
# ---------------

# 2 steps
# step-1: mention values in 'return' statement inside the function
# Step-2: Assign function call to variable

def employee():
    name = "emp-1"
    company="comp-1"
    print("Name:", name)
    print("Company:", company)
    # Step-1
    return {"name": name, "company": company}
    # after return, if we have some statements then it will never execute
    # below line will never execute
    print("some message")

received_value = employee() # step-2
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################


print("Function without return statment: None will be returned")
print("-" * 20)


# ---------------

# 2 steps
# step-1: mention values in 'return' statement inside the function
# Step-2: Assign function call to variable

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)


received_value = employee()  # step-2
print("received_value:", received_value)

print("#" * 40, end="\n\n")
###########################


print("Function with EXPRESSION in return statment: Expression RESULT will be returned")
print("-"*20)
# ---------------

# 2 steps
# step-1: mention values in 'return' statement inside the function
# Step-2: Assign function call to variable

def employee():
    name = "emp-1"
    company="comp-1"
    print("Name:", name)
    print("Company:", company)
    return (10+20)/(10-20)


received_value = employee() # step-2
print("received_value:", received_value)

print("#"*40, end="\n\n")
###########################