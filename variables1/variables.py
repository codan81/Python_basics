# Create variables
# string, intiger, float, boolean
crypto_currency = "bitcoin"
position_by_mc = 1
current_price = 35820.00
the_king_of_crypto = True

# Print the variables
print(crypto_currency)
print(position_by_mc)
print(current_price)
print(the_king_of_crypto)

# Prints the data type of each declared variable
print("The data type of Crypto currency is", type(crypto_currency))
print("The data type of position by Market Cap is", type(position_by_mc))
print("The data type of current price is", type(current_price))
print("The data type of the_king_of_crypto is", type(the_king_of_crypto))

# Using variable names in calculations
# market cap calculation formula Total_value(shares) * current value (unit)
btc_mined = 19032981.25
market_cap = btc_mined * current_price
print(f"the Market Cap of Bitcoin is:", {market_cap})

# Updating variables using assignment
btc = 3
dollars = current_price * btc

# Substituting/formatting variable
message = f"The price in Dollars of three bitcoin is: $ {dollars}"
print(message)

# Two number values will be added
btc_transaction_1 = 1.8
btc_transaction_2 = 5.8

total_btc = btc_transaction_1 + btc_transaction_2 + btc 
print(f"the total amount in bitcoin is:",{total_btc})

total_transaction = total_btc * current_price
print(f"the total value in dollars is: $",{total_transaction})

# Two string values will be concatenated
first_name = "Israel"
last_name = "Fernandez"
full_name = first_name + last_name

print(full_name)
print("My name is:" + first_name + " " + last_name + ".")

# Variable naming conventions
mpg = 24

# Better Example
miles_per_gallon = 24
