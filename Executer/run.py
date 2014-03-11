__author__ = 'serg'
from AbyssExecuter import AbyssExecuter
from VelvetExecuter import VelvetExecuter
assemblers = {"Abyss": AbyssExecuter, "Velvet": VelvetExecuter}


def run(args):
    """
    parse args and execute assembler
    :param args:
    """
    executer = assemblers[args[0]](args[1:])
    executer.execute()