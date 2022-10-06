# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10

import random
number = random.randint(0,100)
bin_result = []
print('Число:', number)
while number > 0:
    bin_result.insert(0, str(number%2))
    number //=2
print('Двоичное представление:', "".join(bin_result))