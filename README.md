# lab1
## Задание 00
словарь `sites` с именами городов в качестве ключей и их координатами в виде кортежей. Каждый кортеж содержит два числа - координаты x и y города.

Затем скрипт вычисляет расстояния между каждой парой городов, используя вложенный цикл. Для каждой пары рассчитывается  расстояние с использованием формулы `sqrt((x1 - x2) **   2 + (y1 - y2) **   2)`, где `(x1, y1)` - координаты первого города, а `(x2, y2)` - координаты второго города. Расстояние затем сохраняется в словаре `distances` с ключом, который является комбинацией двух имен городов, разделенных дефисом.

После того как все расстояния были рассчитаны и сохранены в словаре `distances`, другой цикл проходит по элементам словаря. Для каждого элемента он выводит ключ (который является парой имен городов) и значение (которое является рассчитанным расстоянием).

Вывод скрипта будет содержать список расстояний между каждой парой городов.
![image](https://github.com/MTrucky/laba_1/assets/146337304/0432dba8-f57c-447d-bb3a-d27c6f650e8f)
_____
## Задание 01
`point_1` - это кортеж, содержащий координаты точки (x, y).

`dist` - это переменная, которая вычисляет расстояние от начала координат до точки, используя формулу `√(x² + y²)`. Здесь **0.5 вычисляет квадратный корень из суммы квадратов координат.
`result` - это переменная, которая проверяет, меньше ли расстояние до точки радиуса круга. Если расстояние меньше или равно радиусу, то точка находится внутри круга.

`print(result)` - выводит результат проверки, который будет `True`, если точка находится внутри круга, и `False` в противном случае.

![image](https://github.com/MTrucky/laba_1/assets/146337304/ad3eb806-6dc4-4481-a609-5e73a0725d4e)
____
## Задание 02
1. Расставляем знаки, как показано в условии
2. Выводим результат

![image](https://github.com/MTrucky/laba_1/assets/146337304/0402338d-5978-40fa-84a3-fad9e711355e)
____
## Задание 03
Выводим резуультат с помощью срезов:
![image](https://github.com/MTrucky/laba_1/assets/146337304/ab4615c8-27cd-46e7-a007-dc19653e24c4)
____
## Задание 04
Создаем список
Создаем список с приблизительным ростом
В переменной father_height находим рост с помощью перебора списка и функции next, которая возвращает элемент, который соответствует условию
В переменной total_height вычисляем общий рост семьи с помощью функции sum
Выводим результат:
![image](https://github.com/MTrucky/laba_1/assets/146337304/a83280d5-1b7d-4777-a34a-7617c439597f)
____
## Задание 05
С помощью функции insert добавляем медведя в список с помощью индекса
Добавляем птиц в список с помощью суммирования
С помощью remove удаляем из списка слона
Выводим на консоль в какой клетке сидит лев и жаворонок, но добавляем +1, чтобы было понятно другим людям
![image](https://github.com/MTrucky/laba_1/assets/146337304/253b23df-6d0b-4c6a-9f38-480765b5a9f3)
____
## Задание 06
`vist[3][1], vist[5][1], vist[8][1]` - это доступы к элементам списка vist, которые представляют собой длительности песен 'Halo', 'Enjoy the Silence' и 'Clean' соответственно.

`round(..., 2)` - функция округления, которая округляет сумму длительностей до двух знаков после запятой.
print(f"Три песни звучат {z} минут") - вывод результата в форматированной строке.
Вычисление и вывод общего времени звучания песен из словаря `vict`

`g = round(vict["Sweetest Perfection"] + vict["Policy of Truth"] + vict["Blue Dress"]`,  2)
print(f"А другие три песни звучат {g} минут")

`vict["Sweetest Perfection"]`, `vict["Policy of Truth"]`, `vict["Blue Dress"]` - это доступы к значениям словаря `vict`, которые представляют собой длительности песен `'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'` соответственно.

`round(..., 2)` - функция округления, которая округляет сумму длительностей до двух знаков после запятой.

print(f"А другие три песни звучат {g} минут") - вывод результата в форматированной строке.

![image](https://github.com/arslanbekovdamir/lab1/assets/163137977/1f38cdd7-0acf-4a7f-97ed-8f05324346e8))
____
## Задание 07
С помощью срезов выводим значение
![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/20a2b228-04a3-4024-8716-b5a8c5456aab)



____
## Задание 08
Создаем множество цветоы с помощью функции set

С помощью union объединяем множества и выводим их

С помощью intersection находим пересечения в множествах и выводим их

С помощью difference возвращаем множество, полученное из различий между множествами

(![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/f3f71da9-d36b-4fae-b74e-89cc6000334f)

____
## Задание 09
В переменной sweets создаем словарь цен на продукты

Выводим их
![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/72a08f85-67e4-410f-ba9d-17a5bab99efe)

____
## Задание 10
1. В lamp_cost и др находим общую сумму товаров
2. В lamp_quantity находим общее количество товаров
3. Выводим результат

![image](https://github.com/MTrucky/laba_1/assets/146337304/e411c834-7176-443a-bb46-3cb5e26a6b93)
____
# 2 Лаба
## 1 Задание
Использовал команду `product` из модуля `itertools`

Просчитал все варианты кодового слова

![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/b6a9da40-de0b-4054-b345-28a52cc74091)

____
## 2 Задание
Записал полученное число в троичной системе исчисления, просчитал количество 2 с помощью команды `count`

![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/1165e2c0-e551-40d4-a321-606ec0f57ba2)

____
## 3 Задание
Сделал функцию, проверяющую число на нечетные делители и возвращающее их число, с учётом единицы и самого числа

![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/06e3fbed-9b03-47b8-badb-44d79fcb153c)
____
# 3 Лаба
## 1 Задание, итеративное
Удалял по элементу из списка, при виде `int` добавлял в сумму

При виде `list` раскрывал список и удалял вложенный список

![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/63d58a4c-25d1-4d64-bdd9-2d74aa7d5f38)

____
## 1 Задание, рекурсивное
Создал функцию и реализовал в ней рекурсию с таким-же функционалом

![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/aa82e1e8-b948-45fb-aa8f-25e3d2b3e3b3)

____
## 2 Задание, итеративное
Сделал формулу по которой будет высчитываться следующее значение списка, и включил её в ограниченый цикл, чтобы показать результат

![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/b1940a5b-1494-4910-ac1c-02e2de64d11e)


____
## 2 Задание, рекурсивное
Сделал функцию и реализовал в ней рекурсию, высчитывающую следующее значение списка

![изображение](https://github.com/arslanbekovdamir/lab1/assets/163137977/3126d4a7-4c2a-4a30-9d7d-1490c64f28d9)
____
## Использованные источники
Рекурсивные функции на пайтоне:
https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-13-rekursivnye-funkcii-2023-01-23 
____
Обьяснение работы рекурсии:
https://habr.com/ru/articles/337030/






