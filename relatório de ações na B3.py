import numpy
import pandas
from pandas_datareader import data as web
import yfinance

yfinance.pdr_override()

ABEV3 = web.get_data_yahoo("ABEV3.SA", start='2020-3-3')

ABEV3.info()

ABEV3.head()

ABEV3.tail(10)


carteira_de_investimentos = ['ABEV3.SA', 'ASAI3.SA', 'CRFB3.SA']
novos_dados = pandas.DataFrame()
for cdi in carteira_de_investimentos:
    novos_dados[cdi] = web.DataReader(
        cdi, data_source='yahoo', start='2020-3-3')['Adj Close']

    novos_dados.tail()

novos_dados.to_csv(
    '/home/rose/portifólio/Faz relatórios de ações de empresas na B3/dados importados do doc em ods.csv')
novos_dados2 = pandas.read_csv(
    '/home/rose/dados importados do doc em ods.csv')
