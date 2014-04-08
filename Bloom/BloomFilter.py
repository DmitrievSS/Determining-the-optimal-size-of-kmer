from Utils.Constants import KMERB

__author__ = 'serg'
from numpy.lib.scimath import logn
from math import e


class BloomFilter():
    def __init__(self, n, p):
        self.m = int(- n * logn(e, p) / (logn(e, 2) ** 2))
        self.k = int(self.m / n * logn(e, 2))
        self.list = [False for _ in xrange(self.m)]
        self.hashtable = []
        for i in xrange(self.k):
            x = i
            self.hashtable.append([])
            self.hashtable[x].append(x+1)
            for _ in xrange(KMERB):
                self.hashtable[x].append(self.hashtable[x][_] * (x + 1))

    def hashfunc(self, k, str, c=None, prev=None ):
        x = k
        res = 0
        if prev is None and c is None:
            for j in xrange(len(str)):
                res = (res + ord(str[j]) * self.hashtable[x-1][j])
        if prev is not None and c is None:
            res = (prev[k-1] + ord(str[len(str) - 1]) * self.hashtable[x-1][len(str) - 1])
        if prev is not None and c is not None:
            res = (prev[k-1]/x - ord(c) + ord(str[len(str) - 1]) * self.hashtable[x-1][len(str)-1])
        return res


    def add(self, kmer):
        for num in xrange(1, self.k):
            str_hash = self.hashfunc(num, kmer)
            self.list[(self.m + str_hash) % self.m] = True


    def exists(self, kmer, prev=None, c=None):
        tmp = []
        result = False
        for num in xrange(1, self.k):
            str_hash = self.hashfunc(num, kmer, c, prev)
            tmp.append(str_hash)
            if not self.list[(self.m + str_hash) % self.m]:
                result = True
        if result:
            for h in tmp:
                self.list[(self.m + h) % self.m] = True
        return result, tmp
