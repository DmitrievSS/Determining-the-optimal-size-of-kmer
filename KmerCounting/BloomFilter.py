# from numpypy.lib.scimath import logn
import math
import subprocess
from Utils.Constants import KMERB

__author__ = 'serg'

from math import e

prefix = "../reads/"
kmers = [21, 23, 25, 27, 29, 31, 35, 37, 39]
reads = ["frag_2.fastq, frag_1.fastq, 1.fastq, norm.fastq, 2.fastq"]
reads = map(lambda x: prefix + x, reads)
for read in reads:
    subprocess.call("./../KmerCounting/1", read)
    subprocess.call("./../KmerCounting/2", read)
    subprocess.call("./../KmerCounting/3", read)



class BloomFilter():
    def __init__(self, n, p):
        self.m = int(- n * math.log(p) / (math.log(2) ** 2))
        self.k = int(self.m / n * math.log(2))
        self.list = [False for _ in xrange(self.m)]
        self.hashtable = []
        for i in xrange(self.k):
            x = i
            self.hashtable.append([])
            self.hashtable[x].append(x+1)
            for _ in xrange(KMERB):
                self.hashtable[x].append(self.hashtable[x][_] * (x + 1))

    def hashfunc(self, k, str, c=None, prev=None):
        x = k
        res = 0
        if prev is None and c is None:
            for j in xrange(len(str)):
                res = (res + ord(str[j]) * self.hashtable[x-1][j])
        if prev is not None and c is None:
            res = (prev[k-1] + ord(str[len(str) - 1]) * self.hashtable[x-1][len(str) - 1])
        if prev is not None and c is not None:
            res = (prev[k-1]/x - ord(c) + ord(str[len(str) - 1]) * self.hashtable[x-1][len(str)-1])
        print type(res)
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
