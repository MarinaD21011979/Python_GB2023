# task2
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
    # 1 2 3 4 5
    # 6
   #  -> 5

n = int(input())
list_1 = [1, 2, 3, 4, 5]
print(list_1)
for i in range(n):
    num = int(input())
    list_1.append(num)
    # print(num)
    print(list_1[num -1])
