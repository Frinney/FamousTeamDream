import time


b = 41
#b = ответ на первую загадку
h = 2
#h = ответ на воторую загадку
m = 21
#m = ответ на третью загадку
score = 0
hpHero = 100
hpDragon = 250
damageHero = 25
damageDragon = 10
damageGoblin1 = 10
hpGoblin1 = 100
damageGoblin2 = 10
hpGoblin2 = 100
damageGoblin3 = 10
hpGoblin3 = 100
damageGoblin4 = 10
hpGoblin4 = 100
damageGoblin5 = 10
hpGoblin5 = 100
live = True

print("Начало игры")
time.sleep(3)
print("Число исполнившихся мне в этом году лет во многом примечательно.\n"
    "Если от этого числа отнять 2, то оно разделится на 3, а если от него отнять 3, то оно разделится на 2.\n"
    "Если к нему прибавить 4, то оно разделится на 5, а если от него отнять 5, то оно разделится на 4.\n"
    "Если от него отнять 5, то оно разделится на 6, а если от него отнять 6, то оно разделится на 5.\n"
    "Если к нему прибавить 7, то оно разделится на 8, а если к нему прибавить 8, то оно разделится на 7.\n"
    "Сколько же лет мне исполнилось в этом году?\n")
print("Напишите сюда ответ.С маленькой буквы")
a = int(input())
if a == b:
    print("Вы получаете меч который дает вам больше урона")
    damageHero = damageHero + 10
    score = score + 10
    print("Вы прошли уровень и получили меч")
    print("Кирпич весит 1 килограмм плюс половину собственного веса.Сколько весит кирпич?")

    print("Напишите сюда ответ")
    f = int(input())
    if f == h:
        print("Вы получаете броню который дает вам больше урона")
        hpHero = hpHero + 10
        score = score + 10
        print("Следующая загадка")
        print("Через два часа до полуночи останется в два раза меньше, чем оставалось бы через час.")
        print("Напишите сюда ответ")
        n = int(input())
        if n == m:
            print("Вы получаете меч который дает вам больше урона")
            damageHero = damageHero + 10
            score = score + 10
            print("Теперь битва с боссом")
            while live:
                print("Чтобы ударить дракона напишите 1")
                d = int(input())
                if d == 1:
                    hpDragon = hpDragon - damageHero
                if hpDragon == 0:
                    print("Вы убили дракона")
                    score = score + 5
                    live = False
                    print("Вы спасли принцессу")
                if hpDragon< 0:
                    print("Вы убили дракона")
                    score = score + 5
                    live = False
                    print("Вы спасли принцессу")
                if d != 1:
                    print("Вы промохнулись")
                    hpHero = hpHero - damageDragon
                    if hpHero == 0:
                        live = True







    if a != b:
        print("1 - Дратся с монстрами и пройти дальше и получить какой-то предмет\n"
              "2 - Убежать и ничего не получать")
    c = int(input())
    if c == 1:
        print("Вы не угадали загадку и решили начать драться против вас 5 гоблинов.Удачи вам")
        while live:
            print("Чтобы ударить гоблина напишите 1")
            d = int(input())
            if d == 1:
                hpGoblin1 = hpGoblin1 - damageHero
            if hpGoblin1 == 0:
                print("Вы убили первого гоблина")
                score = score + 1
                live = False
            if hpGoblin1 < 0:
                print("Вы убили первого гоблина")
                score = score + 1
                live = False
            if d != 1:
                print("Вы промохнулись")
                hpHero = hpHero - damageGoblin1
                if hpHero == 0:
                    live = True
        live = True
        while live:
            print("Чтобы ударить гоблина напишите 1")
            d = int(input())
            if d == 1:
                hpGoblin2 = hpGoblin2 - damageHero
            if hpGoblin2 == 0:
                score = score + 1
                print("Вы убили второго гоблина")
                live = False
            if hpGoblin2 < 0:
                print("Вы убили второго гоблина")
                score = score + 1
                live = False
            if d != 1:
                print("Вы промохнулись")
                hpHero = hpHero - damageGoblin2
                if hpHero == 0:
                    live = True
        live = True
        while live:
            print("Чтобы ударить гоблина напишите 1")
            d = int(input())
            if d == 1:
                hpGoblin3 = hpGoblin3 - damageHero
            if hpGoblin3 == 0:
                print("Вы убили третьего гоблина")
                score = score + 1
                live = False
            if hpGoblin2 < 0:
                print("Вы убили третьего гоблина")
                score = score + 1
                live = False
            if d != 1:
                print("Вы промохнулись")
                hpHero = hpHero - damageGoblin3
                if hpHero == 0:
                    live = True
        live = True
        while live:
            print("Чтобы ударить гоблина напишите 1")
            d = int(input())
            if d == 1:
                hpGoblin4 = hpGoblin4 - damageHero
            if hpGoblin4 == 0:
                print("Вы убили четвертого гоблина")
                score = score + 1
                live = False
            if hpGoblin2 < 0:
                print("Вы убили четвертого гоблина")
                score = score + 1
                live = False
            if d != 1:
                print("Вы промохнулись")
                hpHero = hpHero - damageGoblin4
                if hpHero == 0:
                    live = True
        live = True
        while live:
            print("Чтобы ударить гоблина напишите 1")
            d = int(input())
            if d == 1:
                hpGoblin5 = hpGoblin5 - damageHero
            if hpGoblin5 == 0:
                print("Вы убили пятого гоблина")
                score = score + 1
                live = False
            if hpGoblin5 < 0:
                print("Вы убили пятого гоблина")
                score = score + 1
                live = False
            if d != 1:
                print("Вы промохнулись")
                hpHero = hpHero - damageGoblin5
                if hpHero == 0:
                    live = True
    if c == 2:
        print("Вы убежали от гоблинов и ничего не получили")
        print("Кирпич весит 1 килограмм плюс половину собственного веса.Сколько весит кирпич?")
        print("Напишите сюда ответ")
        f = int(input())
        if f == h:
            print("Вы угадали загадку")
            score = score + 10








