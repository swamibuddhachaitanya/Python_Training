"""
testing Database
"""

import sqlite3

# Test Case
def test_query_result():
    con = sqlite3.connect("my_data_db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM MY_DATA_TABLE")
    res = cur.fetchall()
    assert len(res) > 1
    assert type(res).__name__ == 'list'