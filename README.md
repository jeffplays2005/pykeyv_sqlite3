# pykeyv_sqlite3
A small database plugin based on sqlite3, is a key and value system where you store a key, followed by a value.

# Install
Download the github repository and place the pykeyv_sqlite3 folder in your root directory of your project and import using:
```py
from pykeyv_sqlite3 import Database
```
# Use
* Database class:
  * file_name = the database file name, the default is db.sqlite
  * table = table name, can create several instances of the database with the same file but different table
* Methods
  * initialise - self initialises, creates a database with the filename
    * no need to use as the class automatically initialises at the beginning
  * set - sets a key and a value
    * key = your key, this also acts as an update
    * value = your value
  * get
    * key = your key to get
  * delete
    * key = your key to delete
# Example
```py
# Import the package
from pykeyv_sqlite3 import Database
# Create a new database, the default parameter for the database is the database path.
a_database = Database()
a_database.set("key", "value")
print(a_database.get("key")) # value
a_database.delete('key')
print(a_database.get("key")) # None
```
