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
def ibov_tickers():
    ibov = ["^BVSP",
            "CPFE3.SA", "ELET3.SA", "BBDC4.SA", "GGBR4.SA", "CMIG4.SA",
            "BRAP4.SA", "CPLE6.SA", "BRKM5.SA", "ABEV3.SA", "BRFS3.SA",
            "CCRO3.SA", "EQTL3.SA", "EMBR3.SA", "BBSE3.SA", "CSAN3.SA",
            "CSNA3.SA", "CYRE3.SA", "ECOR3.SA", "BBAS3.SA", "JBSS3.SA",
            "SUZB3.SA", "PETR4.SA", "SLCE3.SA", "VALE3.SA", "CXSE3.SA",
            "MRFG3.SA", "PETZ3.SA", "PSSA3.SA", "NTCO3.SA", "PETR3.SA",
            "TOTS3.SA", "MRVE3.SA", "WEGE3.SA", "MGLU3.SA", "LREN3.SA",
            "RAIZ4.SA", "ELET6.SA", "UGPA3.SA", "SBSP3.SA", "STBP3.SA",
            "AZUL4.SA",
            "ALUP11.SA", "KLBN11.SA", "SANB11.SA", "TAEE11.SA"]

    return ibov

def others_tickers():
    items = ["SGO.PA"]

    return items


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

    # Value Adjust (Round)
    decimals = 3
    for col in data.columns:
        data[col] = np.round(data[col], decimals=decimals)

    
    return data    


# Testing
if(__name__ == "__main__"):
    for i in ibov_tickers():
        info = get_values(i, start="2025-01-01", end="2025-05-01")
        print(info)
    
        


        

