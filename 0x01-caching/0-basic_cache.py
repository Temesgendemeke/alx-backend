#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class will inherit self.cache_data from BaseCashing
    but wil not have a limit
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds key value pairs to self.cache_data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
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
