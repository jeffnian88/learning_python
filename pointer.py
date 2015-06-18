a=[1,2,3,4]
b=a

b.append(5)
print a
print b

a.append(6)
print a
print b

print 'a is b:{0}'.format(a is b)

c=[1,2,3,4,5,6]
print 'c is a:{0}'.format(c is a)
print 'c == a:{0}'.format(c==a)
