# Name [P444] - B3 Investiments portfolio control

# Versions
# 01 - Nov 20th, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
# 01 - Change column `value` to `purchase_value` or something simular,
# 02 - Add number formater: decimals fixed,
# 03 - Add line number to `view_portfolio`, useful for `delete_operation`
#          function,
# 04 - 


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


def _export_portfolio(DataFrame, filename="portfolio_b3.csv"):
    """
    Export data from dataframe portofolio to .csv

    """
    DataFrame.to_csv(filename, sep=",", encoding="utf-8")

    return None


def _find_operation(value):
    """
    Find the operation, if negative is a **sell**,
    if positive is a **buy**.

    """
    if(value > 0):
        op = "buy"

    elif(value < 0):
        op = "sell"

    else:
        op = None


    return op


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
        operation = _find_operation(value)

        print(date, stock, qty, value, operation)

    # Continue            

    return None
    

def add_operation(DataFrame):
    """
    Add an operation (purchase or sell), selling could also work with
    the `delete_operation`.

    Important: Need to save the porfolio to keep information.

    """
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
    """
    Remove an operation from the list. Could be used for selling or
    register the sell as a negative stock value in `add_operation`.

    Important: Need to save the portfolio to keep information.

    """
    
    view_portfolio(DataFrame)
    line_max = np.max(DataFrame.index)

    while(True):
        line_remove = int(input(f" Choose line to be deleted [0~{line_max}]: "))        
        if(line_remove <= line_max):
            DataFrame = DataFrame.drop(labels=line_remove, axis=0)
            break

        else:
            print(f" >>> Error: Index of range \n")
            

    return DataFrame


def view_portfolio(DataFrame):
    """
    Friendly viewer for portfolio DataFrame.
    
    """
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


