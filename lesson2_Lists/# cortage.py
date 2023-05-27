# cortage

t = ()

print(type(t))

t = (1, )
print(type(t))

v = [1, 2, 3 ]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v)) # transform to cortage

# a,b = 1,2 # множественное присваивание a = b = 1
# divide the cortage to three variable

a,b,c = v  
print(a, b, c)