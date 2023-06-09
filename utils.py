def filterTrades(trades, asset_class, trade_type, start, end, min_price, max_price):
    filteredTrades = trades
    # filtering the trades if we have provided asset class
    if asset_class:
        filteredTrades = list(filter(lambda x: x.asset_class == asset_class, filteredTrades))

    # filtering the trades if we have provided trade_type
    if trade_type:
        filteredTrades = list(filter(lambda x: x.trade_details.buySellIndicator == trade_type, filteredTrades))

    # filtering the trades if we have provided start dateTime
    if start:
        filteredTrades = list(filter(lambda x: x.trade_date_time >= start, filteredTrades))

    # filtering the trades if we have provided end dateTime
    if end:
        filteredTrades = list(filter(lambda x: x.trade_date_time <= end, filteredTrades))

    # filtering the trades if we have provided minimum trade price
    if min_price:
        filteredTrades = list(filter(lambda x: x.trade_details.price >= min_price, filteredTrades))

    # filtering the trades if we have provided maximum trade price
    if max_price:
        filteredTrades = list(filter(lambda x: x.trade_details.price <= max_price, filteredTrades))

    return filteredTrades



def sortTrades(trades, sortBy, order):
    # sorting the result with given column
    if sortBy == "Asset Class":
        trades.sort(
            key=lambda trade: getattr(trade, "asset_class"),
            reverse=(order == "Descending"),
        )
    if sortBy == "Timestamp":
        trades.sort(
            key=lambda trade: getattr(trade, "trade_date_time"),
            reverse=(order == "Descending"),
        )
    if sortBy == "Trade Type":
        trades.sort(
            key=lambda trade: getattr(trade.trade_details, "buySellIndicator"),
            reverse=(order == "Descending"),
        )
    if sortBy == "Trade Price":
        trades.sort(
            key=lambda trade: getattr(trade.trade_details, "price"),
            reverse=(order == "Descending"),
        )
    
    return trades