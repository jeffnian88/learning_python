# aaa() function return iterable
def aaa():
    n = 0
    while True:
        yield n
        n = n + 1
        if n==10: break

print list(aaa())
print sum(aaa())

# xrange is a generator function
print sum(xrange(10))
