#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching
and is a caching system:
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class will inherit self.cache_data from BaseCashing
    but wil not have a limit
    """
    def __init__(self):
        """
        Init from BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds key value pairs to self.cache_data
        """
        if key is not None and item is not None:
            keyList = list(self.cache_data)[0:]
            if key in keyList:
                del self.cache_data[key]
                keyList.remove(key)
            self.cache_data[key] = item
            keyList.append(key)

            if len(keyList) > BaseCaching.MAX_ITEMS:
                remove = keyList.pop(0)
                print("DISCARD: " + remove)
                del self.cache_data[remove]
        else:
            pass

    def get(self, key):
        """
        Retrieves items from self.cache_data by key
        """
        try:
            return self.cache_data[key]
        except Exception:
            pass
