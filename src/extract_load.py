import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

commodities = ['CL=F', 'GC=F', 'SI=F']

# função que retorna um DataFrame
def buscar_dados_commodities(simbolo, periodo = '5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period = periodo, interval = intervalo)[['Close']] #pegando apenas a coluna 'Close'
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commodities():
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities()
    print(dados_concatenados)

