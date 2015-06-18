def mapf(x): return x+1
list_=map(mapf,range(10))
print list_

def reducef(x,y): return max(x,y)
list__=reduce(reducef, list_)
print list__
