# 2: Создайте функцию, принимающую на вход 3
# числа и возвращающую наибольшее из них.

def maximum(lst):
    return max(lst)


def minimum(lst):
    return min(lst)


list1 = [1, 34, 423, -2, -6, 1, 6, 0, 345, 1, 9, 50]

print(max(list1))
print(min(list1))
result = filter(lambda x: x % 2 == 0, list1)
print(list(result))

print(sorted(list1, key=lambda x: x**2, reverse=True))

result2 = map(lambda x: x**3, list1)
print(list(result2))
