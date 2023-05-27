# срезы
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) #1
print(list_1[1]) #2
print(list_1[len(list_1)-1]) # 10 the last from the end
print(list_1[-5]) #6
print(list_1[:]) #whole list
print(list_1[: 2]) # up to 2
print(list_1[len(list_1)-2:]) # 2 elements from the end
print(list_1[2 : 9]) # from index 2 to index 9, but we don't print the last
print(list_1[6 : -18]) 
print(list_1[0: len(list_1):6]) # from index 0 (value 1) with step 6
print(list_1[: : 6]) # with step 6