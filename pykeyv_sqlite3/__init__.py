#!/usr/bin/env python
"""Pykeyv_sqlite3

Author: Jeffplays2005

https://github.com/jeffplays2005
"""
import sqlite3
# A key and value sqite package that takes a custom database path and table
__version__ = "1.0.0"

class Database():
    def __init__(self, file_name="db.sqlite", table = "db"):
        self.file_name = file_name
        self.con = sqlite3.connect(file_name)
        self.cur = self.con.cursor()
        self.table = table
        self.initialise(table)
    def initialise(self, table = "db"):
        sql = f"""CREATE TABLE IF NOT EXISTS {table} (
        \"key\" VARCHAR(255) PRIMARY KEY,
        \"value\" TEXT
        );""";
        return self.cur.execute(sql)
    def set(self, key, value):
        if not key or not value:
            raise MissingValueException("Missing key or value in .set()")
        sql = f"""INSERT INTO db (key, value)
			VALUES(?, ?)
			ON CONFLICT(key)
			DO UPDATE SET value=excluded.value;"""
        self.cur.execute(sql, (key, value))
        self.con.commit()
    def get(self, key):
        if not key:
            raise MissingValueException("Missing key .get()")
        sql = f"SELECT * FROM {self.table} WHERE key = \"{key}\""
        res = self.cur.execute(sql)
        output = res.fetchall()
        if len(output) != 0:
            return output[0][1]
        else:
            return None
    def delete(self, key):
        if self.get(key) != None:
            sql = f"DELETE FROM {self.table} WHERE key = \"{key}\""
            self.cur.execute(sql)
