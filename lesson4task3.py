# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
#     Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
#
# В этом случае ответ будет:
# [5, 8]
# import timeit, random, itertools, operator, functools, numpy
from random import randint
my_list_1 = [randint(-5, 5) for i in range(20)]
print(my_list_1)
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = list(set(my_list_1))
print(my_list_2)

newList = []
for i in my_list_1:
    if my_list_1.count(i) == 1:
        newList.append(i)

print(newList)
