# SteelEye API Developer technical test

This solution has four files

-   database.py - will be having an lsit of trades
-   main.py - the fastAPI server is located and main functions are here
-   models.py - models provided
-   utils.py - utility functions for filtering and sorting the trades

# Approach

1. First we setup the server.
2. We have three APIs :

-   /trades - which will get all the trades and it has filters
-   /trades/search - this will get the list of trades which will contain a query string in counterparty, instrumentId, instrumentName, trader
-   /trades/trade_id - which will get a particular trade with the given trade_id

3. This solution also has pagination and sorting.
4. Trades can be filtered with properties:
   assetClass, end, maxPrice, minPrice, start, tradeType
5. Trades can be sorted by:
   assetClass, tradeType, timestamp, trade Price
