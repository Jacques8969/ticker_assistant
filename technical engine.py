def technical_score(hist):
    score = 50
    reasons = []

    close = hist["Close"]

    ma20 = close.rolling(20).mean().iloc[-1]
    ma50 = close.rolling(50).mean().iloc[-1]
    latest = close.iloc[-1]

    if latest > ma20:
        score += 10
        reasons.append("Price above 20-day moving average")
    else:
        score -= 10
        reasons.append("Price below 20-day moving average")

    if latest > ma50:
        score += 10
        reasons.append("Price above 50-day moving average")
    else:
        score -= 10
        reasons.append("Price below 50-day moving average")

    if ma20 > ma50:
        score += 10
        reasons.append("Positive short-term trend")
    else:
        score -= 10
        reasons.append("Weak short-term trend")

    return {
        "technical_score": max(0, min(100, score)),
        "reasons": reasons
    }
