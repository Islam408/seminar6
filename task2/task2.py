# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.



N = int(input('Введите число: '))
fac = lambda a, b:  a * b
f = 1
for i in range(N):
    i+=1
    f = fac(f,i)
    print(f, end=' ')

