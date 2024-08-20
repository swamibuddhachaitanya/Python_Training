"""
fixtures
"""
import requests
import sqlite3
import pytest

@pytest.fixture
def my_db_cursor():
    con = sqlite3.connect("my_data_db.sqlite3")
    cur = con.cursor()
    return cur

def test_db_1(my_db_cursor):
    my_db_cursor.execute("SELECT * FROM MY_DATA_TABLE")
    res = my_db_cursor.fetchall()
    assert len(res) > 1
    assert type(res).__name__ == 'list'




# How to execute?
# pytest -v test_pytest_example_6.py