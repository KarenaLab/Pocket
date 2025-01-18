
# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# Functions
def rate_annual_to_month(annual):
    """
    Converts annual investment rate into monthly investment rate.
    Equation: (1+a)^1 = (1+m)^12

    """
    annual = annual / 100
    month = np.power(1+annual, (1/12)) - 1

    month = month * 100
    month = np.round(month, decimals=5)
    
    return month
    

def rate_month_to_annual(month):
    """
    Converts monthly investment rate into annual investment rate.
    Equation: (1+m)^12 = (1+a)^1

    """
    month = month / 100
    annual = np.power(1+month, 12) - 1

    annual = annual * 100
    annual = np.round(annual, decimals=5)

    return annual


def time_to_double(annual):
    """
    Calculates the time (months) to twice the interrest invested.
    Equation: x = log(2) / log(1+i)

    Return the number of months to twice the value.

    """
    monthly = rate_annual_to_month(annual)
    monthly = monthly / 100

    delta = np.log(2) / np.log(1+monthly)
    

    return delta

