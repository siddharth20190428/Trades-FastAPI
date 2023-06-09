from models import Trade, TradeDetails
import random
import string
from datetime import datetime

trades = []

# creating a list of 100 trades
for i in range(100):
    # day variable for creating random dates 
    day = (9 + i) % 30 + 1
    trade = Trade(
        assetClass=random.choice(["Equity", "Bond", "FX"]),
        counterparty="".join(random.choices(string.ascii_uppercase + string.digits, k=6)),
        instrumentId="".join(random.choices(string.ascii_uppercase + string.digits, k=4)),
        instrumentName="Random Instrument",
        tradeDateTime=datetime(2023, 6, day, 10, 00, 20),
        tradeDetails=TradeDetails(
            buySellIndicator=random.choice(["BUY", "SELL"]),
            price=random.uniform(10.0, 100.0),
            quantity=random.randint(1, 100),
        ),
        tradeId="".join(random.choices(string.ascii_uppercase + string.digits, k=4)),
        trader="".join(random.choices(string.ascii_uppercase + string.digits, k=6)),
    )
    trades.append(trade)