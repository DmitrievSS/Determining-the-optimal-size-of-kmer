__author__ = 'serg'
import time


def timing_val(func):
    def tmp(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print "Time %s: %f\n" % (func.__name__, time.time() - t)
        return res

    return tmp