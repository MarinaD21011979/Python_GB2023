# main functions in lists
# 1 to delete the last element - pop 
list_1 = [12, 7, -1, 21, 0]
a = list_1.pop()
print(a) # delete the last element
print(list_1.pop()) #0
print(list_1)
print(list_1.pop()) #21
print(list_1)
print(list_1.pop()) # -1
print(list_1)

# to delete the specific element from the list
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # to delete element with specific index, 0 in this case
print(list_1)
print(list_1.pop(3))
print(list_1)

# to add the element to the list for the needed position - function insert
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(5, 9)) # 2 arguments: 1 - position = index, 2 - value = to add 9 on the position with index 5
print(list_1)
