__author__ = 'serg'

from Executer import Executer


class VelvetExecuter(Executer):
    def __init__(self, args):
        Executer.__init__(self, args)
        self.name = "./../velvet/velveth"

    def interpret(self):
        for opt, arg in self.opts:
            if opt == "--k":
                self.exArgs[1] = arg
            if opt == "--o":
                self.exArgs[0] = arg
            if opt == "--i":
                self.exArgs[4](arg)
            if opt == "--f":
                self.exArgs[2] = "-" + arg
            if opt == "--r":
                self.exArgs[3] = "-" + arg
