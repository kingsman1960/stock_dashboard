import streamlit as st
from datetime import date
import pandas as pd
import yfinance as yf

st.title("NASDAQ NYSE Financial Institutes Dashboard")

st.markdown("This streamlit application is using for"
            "monitoring NASDAQ NYSE Financial companies with upperthan medium market Cap (> $ 2 Bil) \n By Youngwon Cho.")
#tickers = ("AAPL","ADBE","ADI",ADSK,AMAT,AMD,ANSS,APP,ASML,AVGO,AZPN,BIDU,BILI,CDNS,CDW,CHKP,COIN,CRWD,CSCO,CTSH,CTXS,DDOG,DOCU,DOX,ENTG,ERIC,FTNT,GOOG,GOOGL,INTC,INTU,JKHY,KLAC,LBTYA,LBTYB,LBTYK,LRCX,MCHP,MDB,META,MPWR,MRVL,MSFT,MTCH,MU,NICE,NLOK,"NTAP","NVDA","NXPI","OKTA","ON","PANW","PTC","QCOM","ROKU","SEDG","SNPS","SPLK","SSNC","STX","SWKS","TEAM","TMUS","TTD","TTWO","TXN","VOD","VRSN","WBD","WDAY","WDC","ZBRA","ZI","ZM","ZS")
DATA_URL3 = "./pages/nasdaq_nyse_financial.csv"
#tickers = pd.read_csv()


def load_data():
    data = pd.read_csv(DATA_URL3)
    #data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace = True)
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis= 'columns', inplace= True)
    #data.rename(columns={'occur_date_occur_time': 'date/time'})
    return data


data = load_data()

dropdown = st.multiselect('Pick your assets', data)


START = st.date_input('Start', value=pd.to_datetime('2017-06-01'))
END = st.date_input('End', value=pd.to_datetime('2022-07-01'))


def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


st.header("The Adjusted Close price of selected assets")
if len(dropdown) > 0:
    df = yf.download(dropdown, START, END)['Adj Close']
    st.line_chart(df)


# Stocks =

st.header("The cummulative returns of selected assets")
if len(dropdown) > 0:
    df1 = relativeret(yf.download(dropdown, START, END)['Adj Close'])
    st.line_chart(df1)
