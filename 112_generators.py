def test():
    for i in range(1,4):
        yield i * 10 
        # yield produces the value and pauses the generator.

gen = test()

for x in gen:
    print(x)