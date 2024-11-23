# Name [P444] - B3 Investments portfolio control

# Updates
# 01 - Nov 20th, 2024 - Starter,
# 02 - Nov 23rd, 2024 - Adjusting functions. Make easier to save
#                       and quit,
# 03 - 


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
    print(" > [a]dd operation")
    print(" > [v]iew portfolio")
    print(" > [s]ave portfolio")
    print(" > [u]pdate database")
    print(" > [q]uit")
    print("")
    print(" > [r]eset portfolio")
    
    print("")
    
    decision = input(" > Choose your action: ")


    if(decision == "a"):
        data = add_operation(data)

    if(decision == "v"):
        view_portfolio(data)

    if(decision == "s"):
        _export_portfolio(data)

    if(decision == "u"):
        pass

    if(decision == "r"):
        data = _reset_portfolio()
        _export_portfolio(data)

    if(decision == "q"):
        break


# end
