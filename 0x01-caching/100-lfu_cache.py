#!/usr/bin/env python3
""" LFUCache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a Least Frequently Used (LFU) caching system """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """ Cache a key-value pair """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS
        and key not in self.cache_data:
            lfu = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == lfu]

            if len(lfu_keys) > 1:
                lru_lfu = {k: self.usage.index(k) for k in lfu_keys}
                discard = self.usage[min(lru_lfu.values())]
            else:
                discard = lfu_keys[0]

            print(f"DISCARD: {discard}")
            del self.cache_data[discard]
            del self.usage[self.usage.index(discard)]
            del self.frequency[discard]

        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        if key in self.usage:
            self.usage.remove(key)

        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to a given key, or None """
        if key is not None and key in self.cache_data:
            self.usage.remove(key)
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
