# Hash Table Implementation in Python

This repository contains a Python implementation of a Hash Table data structure. This implementation has in mind an use for a supermarket that has products using a string of length 12 as an ID & the quantity of items that are going to be added as the value
## Usage

The Hash Table implementation is provided in the `Hash Table.py` file. To use the Hash Table in your Python project, follow these steps:

1. Download or clone this repository.
2. Import the `HashTable` class from the `Hash Table.py` file into your Python script.

  from HashTable import HashTable

3.then instanciate it 
  hash_table = HashTable()


##Example code
from HashTable import HashTable

hash_table = HashTable()

hash_table.put("apple", 5)
hash_table.put("banana", 2)

print(hash_table.get("apple"))    # Output: 5
print(hash_table.get("banana"))   # Output: 2

hash_table.remove("apple")

print(hash_table.contains("apple"))   # Output: False
print(hash_table.size())              # Output: 1
