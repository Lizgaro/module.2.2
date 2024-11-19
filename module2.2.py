# Получаем три целых числа от пользователя
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Проверяем, сколько чисел равны между собой
if first == second == third:
    print(3)  # Все три числа равны
elif first == second or first == third or second == third:
    print(2)  # Равны хотя бы два числа
else:
    print(0)  # Все числа разные
