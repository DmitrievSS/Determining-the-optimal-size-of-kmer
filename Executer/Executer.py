__author__ = 'serg'

import os
import getopt
import sys


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
        os.execv(self.name, self.exArgs)