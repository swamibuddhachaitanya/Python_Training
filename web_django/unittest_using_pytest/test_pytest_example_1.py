"""
unittesting using pytest
"""

"""
Procedure
- file name should startswith test_
- Write each test in separate functions
- function name also should startswith test_
- verify result using 'assert' instead of using 'if-else'
"""

def test_add_test():
    a = 10
    b = 20
    c = a + b
    assert c == 30
    assert c > 0
    assert c < 100

def test_sub_test():
    a = 10
    b = 20
    c = a - b
    assert c == -10


# COMMAND
# pytest -v test_pytest_example_1.py