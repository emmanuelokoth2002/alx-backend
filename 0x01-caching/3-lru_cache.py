#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """

    def __init__(self):
        super().__init__()
        self.keys_in_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.keys_in_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            if key in self.keys_in_order:
                self.keys_in_order.remove(key)
            self.keys_in_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            if key in self.keys_in_order:
                self.keys_in_order.remove(key)
            self.keys_in_order.append(key)
            return self.cache_data.get(key)
