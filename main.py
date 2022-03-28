Matrix = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
MatrixLts = Matrix.split(',')
MatrixLts += Matrix.lower().split(',')
wordDict = {}
entr = 0
# wordDict [число повторений буквы в слове, вероятность, [нижняя граница, верхняя граница]]


def func3(word):
    global wordDict
    global entr
    wordDict[' '] = [0, 0.0, [0.0, 0.0]]
    for j in MatrixLts:
        wordDict[j] = [0, 0.0, [0.0, 0.0]]

    for i in word:
        wordDict[i][0] += 1

    MatrixLts1 = [' ']
    MatrixLts1 += MatrixLts
    print(MatrixLts1)
    varible = 0.0

    for q in MatrixLts1:
        if wordDict[q][0] != 0:
            wordDict[q][1] = wordDict[q][0]/len(word)
            wordDict[q][2][0] = varible
            wordDict[q][2][0] = float("{0:.12f}".format(wordDict[q][2][0]))
            wordDict[q][2][1] = varible = wordDict[q][1]+varible
            wordDict[q][2][1] = float("{0:.12f}".format(wordDict[q][2][1]))

    print(wordDict)
# lts = [верхняя граница = 0.0, нижняя граница = 1.0 ]

    lts = [0.0, 1.0]

    for i in word:
        if wordDict[i][0] != 0:
            interval = float("{0:.12f}".format(lts[1]-lts[0]))
            lts[1] = float("{0:.12f}".format(lts[0]+(interval*wordDict[i][2][1])))
            lts[0] = float("{0:.12f}".format(lts[0]+(interval*wordDict[i][2][0])))
            print(i, " -- ", lts)
    res = float("{0:.12f}".format( lts[0]))
    print("\n""Результат кодирования '{}' -- ".format(word), res, "\n")
    for i in MatrixLts1:
        for j in word:
            if (i == j):
                entr += 1
                break
    print("Энтропия = ", entr)


# декодирование
    print()
    str_res = ""
    ch = ""
    for i in word:
        for j in word:
            if wordDict[j][2][0] <= res <= wordDict[j][2][1]:
                ch = j
                break
        interval_one = wordDict[ch][2][1] - wordDict[ch][2][0]
        res = res - wordDict[ch][2][0]
        res = res / interval_one
        print("res -- ", res)
        str_res += ch
    print("\n""Декодирование -- ", str_res)


def func1(word, index):
    newWord = ""
    for i in word:
        if i == ' ':
            newWord += ' '
            continue
        if MatrixLts.index(i)+index <= len(MatrixLts):
            newWord += MatrixLts[MatrixLts.index(i)+index]
        else:
            newWord += MatrixLts[MatrixLts.index(i) + index - len(MatrixLts)]
    print(newWord)


def func2(word, index):
    newWord = ""
    for i in word:
        if i == ' ':
            newWord += ' '
            continue
        if MatrixLts.index(i)-index >= 0:
            newWord += MatrixLts[MatrixLts.index(i)-index]
        else:
            newWord += MatrixLts[MatrixLts.index(i) + len(MatrixLts) - index]
    print(newWord)

#func1("Book is very good ",13)
#func2("OBBx vF IrEL tBBq",13)
func3("BILL GATES")
