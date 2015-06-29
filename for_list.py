a=[1,2,3,4,5]
print 1 in a
for x in a:
    print x*x

b=[x*x for x in a]
print b

b=[x*x for x in a if x%2==0]
print b


matrix=[[1,2,3],[4,5,6],[7,8,9]]

print 'matrix={0}'.format(matrix)

list_=[[ x*x for x in matrix[i]] for i in range(len(matrix))]
print list_

nested=matrix
#         first forloop         secand forloop
list_= [x for sublist in nested for x in sublist]
print list_


