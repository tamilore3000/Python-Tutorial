months = ['January', 'February', 'March'] 
prices = [238.11, 237.81, 238.91]

# Identify min price 
min_price = min(prices)

# Identify min price index 
min_index = prices.index(min_price) 

# Identify the month with min price 
min_month = months[min_index] 
print[min_month]  