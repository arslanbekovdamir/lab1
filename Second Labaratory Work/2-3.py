#Найдите все натуральные числа, принадлежащие отрезку [40000; 50000] [40000; 50000] [40000; 50000], 
#у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым).
#Выведите найденные числа в порядке возрастания. 
def func(n):
    count = 0
    for i in range (1, n+1, 2):
        #if n % i == 0 and i % 2 == 1:
        if n % i == 0 and i % 2 == 1:
            count += 1
    return count

for i in range(40000, 50001):
    if func(i) == 5:
        print(i)