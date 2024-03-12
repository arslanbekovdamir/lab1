#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
distances = {}
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
a = len(sites)
for i in range (a):
    if i == 0:
        x1 = sites["Moscow"][0]
        y1 = sites["Moscow"][1]
        x2 = sites["London"][0]
        y2 = sites["London"][1]
        a = (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        distances["Лондон-Москва"] = a
    if i == 1:
        x1 = sites["Moscow"][0]
        y1 = sites["Moscow"][1]
        x2 = sites["Paris"][0]
        y2 = sites["Paris"][1]
        b = (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        distances["Москва-Париж"] = b
    if i == 2:
        x1 = sites["Paris"][0]
        y1 = sites["Paris"][1]
        x2 = sites["London"][0]
        y2 = sites["London"][1]
        c = (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        print(c)
        distances["Лондон-Париж"] = c

# TODO здесь заполнение словаря

print(distances)




