#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
garden_set1 = set(garden)
meadow_set1 = set(meadow)
garden_set2 = set(garden)
meadow_set2 = set(meadow)
garden_set3 = set(garden)
meadow_set3 = set(meadow)
a = len(garden_set)
print(garden_set)
print(a)

# выведите на консоль все виды цветов
# TODO здесь ваш код
print("все цветы", set.union(garden_set, meadow_set))
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
print("растут и там и там",set.intersection(garden_set1, meadow_set1))
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
print("растут на cаду, но не растут в лугу",set.difference(garden_set3, meadow_set3))
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
print("растут в луге, но не растут на саде",set.difference(meadow_set2, garden_set2))
