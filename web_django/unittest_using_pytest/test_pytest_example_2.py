"""
test mymodule.py
"""
from mymodule import course, add, MyClass

# Test Case-1
def test_course():
    assert course == "Python"

# Test Case-2
def test_add():
    r1 = add(10,20)
    assert r1 == 30
    r2 = add(30, 40)
    assert r2 == 70

# Test Case-3
def test_MyClass():
    m = MyClass()
    m.add_name("abc")
    r = m.view_name()
    assert r == "abc"



# COMMAND
# pytest -v test_pytest_example_2.py