n = int(input("Введите число: "))
print(type(n))
while n < 0 or n > 10:
    print("Число не подходит! Оно должно быть в диапазоне от 0 до 10")
    n = input("Введите новое число: ")
else:
    print(f"Квадрат числа {n} = {n**2}")
