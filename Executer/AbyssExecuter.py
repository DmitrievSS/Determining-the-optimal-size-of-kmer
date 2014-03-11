__author__ = 'serg'

from Executer import Executer


class AbyssExecuter(Executer):
    def __init__(self, args):
        Executer.__init__(self, args)
        self.name = "abyss-pe"

    def interpret(self):
        for opt, arg in self.opts:
            if opt == "--k":
                self.exArgs.append("k=" + arg)
            if opt == "--o":
                self.exArgs.append("name=" + arg)
            if opt == "--i":
                self.exArgs.append("in" + " " + arg)