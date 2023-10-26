#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system
    """

    def __init__(self):
        """Initializes the class"""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key."""
        return self.cache_data.get(key, None)
