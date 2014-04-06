__author__ = 'serg'
from numpy.lib.scimath import logn
from math import e


class BloomFilter():
    def __init__(self, n, p):
        self.m = int(- n * logn(e, p) / (logn(e, 2) ** 2))
        self.k = int(self.m / n * logn(e, 2))
        self.list = [False for _ in xrange(self.m)]

    def hash(self):
        result = []
        for i in xrange(self.k):
            x = i

            def tmphash(str):
                res = 1
                for j in xrange(len(str)):
                    res = (res + ord(str[j]) * x**j) % self.m
                return res
            result.append(tmphash)
        return result

    def qhash(self, prev):
        result = []
        for i in xrange(self.k):
            x = i

            def tmphash(str):
                res = (prev[i] + ord(str[len(str) - 1]) * x**(len(str) - 1)) % self.m
                return res
            result.append(tmphash)
        return result

    def add(self, str):
        for f in self.hash():
            str_hash = f(str)
            self.list[str_hash] = True

    def qexists(self, str, prev):
        tmp = []
        result = True
        for f in self.qhash(prev):
            str_hash = f(str)
            tmp.append(str_hash)
            if self.list[str_hash]:
                result = False

        for h in tmp:
            self.list[h] = True

        return result, tmp

    def exists(self, str):
        tmp = []
        result = True
        for f in self.hash():
            str_hash = f(str)
            tmp.append(str_hash)
            if self.list[str_hash]:
                result = False

        for h in tmp:
            self.list[h] = True

        return result,tmp
