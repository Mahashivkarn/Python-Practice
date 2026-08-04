def sum(*args):
    #Args will be the tupel of all the values pass to sum.
    total= 0
    for items in args:
        total += items
    return total

print(sum(342,2,7))