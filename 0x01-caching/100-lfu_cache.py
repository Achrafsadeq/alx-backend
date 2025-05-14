#!/usr/bin/env python3
""" LFUCache Module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a Least Frequently Used (LFU) caching system """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.usage_count = {}
        self.usage_order = []

    def put(self, key, item):
        """ Assign an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.evict_lfu()
            self.cache_data[key] = item
            self.usage_count[key] = 1
            self.usage_order.append(key)

        self.usage_order.append(
            self.usage_order.pop(self.usage_order.index(key))
        )

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        self.usage_order.append(
            self.usage_order.pop(self.usage_order.index(key))
        )
        return self.cache_data[key]

    def evict_lfu(self):
        """ Evict the least frequently used (LFU) item """
        min_usage = min(self.usage_count.values())
        lfu_keys = [
            k for k in self.usage_order if self.usage_count[k] == min_usage
        ]

        if lfu_keys:
            lfu_key = lfu_keys[0]
            self.usage_order.remove(lfu_key)
            del self.cache_data[lfu_key]
            del self.usage_count[lfu_key]
            print(f"DISCARD: {lfu_key}")
