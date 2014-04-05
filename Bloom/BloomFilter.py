__author__ = 'serg'
from numpy.lib.scimath import logn
from math import e


class BloomFilter():
    def __init__(self, n, p):
        self.m = int(- n * logn(e, p) / (logn(e, 2) ** 2))
        self.k = int(self.m / n * logn(e, 2))
        self.list = [False for _ in xrange(self.m)]
        self.savedhash = {}

    def hash(self):
        result = []
        for i in xrange(self.k):
            x = i

            def tmphash(str):
                res = 1
                for j in xrange(len(str)):
                    res += str[j] * x**j
                return res
            result.append(tmphash)
        return result

    def hash(self, prev):
        result = []
        for i in xrange(self.k):
            x = i

            def tmphash(str):
                res = prev[i] + str[len(str) - 1] * x**(len(str) - 1)
                return res
            result.append(tmphash())

    def add(self, str):
        res = []
        for f in hash():
            str_hash = f(str)
            res.append(str_hash)
            self.list[str_hash] = True
        self.savedhash[str] = res

    def add(self, str, prev):
        res = []
        for f in hash():
            str_hash = f(str, prev)
            res.append(str_hash)
            self.list[str_hash] = True
        self.savedhash[str] = res

    def exists(self, str):
        for f in hash():
            if not self.list[f(str)]:
                return False
        return True