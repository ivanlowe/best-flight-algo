import json
import os

class Cache:
    def __init__(self, cacheFile):
        self.__c_file = open(cacheFile, "r+")
        self.__caches = json.load(self.__c_file)

    def __updateCache(self):
        json_str = json.dumps(self.__caches)
        self.__c_file.seek(0, 0)
        self.__c_file.write(json_str)

    def get(self, key):
        if key in self.__caches:
            return self.__caches[key]

        return None

    def contains(self, key):
        return key in self.__caches

    def set(self, key, value):
        self.__caches[key] = value
        self.__updateCache()

    def remove(self, key):
        self.__caches.pop(key)
        self.__updateCache()

    def clear(self):
        self.__caches.clear()
        self.__updateCache()

    def close(self):
        self.__c_file.close()