#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """
    LFUCache class
    """

    def __init__(self):
        super().__init__()
        self.frequency_counter = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequency_counter.values())
                items_to_discard = [k for k, v in self.frequency_counter.items() if v == min_frequency]
                if len(items_to_discard) > 1:
                    least_recently_used = min(self.keys_in_order, key=lambda x: self.keys_in_order.index(x))
                    items_to_discard.remove(least_recently_used)
                for item in items_to_discard:
                    del self.cache_data[item]
                    self.keys_in_order.remove(item)
                    del self.frequency_counter[item]
                    print(f"DISCARD: {item}")
            self.cache_data[key] = item
            self.keys_in_order.append(key)
            self.frequency_counter[key] = self.frequency_counter.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.frequency_counter[key] += 1
            return self.cache_data.get(key)
