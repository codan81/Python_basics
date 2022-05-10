# Lists - Manipulation Exercise

# Using the `stock_tickers` list, update, add and remove elements according to the specified instructions.
# Print after each action, print the list in order to confirm your syntax was correct.
crypto_tickers = ["BTC", "ETH", "GRT", "XRP", "MATIC", "SHIB", "ADA", "VET", "ON"]


# @TODO Update the ticker 'ON' to 'ONE'
crypto_tickers [8] = "ONE"

# @TODO Add the ticker 'ZM' to the end of the stock_tickers list
crypto_tickers.append("SOL")

# @TODO Add the ticker 'AUDIO' to the beginning of the stock_tickers list.
# @TODO Add the ticker 'AMP' so it appears between 'SHIB' and 'ADA'.
crypto_tickers.insert(0, "AUDIO")
crypto_tickers.insert(7, "AMP")

# @TODO Remove the ticker 'AUDIO' from the stock_tickers list
crypto_tickers.remove("AUDIO")

# @TODO Remove the ticker 'AMP' from the list using the pop() method
crypto_tickers.pop(7)

# @TODO Slice a section of the list that includes the tickers 'ETH', 'GRT', 'XRP', and 'MATIC'.
# @TODO Set this equal to a variable called crypto_tickers_slice.
crypto_tickers_slice =  crypto_tickers[1:5]
print(crypto_tickers_slice)

