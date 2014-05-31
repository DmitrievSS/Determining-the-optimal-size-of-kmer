__author__ = 'serg'

with open("new.fastq", "r") as inp, open("new1.fastq", "w+") as outp:
    for line in inp:
        if line[0] == '@':
            t = inp.next()
            outp.write(t[:-1])
            inp.next()
            inp.next()
