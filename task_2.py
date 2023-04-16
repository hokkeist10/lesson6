list_1 = [-6, 7, 0, 3, -1, 10, 1, 4, 5, 11, 2, 0, 9, 0, 8, -5, -7]
min_n = int(input('Введите нижнюю границу диапазона чисел: '))
max_n = int(input('Введите верхнюю границу диапазона чисел: '))
for el in range(len(list_1)):
    if min_n <= list_1[el] <= max_n:
        print(el)
