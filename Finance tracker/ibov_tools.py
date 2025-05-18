# [P519] Finance Tracker

# Versions
# 01 - May 17th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import os
import datetime as dt

import numpy as np
import pandas as pd
import scipy.stats as stats

import yfinance as yf

import matplotlib.pyplot as plt



# ----------------------------------------------------------------------
def get_values(ticker, start, end):
    # Datetime preparation
    start = dt.datetime.strptime(start, "%Y-%m-%d")
    end = dt.datetime.strptime(end, "%Y-%m-%d")

    # Download data from Yahoo Finance
    data = yf.download([ticker], start, end, auto_adjust=False,
                       threads=True, ignore_tz=True, keepna=True,
                       progress=False)

    # Prepare columns
    def _prep_name(text):
        value = text[0]
        value = value.lower()
        value = value.replace(" ", "_")

        return value

        
    data.columns = [_prep_name(i) for i in data.columns]


    # Remove not used columns
    data = data.drop(columns=["adj_close"])

    
    return data    


# Testing
if(__name__ == "__main__"):
    info = get_values("ITUB3.SA", start="2024-01-01", end="2025-05-17")
    print(info)

