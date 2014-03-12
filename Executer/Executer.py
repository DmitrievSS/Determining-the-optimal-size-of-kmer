__author__ = 'serg'


import getopt
import sys
from subprocess import call

class Executer:
    def __init__(self, args):
        self.name = None
        try:
            self.opts, self.args = getopt.getopt(args, "", ["k=", "i=", "o=", "f=", "r="])
        except getopt.GetoptError:
            print 'executer.py -k <integer> -o <outputfilename> '
            sys.exit(2)
        self.exArgs = []
        self.interpret()

    def interpret(self):
        pass

    def execute(self):
        print self.exArgs
        call(self.exArgs)