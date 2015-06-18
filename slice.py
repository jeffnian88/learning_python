a='abcd'

print a
# extended Slices
for x in range(-4,len(a)+1,1):
    print 'a[{1}::-1]={0}'.format(a[x::-1],x)
for x in range(-4,len(a)+1,1):
    print 'a[{1}::1]={0}'.format(a[x::1],x)

print 'a[::-1]={0}'.format(a[::-1])
