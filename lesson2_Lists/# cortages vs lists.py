# cortages vs lists
t = (1, 2, 3, 4, 5)
print(t[1])

for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])

t = [1, 2, 3, 4, 5]
t[0] = 2
print(t)

# cortage is the same as a list, but we can't change any elements in it