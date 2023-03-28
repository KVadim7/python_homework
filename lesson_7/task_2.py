stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

merged_dict = {key: stock.get(key, 0) * prices.get(key, 0) for key in set(stock) | set(prices)}
print(merged_dict)

total_price = 0
for value in merged_dict.values():
    total_price += value
print("Total price:", int(total_price))
