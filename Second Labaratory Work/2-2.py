  # 9 ^ 8 + 3 ^ 5 − 9  записали в системе счисления с основанием 3. 

n = ((9**8) + (3**5) - 9)
string = ''
while n > 0:
    string+=str(n%3)
    n//= 3
print(string.count("2"))

