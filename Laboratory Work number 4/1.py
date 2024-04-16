import time
def decorator(sply):
    i = 0
    def wrapper():
        nonlocal i
        i += 1
        print('Анабиоз будет длиться =', i )
        sply(i)
    return wrapper
@decorator
def son(i):
    time.sleep(i)
    print("Можно снова вызывать функцию")
while True:
    a = int(input("Введите : 1 чтобы вызвать функцию"))
    if a == 1:
        son()
