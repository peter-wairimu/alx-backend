#!/usr/bin/env python3
"""
LIFO Caching
Classes:
    LIFOCache
Functions_
    put(object, key: string, item: string)
    get(object, key: string)
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from BaseCaching and is a caching system:
    ...
    Parametres
    ----------
    None
    Methods
    -------
    put(key, item)
        assigns the dictionary cache_data the value of the item for the key
    get(key)
        returns the dictionary cache_data value of the given key
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the person object
        """
        super().__init__()
        self.new_key = []
        self.index = 3

    def put(self, key, item):
        """
        Assigns the dictionary cache_data the value of the item for the key
        If the argument key or item is None, this method should not do anything
        Parameters
        ----------
            key (string): key to append to dictionary
            item (string): value to add the dictionary with its
            corresponding key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if key not in self.new_key:
                self.new_key.append(key)

            if len(self.new_key) > BaseCaching.MAX_ITEMS:
                discard = self.new_key.pop(self.index)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            if key in self.new_key:
                self.index = self.new_key.index(key)

    def get(self, key):
        """
        Returns the dictionary cache_data value of the given key
        if the argument key is None or the key doesn't exist in
        dictionary cache_data, return None
        Parameters
        ----------
            key (string): key that will be searched in the dictionary
            to return the value
        Returns
        -------
            Dictionary value if it finds the key, if not none
        """
        string_value = None
        if key is None or key in self.cache_data:
            for keys, values in self.cache_data.items():
                if key == keys:
                    string_value = values

        return string_value
