# Name [P444] - B3 Investiments portfolio control

# Versions
# 01 - Nov 20th, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
# 01 - Change column `value` to `purchase_value` or something simular,
# 02 - Add number formater: decimals fixed,
# 03 - 


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
                        columns=["date", "stocks", "qty", "value", "today", "ibov"])

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


def consolidate_portfolio(DataFrame):
    """
    Gets a list of purchase and sell of stocks and consolidate it.

    """
    cols = list(DataFrame.columns)
    wallet = dict()

    for row in DataFrame.index:
        date = DataFrame.loc[row, "date"]
        stock = DataFrame.loc[row, "stocks"]
        qty = int(DataFrame.loc[row, "qty"])
        value = int(DataFrame.loc[row, "value"])
        operation = _find_operation

    # Continue            

    return None
    

def add_operation(DataFrame):
    # Data input (by user)
    date = input(" > Inform date of operation ('yyyy-mm-dd'): ")
    stock = input(" > Inform name of asset: ")
    qty = input(" > Inform quantity of stocks: ")
    value = input(" > Inform value per stock unit: ")
    ibov = input(" > Inform ibov value at the moment of purchase/sell: ")
    print("")

    # Append data to DataFrame
    row = len(list(DataFrame.index))
    DataFrame.loc[row, "date"] = date
    DataFrame.loc[row, "stocks"] = stock
    DataFrame.loc[row, "qty"] = int(qty)
    DataFrame.loc[row, "value"] = float(value)
    DataFrame.loc[row, "ibov"] = int(ibov)
    
    return DataFrame


def delete_operation(DataFrame):
    view_portfolio(DataFrame)

    line_max = np.max(DataFrame.index)
    while(True):
        line_remove = int(input(f" Choose line to be deleted [0~{line_max}]: "))        
        if(line_remove <= line_max):
            DataFrame = DataFrame.drop(labels=line_remove, axis=0)
            break

        else:
            print(f" >>> Error: Index of range")
            

    return DataFrame


def view_portfolio(DataFrame):
  #       date    stock      qty      value        ibov 
  # 2024-01-01   ABCD12   99.999   1.000,00   9.999.999
  #1234567890123456789012345678901234567890123456789012  > numeral
  #0         1        2        2          4           5  > decimal

    # Header
    print("       date    stock      qty      value        ibov") 

    # Wallet lines   
    for row in DataFrame.index:
        date = DataFrame.loc[row, "date"]
        stock = DataFrame.loc[row, "stocks"]
        qty = str(DataFrame.loc[row, "qty"])
        value = str(DataFrame.loc[row, "value"])
        ibov = str(DataFrame.loc[row, "ibov"])

        print(f"{date:>11s}{stock:>9s}{qty:>9s}{value:>11s}{ibov:>12s}")

    # Closing line space
    print("")

    return None


def remove_stock(DataFrame):
    """
    Remove a line from portfolio.
    Action of sell.
    
    """
    pass

    return None


def update_database():
    """
    Update the data from iBovespa (BOV) daily values of stocks.

    """
    pass

    return None


