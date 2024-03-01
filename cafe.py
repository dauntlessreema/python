# menu list and 2 dictionaries (one for stock and one for its value) created

# variables
menu = "peaches , ice-cream, tsuchinoko , noodles"
print(menu)
stock = {1: 83, 2: 16, 3: 2, 4: 9001}
price = {1: 0.60, 2: 2.99, 3: 599.00, 4: 0.20}

# main loop to calculate and print the total stock value, 'items' set as keys to access corresponding values
total_stock = 0
for items in price:
    item_value = price[items] * stock[items]
    total_stock += item_value
print(f"Total value of stock = £{total_stock}")