import random

__author__ = 'serg'
dict = ['A', 'C', 'G', 'T']
random.seed()
with open("input", "w") as output:
    for i in xrange(10000):
        str = ""
        for j in xrange(80):
            str += dict[random.randint(0, 3)]
        str += "\n"
        output.write(str)
    output.close()