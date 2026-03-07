"""
Author: Viktor
Description: Pandas and BeautifulSoup webscrapers + Currency converion
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO
from forex_python.converter import CurrencyRates

# Currency Rates (USD, EUR)
c = CurrencyRates()
USD_GBP = c.get_rate('USD', 'GBP')
EUR_GBP = c.get_rate('EUR', 'GBP')

# VLSFO_Price
url = 'https://shipandbunker.com/prices/av/global/av-glb-global-average-bunker-price'
tables = pd.read_html(url)
VLSFO_Price_df = tables[1]
VLSFO_Price_df['Date'] = pd.to_datetime(VLSFO_Price_df['Date'].str[2:], format="%b %d")

VLSFO_Price = VLSFO_Price_df['Price $/mt'][0] * USD_GBP

# EU_ETS_Price
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

url = "https://tradingeconomics.com/commodity/carbon"
response = requests.get(url, headers=headers)

EU_ETS_Price_df = pd.read_html(StringIO(response.text))[1]
EU_ETS_Price = EU_ETS_Price_df['Actual'][0] * EUR_GBP