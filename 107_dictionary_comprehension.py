prices = {
    "apple": 50,
    "banana": 30,
    "mango": 80,
    "orange": 40
}

result = {key : value + 10 for key , value in prices.items()}

print(result)