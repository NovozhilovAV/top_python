from functools import reduce
# Модуль 4. Строки. Списки. Часть 3

# Два списка целых заполняются случайными числами.
# Необходимо: Сформировать третий список
# содержащий элементы обоих списков;
# содержащий элементы обоих списков без повторений;
# содержащий элементы общие для двух списков;
# содержащий только уникальные элементы каждого из списков;
# содержащий только минимальное и максимальное значение каждого из списков

one = [1, 2, 5, 11, 17, 34, 99, 45, 39]
print(f'Список 1 - {one}')
two = [89, 76, 45, 5, 33, 2, 49, 4, 7, 9, 88]
print(f'Список 2 - {two}')
three = one + two
print(f'Элементы обоих списков - {three}')
# print(one + two)    # элементы обоих списков

print(f'Оба списка без повторений - {list(set(three))}')

five = [x for x in one if x in two]
print(f'Общие элементы двух списков V1 - {five}')
print(f'Общие элементы двух списков V2 - {list(set(one)&set(two))}')
print(f'Общие элементы двух списков V3 - {list(set(one).intersection(two))}')
five_2 = []
for i in one:
    for j in two:
        if i == j:
            five_2.append(i)
            break

print(f'Общие элементы списков v4 - {five_2}')

five_3 = []
for i in one:
    if i in two:
        five_3.append(i)

print(f'Общие элементы списков V5 - {five_3}')

print(f'Уникальные элементы двух списков  - {list(set(one) and set(two))}')

# содержащий только минимальное и максимальное значение каждого из списков
# six = list(filter(lambda a, b: a if a > b else b, three))   # ?????

six = reduce(lambda a, b: a if a > b else b, three)
print(f'Максимальное в списках  - {six}')
six_2 = reduce(lambda a, b: a if a < b else b, three)
print(f'Минимальное в списках  - {six_2}')