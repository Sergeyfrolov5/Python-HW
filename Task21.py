
n = float(input('Введите вещественное число: '))
sum = 0
while (n != int(n)):
    n *= 10
print(n)
while n > 0:
    sum += n % 10
    n //= 10
print(sum)