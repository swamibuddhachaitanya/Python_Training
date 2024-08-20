"""
testing API
https://demoqa.com/utilities/weather/city/pune
and
database
"""
import requests
import sqlite3
import pytest

@pytest.mark.myapitests
def test_api_1():
    response = requests.get("https://demoqa.com/utilities/weather/city/pune")
    response = response.json()
    assert "pune" in response.values()
    assert "City" in response.keys()
    assert ("City", "pune") in response.items()

@pytest.mark.myapitests
def test_api_2():
    response = requests.get("https://demoqa.com/utilities/weather/city/pune")
    response = response.json()
    assert "pune" in response.values()
    assert "City" in response.keys()
    assert ("City", "pune") in response.items()

@pytest.mark.mydbtests
def test_db_1():
    con  = sqlite3.connect("my_data_db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM MY_DATA_TABLE")
    res = cur.fetchall()
    assert len(res) > 1
    assert type(res).__name__ == 'list'


@pytest.mark.mydbtests
def test_db_2():
    con  = sqlite3.connect("my_data_db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM MY_DATA_TABLE")
    res = cur.fetchall()
    assert len(res) > 1
    assert type(res).__name__ == 'list'


# How to execute?
# pytest -v -m mydbtests test_pytest_example_5.py