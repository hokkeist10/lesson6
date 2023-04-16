first_n = int(input('Введите первое число арифметической прогрессии: '))
numbers= int(input('Введите количество членов арифметической прогрессии: '))
difference = int(input('Введите разность между членами арифметической прогрессии: '))
for el in range(numbers):
    print(first_n + el*difference)

