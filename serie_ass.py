import yfinance as yf
import pandas as pd
import os

tickers = [
    "UCG.MI",      # UniCredit
    "ISP.MI",      # Intesa Sanpaolo
    "LDO.MI",      # Leonardo
    "STLAM.MI",    # STMicroelectronics
    "RACE.MI",     # Ferrari
    "BMED.MI",     # Banca Mediolanum
    "AZM.MI",      # Azimut Holding
    "PRY.MI",      # Prysmian
    "MONC.MI",     # Moncler
    "REC.MI"       # Recordati
]

data = yf.download(
    tickers,
    start="2005-02-28",
    end="2026-04-15",
    auto_adjust=False
)

prices = data["Close"]
# tiene solo le date comuni a tutti i titoli
prices = prices.dropna()

download_path = os.path.join(os.path.expanduser("~"), "Downloads", "Project_FMaS.csv")
prices.to_csv(download_path)

print(f"File salvato in: {download_path}")
print(prices.head())