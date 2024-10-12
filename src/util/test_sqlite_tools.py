# TODO: Actually test this code

from sqlite_tools import sqlite_tools

db = sqlite_tools("test_1")

# print(db.create_table("CREATE TABLE test1('field1', 'field2', 'field3')"))

print(db.select_one("SELECT name FROM sqlite_master"))

print(db.table_exists('test1'))