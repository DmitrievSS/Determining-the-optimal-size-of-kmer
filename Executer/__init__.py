__author__ = 'serg'

from run import *

prefix = "../reads/"
kmers = [19, 25, 31, 35, 41]
reads = prefix + "half_fragment.fastq"
assemblers = ["Abyss"]

for k in kmers:
    for assembler in assemblers:
        args = [assembler, "--o", "test" + assembler + "/" + str(k), "--k", str(k),
                "--i", reads, "--f", "fastq", "--r", "long"]
        run(args)

# assemblers = ["SPAdes"]
# args = [assembler, "--o", "test" + assembler + "/" + str(k), "--k", str(k),
#         "--i", reads, "--f", "fastq", "--r", "long"]
