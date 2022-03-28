#Перестановка
from random import randint


def output(mas, str_k):
    print("\n", str_k)
    for b in mas:
        print(b)


def encryption(mas):
    mas_res = [[] for i in range(0, len(mas))]
    mas_key = []
    for f in mas[0]:
        mas_key.append(f)
    mas_key.sort()
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
key_mas_two = mas_two[1]

mas_three = [
        [4,   1,   3,   2],
    [3, "п", "р", "и", "л"],
    [1, "е", "т", "а", "ю"],
    [4, "в", "о", "с", "ь"],
    [2, "м", "о", "г", "о"]
]
key_mas_three_one = mas_three[0]
key_mas_three_two = []

for a in mas_three[1:]:
    key_mas_three_two.append(a[0])

# output(mas_one, "первая матрица")
# output(mas_two, "вторя матрица")
# output(mas_three, "третья матрица")
output(encryption(mas_two), "Результат")
