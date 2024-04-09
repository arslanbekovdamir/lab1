from math import sqrt 
#a = [1]
#b = [1]
#for i in range (10):
    #a[0] = ((1/2)*(sqrt(b[-1])) + ((1/2)*(sqrt(a[-1]))))
    #b[0] = ((3/2)*(sqrt(b[-1])) + ((1/2)*(a[-1]**2)))
i = 0
a = [1]
b = [1]
#print(a)
#print(b)
def deeef(a, b, i):
    i += 1
    if i == 10:
        return a, b
    else:
        a[0] = ((1/2)*(sqrt(b[-1])) + ((1/2)*(sqrt(a[-1]))))
        b[0] = ((3/2)*(sqrt(b[-1])) + ((1/2)*(a[-1]**2)))
        return deeef(a, b, i)
print(deeef(a, b, i))
