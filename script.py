import pandas as pd
from pandas_datareader import data
from datetime import datetime
import pytz

def Stock_Price(stocks, day, end_day):
    pd.set_option("max_rows", None)
    pd.set_option("max_columns", None)
    stocks_df = pd.DataFrame()
    for acao in stocks:
        stocks_df[acao] = data.DataReader(acao, data_source = 'yahoo', start=day, end=end_day)['Close']
    return(stocks_df.values[0])

def Today():
    sp = pytz.timezone('America/Sao_Paulo')
    data_sp = datetime.now(sp)
    day = data_sp.strftime("%Y-%m-%d")
    return day
