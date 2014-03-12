from subprocess import call

__author__ = 'serg'

from run import *
prefix = "../reads/"
# prefix = "/home/serg/work/Baka/reads/"
kmers = [10, 20, 30]
reads = prefix + "frag_1.fastq"
assemblers = ["Velvet"]
tmp = ["abyss-pe", "name=testout", "k=10", "in='" + reads + "'"]
print tmp
# call(["./../../velvet/velveth", 'testVelvet10', '10', '-fastq', '-short', '../reads/frag_1.fastq'])
# call(tmp)

for k in kmers:
    for assembler in assemblers:
        args = [assembler, "--o", "test" + assembler + str(k), "--k", str(k),
                "--i", reads, "--f", "fastq", "--r", "short"]
        run(args)