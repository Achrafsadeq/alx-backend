# 0x01. Caching

## Description

This project focuses on implementing different caching algorithms in Python. You'll learn how caching systems work and implement various caching strategies including FIFO, LIFO, LRU, MRU, and LFU. The tasks cover basic caching systems and more advanced implementations with different eviction policies.

## Requirements

| Category | Details |
|----------|---------|
| Interpreter | Ubuntu 18.04 LTS using python3 (version 3.7) |
| File Endings | All files should end with a new line |
| Shebang | The first line of all files should be exactly `#!/usr/bin/env python3` |
| README | A README.md file at the root of the project folder is mandatory |
| Coding Style | pycodestyle (version 2.5.x) |
| Executable | All files must be executable |
| File Length | The length of files will be tested using `wc` |
| Documentation | Modules, classes and functions should be documented |
| Base Class | All caching classes must inherit from BaseCaching |

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0 | Basic dictionary caching system without limit | 0-basic_cache.py |
| 1 | FIFO (First-In First-Out) caching system | 1-fifo_cache.py |
| 2 | LIFO (Last-In First-Out) caching system | 2-lifo_cache.py |
| 3 | LRU (Least Recently Used) caching system | 3-lru_cache.py |
| 4 | MRU (Most Recently Used) caching system | 4-mru_cache.py |
| 5 | LFU (Least Frequently Used) caching system | 100-lfu_cache.py |

## Learning Objectives

By completing this project, you will be able to:

* Understand and implement different caching algorithms in Python
* Implement FIFO (First-In First-Out) caching strategy
* Implement LIFO (Last-In First-Out) caching strategy
* Implement LRU (Least Recently Used) caching strategy
* Implement MRU (Most Recently Used) caching strategy
* Implement LFU (Least Frequently Used) caching strategy
* Work with dictionary data structures for caching
* Handle cache eviction when maximum capacity is reached
* Write properly documented and executable Python code
* Implement inheritance from a base caching class
* Understand the trade-offs between different caching strategies

## Base Caching Class

All implementations must inherit from the following base class:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.

