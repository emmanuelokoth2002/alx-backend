#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                most_recently_used = list(self.cache_data.keys())[-1]
                del self.cache_data[most_recently_used]
                print(f"DISCARD: {most_recently_used}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.cache_data.pop(key)
            self.cache_data[key] = self.cache_data[key]
            return self.cache_data.get(key)
