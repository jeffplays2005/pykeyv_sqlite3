# Import the package
from pykeyv_sqlite3 import Database
# Create a new database, the default parameter for the database is the database path.
"storing a string"
# By default, the database path is db.sqlite
a_database = Database()
# The set method takes two parameters, a key and a value
a_database.set("key", "value")
# The get method takes a key
print(a_database.get("key")) # value
"storing JSON/a dictionary"
# Create an example dictionary to store
import json

example_dictionary = {
    "a":"b"
}
a_database.set("a_dictionary", json.dumps(example_dictionary))
print(json.loads(a_database.get("a_dictionary"))) # { "a": "b" }
print(type(json.loads(a_database.get("a_dictionary")))) # <class 'dict'>

# delete method
a_database.delete('key')
print(a_database.get("key")) # None
