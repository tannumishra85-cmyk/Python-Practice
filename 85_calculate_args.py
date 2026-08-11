def calculate_total(*prices):
    total = 0
    for price in prices:
        total += price

    return total

print(calculate_total(100, 200))
print(calculate_total(50, 20, 30, 100))