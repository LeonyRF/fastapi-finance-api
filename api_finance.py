from fastapi import FastAPI
from fastapi.responses import JSONResponse
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de Datos Financieros con yFinance"}

@app.get("/apple")
def get_apple_data(period: str = "1d", interval: str = "1m"):
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period=period, interval=interval)
    data.reset_index(inplace=True)
    return JSONResponse(content=data.to_dict(orient="records"))
