import yfinance as yf
from fastapi import FastAPI

app = FastAPI()


@app.get("/samsung")
def samsung():
    df = yf.Ticker("005930.KS").history(period="5d")  # 삼성전자 최근 5일
    df.index = df.index.strftime("%Y-%m-%d")
    return df[["Open", "High", "Low", "Close", "Volume"]].to_dict(orient="index")
