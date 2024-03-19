import itertools
n = 0
for i in itertools.product("XYZ", "ABC", "ABC", "ABC"):
    n += 1
print(n)

