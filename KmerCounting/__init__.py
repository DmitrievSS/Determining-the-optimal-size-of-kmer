import sys

__author__ = 'serg'

from BloomFilter import BloomFilter
from Utils.Decorators import timing_val

# @timing_val
def exist(bf, kmer, differentkmers, kstart, line):
    length = len(kmer)
    kmerhashes = []
    if length <= 20:
        kmerhashes = bf[length - kstart - 1].exists(kmer)
    else:
        kmerhashes = bf[length - kstart - 1].exists(kmer, exist(bf, kmer[:-1], differentkmers, kstart, line)[1])
    if kmerhashes[0]:
        differentkmers[length - kstart - 1] += 1
    lastkmerhashes = kmerhashes
    for i in xrange(1, len(line) - length + 1):
        lastkmerhashes = bf[length - kstart - 1].exists(line[i:length + i], lastkmerhashes[1], line[i - 1])
        if lastkmerhashes[0]:
            differentkmers[length - kstart - 1] += 1
    return kmerhashes


# @timing_val
def getkmers(k):
    # input = open("Bloom/input", "r")
    input = open("new.fastq", "r")
    return input


@timing_val
def run(kstart, kend):
    differentkmers = [0 for _ in xrange(kstart, kend)]
    bloomFilter = [BloomFilter(50000, 0.01) for _ in xrange(kstart, kend)]
    # with open("Bloom/output", "w") as output:
    with open("output", "w") as output:
        strInput = getkmers(kstart)
        # done = 0
        for line in strInput:
            if line[0] == '@':
                line = strInput.next()
                line = line[:-1]
                exist(bloomFilter, line[:kend], differentkmers, kstart, line)

        map(lambda x, y: output.write(str(y + 1) + "  different kmers = " +
                                      str(x) + "\n"), differentkmers, xrange(kstart, kend))
        # output.write("max diff kmers " + differentkmers.sort()[0])
        output.close()
        strInput.close


run(19, 40)
