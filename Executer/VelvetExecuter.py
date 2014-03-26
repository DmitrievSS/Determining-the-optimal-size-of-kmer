from subprocess import call

__author__ = 'serg'

from Executer import Executer
from Constants import VELVETH, VELVETG

class VelvetExecuter(Executer):
    def __init__(self, args):
        Executer.__init__(self, args)
        self.name = VELVETH

    def interpret(self):
        self.exArgs = [None for j in xrange(6)]
        self.exArgs[0] = VELVETH
        for opt, arg in self.opts:
            if opt == "--k":
                self.exArgs[2] = arg
            if opt == "--o":
                self.exArgs[1] = arg
            if opt == "--i":
                self.exArgs[5] = arg
            if opt == "--f":
                self.exArgs[3] = "-" + arg
            if opt == "--r":
                self.exArgs[4] = "-" + arg

    def execute(self):
        print self.exArgs
        call(self.exArgs)
        call([VELVETG, self.exArgs[1]])
