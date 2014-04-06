from Constants import SPAdes
from Constants import Python

__author__ = 'serg'

from Executer import Executer


class SPAdesExecuter(Executer):
    def __init__(self, args):
        Executer.__init__(self, args)
        self.name = SPAdes

    def interpret(self):
        self.exArgs.append(Python)
        self.exArgs.append(SPAdes)
        self.exArgs.append("--only-assembler")
        for opt, arg in self.opts:
            # if opt == "--k":
            #     self.exArgs.append("k=" + arg)
            if opt == "--o":
                self.exArgs.append("-o " + arg)
            if opt == "--i":
                self.exArgs.append("s " + arg)