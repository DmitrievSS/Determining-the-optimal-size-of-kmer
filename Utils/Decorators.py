__author__ = 'serg'
import time


def timing_val(func):
    def tmp(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print "Time : %f \n" % (time.time() - t)
        return res

    return tmp