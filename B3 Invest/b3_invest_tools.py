# Name [P444] - B3 Investiments portfolio control

# Versions
# 01 - Nov 20th, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
def _reset_portfolio():
    """
    Reset the portfolio dataframe.
    Use it carefully.

    """
    data = pd.DataFrame(data=[],
                        columns=["date", "stocks", "qty", "value", "ibov"])

    return data


def _export_portfolio(DataFrame):
    """
    Export data from dataframe portofolio to .csv

    """
    filename = "portfolio_b3.csv"
    DataFrame.to_csv(filename, sep=",", encoding="utf-8")

    return None


def read_portfolio():
    """
    Import data from portfolio as a dataframe.

    """
    filename = "portfolio_b3.csv"
    data = pd.read_csv(filename, index_col=0, sep=",", encoding="utf-8")  

    return data
    

def add_operation(DataFrame):
    # Data input (by user)
    date = input(" > Inform date of operation ('yyyy-mm-dd'): ")
    stock = input(" > Inform name of asset: ")
    qty = input(" > Inform quantity of stocks: ")
    value = input(" > Inform value per stock unit: ")
    ibov = input(" > Inform ibov value at the moment of purchase/sell: ")
    print("")

    row = len(list(DataFrame.index))
    DataFrame.loc[row] = [date, stock, qty, value, ibov]
    

    return DataFrame


def view_portfolio(DataFrame):
  #       date    stock      qty      value        ibov 
  # 2024-01-01   ABCD12   99.999   1.000,00   9.999.999
  #12345678901234567890123456789012345678901234567890123
  #         1         2         3         4         5

    print("       date    stock      qty      value        ibov")

    for row in DataFrame.index:
        date = DataFrame.loc[row, "date"]
        stock = DataFrame.loc[row, "stocks"]
        qty = DataFrame.loc[row, "qty"]
        value = DataFrame.loc[row, "value"]
        ibov = DataFrame.loc[row, "ibov"]

        print(date, stock, qty, value, ibov)

    print("")

    return None


def update_database():
    pass

    return None

