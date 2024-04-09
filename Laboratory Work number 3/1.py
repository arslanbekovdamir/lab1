from math import sqrt
a = [1]
b = [1]
for i in range (10):
    a[0] = ((1/2)*(sqrt(b[-1])) + ((1/2)*(sqrt(a[-1]))))
    b[0] = ((3/2)*(sqrt(b[-1])) + ((1/2)*(a[-1]**2)))
    
print(a)
print(b)
