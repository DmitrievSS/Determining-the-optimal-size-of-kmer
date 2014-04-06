from BloomFilter import BloomFilter
from Utils.Decorators import timing_val

__author__ = 'serg'

# @timing_val
def exist(bf, str, differentkmers, kstart):
    length = len(str)
    kmerhashes = []
    if length <= 20:
        kmerhashes = bf[length - kstart - 1].exists(str)
    else:
        kmerhashes = bf[length - kstart - 1].qexists(str, exist(bf, str[:-1], differentkmers, kstart)[1])
    if kmerhashes[0]:
        differentkmers[length - kstart - 1] += 1
    return kmerhashes

# @timing_val
def getkmers(k):
    # input = open("Bloom/input", "r")
    input = open("input", "r")
    return input


@timing_val
def run(kstart, kend):
    differentkmers = [0 for _ in xrange(kstart, kend)]
    bloomFilter = [BloomFilter(10000, 0.01) for _ in xrange(kstart, kend)]
    # with open("Bloom/output", "w") as output:
    with open("output", "w") as output:
        strInput = getkmers(kstart)
        # done = 0
        for line in strInput:
            for s in xrange(len(line) - kend):
                exist(bloomFilter, line[s:- len(line) + kend + s], differentkmers, kstart)
            for l in xrange(0, kend - kstart - 1):
                exist(bloomFilter, line[len(line) - kend + l:-1], differentkmers, kstart)

        map(lambda x, y: output.write(str(y+1) + "  different kmers = " +
                                      str(x) +"\n"), differentkmers, xrange(kstart, kend))
        output.close()
        strInput.close

run(19, 40)
