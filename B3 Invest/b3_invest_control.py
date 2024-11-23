# Name [P444] - B3 Investments portfolio control



# Libraries
import os
import sys

import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


# Personal modules
sys.path.append(r"c:\python_modules")
from b3_invest_tools import (_reset_portfolio,
                             _export_portfolio,
                             read_portfolio,
                             add_operation,
                             view_portfolio,
                             update_database)


# Functions



# Setup/Config



# Program --------------------------------------------------------------
data = read_portfolio()

while(True):
    print(" > [a]dd operation,")
    print(" > [q]uit and save portfolio")
    print(" > [f]inish without save portfolio")
    print(" > [v]iew portfolio")
    print("")
    print(" > [r]eset portfolio")
    
    print("")
    
    decision = input(" > Choose your action: ")


    if(decision == "a"):
        data = add_operation(data)


    if(decision == "r"):
        data = _reset_portfolio()
        _export_portfolio(data)


    if(decision == "v"):
        view_portfolio(data)


    if(decision == "q"):
        _export_portfolio(data)
        break


    if(decision == "f"):
        break


# end

