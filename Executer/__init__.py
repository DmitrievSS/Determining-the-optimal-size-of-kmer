import subprocess

__author__ = 'serg'

from run import *

prefix = "../reads/"
kmers = [21, 23, 25, 27, 29, 31, 35, 37, 39]
# kmers = [23]
reads = [prefix + "frag_2.fastq"]
assemblers = ["Abyss"]
for read in reads:
    for k in kmers:
        for assembler in assemblers:
            args = [assembler, "--o", "test" + assembler + "/" + str(k), "--k", str(k),
                    "--i", read, "--f", "fastq", "--r", "long"]
            run(args)
    # subprocess.call("./../KmerCounting/1", read)
    # subprocess.call("./../KmerCounting/2", read)
    # subprocess.call("./../KmerCounting/3", read)

# assemblers = ["SPAdes"]
# args = [assembler, "--o", "test" + assembler + "/" + str(k), "--k", str(k),
#         "--i", reads, "--f", "fastq", "--r", "long"]
