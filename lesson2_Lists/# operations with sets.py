# operations with sets

a = {1, 2, 3, 4, 5, 6}
b = {10, 9, 8, 7, 0, 6}
c = a.copy() # to copy set from variable a to c
u = a.union(b) #to union set a and set b
print(u)
i = a.intersection(b) # only common elements
print(i)
dif = a.difference(b) #how to find the diffrence between set a and b
print(dif)
diff = b.difference(a) #how to find the diffrence between set b and a
print(diff)
q = a.union(b).difference(a.intersection(b))
print(q)
