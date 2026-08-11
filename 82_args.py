                # inside the function, args become a tuple
                # It can store any number of arguments
                # store them as tuple
                # * is tells pythonCollect all extra positional arguments into args.
                # args is just conventional name >>>> *numbers is also allowed
# *args >> unnamed/positional values >>>>>> tuple
# **kwargs >> named/keyword values >>>>>> dictionary 
# kwargs >> key-word arguments

def add(*args):
    total = 0

    for number in args:
        total += number

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50))
    