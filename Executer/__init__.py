import os
import subprocess

__author__ = 'serg'

from run import *

prefix = "../reads/"
kmers = [21, 23, 25, 27, 29, 31, 35, 37, 39]
# kmers = [23]
_reads = ["frag_2.fastq, frag_1.fastq, 1.fastq, norm.fastq, 2.fastq"]
assemblers = ["Abyss"]
i = 0
for read in _reads:
    i += 1
    for k in kmers:
        for assembler in assemblers:
            if not os.path.exists("test" + assembler + "/" + str(i)):
                os.mkdir("test" + assembler + "/" + str(i) + "/")
            args = [assembler, "--o", "test" + assembler + "/" + str(i) + "/" + str(k), "--k", str(k),
                    "--i", prefix+read, "--f", "fastq", "--r", "long"]
            run(args)

# assemblers = ["SPAdes"]
# args = [assembler, "--o", "test" + assembler + "/" + str(k), "--k", str(k),
#         "--i", reads, "--f", "fastq", "--r", "long"]
