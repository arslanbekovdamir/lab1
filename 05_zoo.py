#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, "BEAR")
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
for i in range (len(birds)):
    zoo.append(birds[i])
print(zoo)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
a = zoo.index("elephant")
zoo.pop(a)
print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
a = zoo.index("lion") + 1
b = zoo.index("lark") + 1
print("клетка льва -",a , "клетка жаворонка -", b)
