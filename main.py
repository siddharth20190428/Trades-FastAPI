from fastapi import FastAPI, HTTPException, Query
from models import Trade
from database import trades
from typing import List, Optional
from datetime import datetime
from utils import filterTrades, sortTrades

app = FastAPI()


@app.get("/trades", response_model=List[Trade])
async def getAllTrades(
    # defining parameters for different filters
    asset_class: Optional[str] = Query(None, description='Filter by "asset class" of the trade.'),
    trade_type: Optional[str] = Query(None, description='Filter by "trade type" of the trade.'),
    start: Optional[datetime] = Query(None, description='Filter by "start timestamp" of the trade.'),
    end: Optional[datetime] = Query(None, description='Filter by "end timestamp" of the trade.'),
    min_price: Optional[float] = Query(None, description='Filter by "min price" of the trade.'),
    max_price: Optional[float] = Query(None, description='Filter by "max price" of the trade.'),
    tradesPerPage: Optional[int] = Query(10, description="Set how many trades per page"),
    page: Optional[int] = Query(1, description="Set the page"),
    sortBy: str = Query("Asset Class", enum=["Asset Class", "Trade Type", "Timestamp", "Trade Price"], description="Sort the trades based on Columns",),
    order: str = Query("Ascending", enum=["Ascending", "Descending"], description="Sort the trades in ascending or descending order",),
):
    # filtering the trades based on column
    filteredTrades = filterTrades(
        trades, asset_class, trade_type, start, end, min_price, max_price
    )
    # variable for showing trades with respect to trades per page and page
    tradesStart = tradesPerPage * (page - 1)

    # result list which has trades form start and end according to itemsPerPage and Page
    # it is done to achieve pagination
    result = filteredTrades[tradesStart : tradesStart + tradesPerPage]

    # sorting the filteredtrades based on column 
    result = sortTrades(result, sortBy, order)

    return result


@app.get("/trades/search", response_model=List[Trade])
async def searchTrades(query: str):
    result = []
    # iterating over the trades we have
    for trade in trades:
        # adding trade to the result array if the trade's counterparty, instrument_id, instrument_name, trader column has query in it
        if (
            query.lower() in trade.counterparty.lower()
            or query.lower() in trade.instrument_id.lower()
            or query.lower() in trade.instrument_name.lower()
            or query.lower() in trade.trader.lower()
        ):
            result.append(trade)

    # returning the result array
    return result


@app.get("/trades/{trade_id}", response_model=Trade)
async def getTradeById(trade_id: str):
    # iterating over the trades
    for trade in trades:
        # if we got the trade whose trade_id is equal to trade_id provided in parameter we return that trade
        if trade.trade_id == trade_id:
            return trade
    else:
        # else we send an exception saying trade not found
        raise HTTPException(status_code=404, detail="Trade not found")
