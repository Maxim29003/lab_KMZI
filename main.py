#Перестановка
from random import randint


def output(mas, str_k):
    print("\n", str_k)
    for b in mas:
        print(b)


def encryption(mas, button=True, key=[]):
    mas_res = [[] for i in range(0, len(mas))]
    mas_key = []
    if button == True:
        for f in mas[0]:
            mas_key.append(f)
        mas_key.sort()
    else:
        for f in key:
            mas_key.append(f)
    for c in mas_key:
        index = mas[0].index(c)
        for i in range(0, len(mas)):
            mas_res[i].append(mas[i][index])
    return mas_res


mas_one = [
    [7,    2,   5,   3,   4,   1,   6],
    ["т", "н", "п", "в", "е", "г", "л"],
    ["е", "а", "р", "а", "д", "о", "н"],
    ["р", "т", "и", "е", "ь", "в", "о"],
    ["м", "о", "б", "т", "м", "п", "ч"],
    ["и", "р", "ы", "с", "о", "о", "ь"]
]

mas_two = [
    [7,    2,   5,   3,   4,   1,   6],
    ["п", "е", "л", "и", "к", "а", "н"],
    ["т", "н", "п", "в", "е", "г", "л"],
    ["е", "а", "р", "а", "д", "о", "н"],
    ["р", "т", "и", "е", "ь", "в", "о"],
    ["м", "о", "б", "т", "м", "п", "ч"],
    ["и", "р", "ы", "с", "о", "о", "ь"]
]


m = encryption(mas_two)
output(m,"Зашивровал")
output(encryption(m,False,mas_two[0]),"hfc")
