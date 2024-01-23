#!/usr/bin/python3
import sys
import ctypes
from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

def unix_time(function):
    stsrt_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()

    return "\nreal: {}\nuser: {}\nsys: {}".format(
            end_time - start_time,
            end_resources.ru_time - start_resources.ru_time,
            end_resources.ru_stime - start_resources.ru_stime)

def print_factors():
    fun = ctypes.CDLL("./lib_factor_functions.so")
    fun.trial_division.argtypes = [ctypes.c_long]
    with open(sys.argv[1], 'r') as prime:
        line = prime.readline()
        while line != '':
            n = int(line)
            fun.trial_division(n)
            line = prime.readline()
