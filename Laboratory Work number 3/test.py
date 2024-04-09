nested = [1,[1],[1,[2]], [2, [3, 4, [5]]]]
suma = 0
while (len(nested)) != 0:
    if type(nested[0]) == int:
        nested.extend(nested[1])
        suma += nested[0]
        nested.pop(0)
        nested.pop(0)
        #print(nested)
        #print(suma)
    if (len(nested)) == 1:
        suma += nested[0]
        nested.pop()
        break
    if type(nested[1]) == int:
        suma += nested[0]
        nested.pop(0)
print(suma)
            

