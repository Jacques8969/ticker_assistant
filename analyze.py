import yfinance as yf
from datetime import datetime

def get_ticker_snapshot(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    hist = stock.history(period="6mo")

    latest_price = hist["Close"].iloc[-1] if not hist.empty else None
    start_price = hist["Close"].iloc[0] if not hist.empty else None

    six_month_return = None
    if latest_price and start_price:
        six_month_return = ((latest_price - start_price) / start_price) * 100

    return {
        "ticker": ticker,
        "company_name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "market_cap": info.get("marketCap"),
        "trailing_pe": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "revenue_growth": info.get("revenueGrowth"),
        "profit_margins": info.get("profitMargins"),
        "latest_price": latest_price,
        "six_month_return_pct": six_month_return,
        "analysis_date": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    ticker = input("Ticker: ").upper()
    result = get_ticker_snapshot(ticker)

    for key, value in result.items():
        print(f"{key}: {value}")
