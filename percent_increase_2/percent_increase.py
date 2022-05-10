# Percent Increase Activity

# Formulas
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# @TODO: Create float variable for original_price
original_price = 580000.00

# @TODO: Create float variable for current_price
current_price = 885000.00

# @TODO: Calculate difference between current_price and original_price
increase = current_price - original_price

# @TODO: Calculate percent_increase
percent_increase = increase/original_price * 100

# Print original_price
print(f"your house original price was ${original_price}")

# Print current_price
print(f"your house current price is ${current_price}")

# @TODO: Print percent_increase to 2 decimal places using f-string formatting
print(f"the percent increase price on your house is ${percent_increase:.2f}%.")
