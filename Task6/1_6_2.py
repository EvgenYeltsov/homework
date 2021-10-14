stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
    "banana": 4
}
ls1 = []
for i, j in stock.items():
    for k, v in prices.items():
        if i == k:
            z = j*v
            ls1.append(z)
print(sum(list))
