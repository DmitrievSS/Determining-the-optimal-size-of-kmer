__author__ = 'serg'

from Executer import Executer
from Utils.Constants import *


class AbyssExecuter(Executer):
    def __init__(self, args):
        Executer.__init__(self, args)
        self.name = ABYSS


    def interpret(self):
        self.exArgs.append(ABYSS)
        self.exArgs.append("np=8")
        for opt, arg in self.opts:
            if opt == "--k":
                self.exArgs.append("k=" + arg)
            if opt == "--o":
                self.exArgs.append("name=" + arg)
            if opt == "--i":
                self.exArgs.append("in=" + "'" + arg + "'")
        # self.exArgs.append("np=1")