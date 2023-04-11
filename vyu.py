'gffththk'
from random import randint


def l1():
    a = []
    for i in range(5):
        a.append(randint(0, 30))
    x = int(input("введите число от 0 до 30 "))
    if x in a:
        print(a, "Поздравляю, Вы угадали число!")
    else:
        print(a, "Нет такого числа!")


l1()


def l2():
    a = []
    k = 0
    for i in range(5):
        a.append(randint(0, 20))
    for i in a:
        for j in a:
            if i == j:
                k = k + 1
    k = k - int(len(a))
    if k > 0:
        print(a,' количество повторов ', k )
    else:
        print(a, "нет повторов")


l2()


def l3():
    a = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    x = int(input("введите количество выходных "))
    k = int(len(a)) - x
    print("ваши рабочие дни - ", a[:k], " ", "ваши выходные - ", a[k:])


l3()


def l4():
    a = ["Михайлова", "Крылова", "Чухвитская", "Иванов", "Бекренева", "Панин", "Чувашев", "Гончарова", "Волхов",
         "Воронина"]
    b = ["Пикин", "Шляпова", "Тюбиков", "Штрихов", "Иванов", "Савичева", "Валуева", "Путин", "Володин", "Рогозин"]
    c = []
    while len(c) != 5:
        x = randint(0, 9)
        if not (a[x] in c):
            c.append(a[x])
    while len(c) != 10:
        x = randint(0, 9)
        if not (b[x] in c):
            c.append(b[x])
    t = tuple(c)
    print("1 группа - ", a)
    print("2 группа - ", b)
    print("команда - ", t, " длина - ", len(c))
    p = tuple(sorted(t))
    print("по алфавиту - ", p)
    if p.count("Иванов") > 0:
        print("Иванов входит в команду - ", p.count("Иванов"))
    else:
        print("Иванов не входит в команду")


l4()