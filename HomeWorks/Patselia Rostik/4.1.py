import random

s = "1234567890"
psw = ''

for x in range(int(1)):
    psw += random.choice(s)

print(psw)

a = int(input())

if a == psw:
    print(Ты угадал)
if a < psw: a > psw:
    print(Ты не угадал)