# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

x = [3, 5, 2, 4, 7, 9, 8]
sum = 0
for i in range(1, len(x), 2):
    sum += x[i]

print(f'{x} -> сумма элементов на нечётных позициях: {sum}')