__author__ = 'serg'

from run import *

prefix = "../reads/"
kmers = [10, 20, 30]
reads = prefix + "reads1.fa" + prefix + "reads2.fa"
assemblers = ["Abyss", "VelvetExecuter"]
for k in kmers:
    for assembler in assemblers:
        args = [assembler, "--o", "test", "--k", str(k), "--i", reads, "--f", "fasta", "--r", "short"]
        run(args)