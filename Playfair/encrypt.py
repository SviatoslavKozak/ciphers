matrix_key = []
text = open("key.txt", "r").readlines()
for i in text:
    local_matrix = []
    i = list(i)
    if "\n" in i:
        i.remove("\n")
    for x in i:
        if x != " ":
            local_matrix.append(x)
    matrix_key.append(local_matrix)


def insert_x(text):
    """ вставляю x між літерами які повторяються"""
    insert_x = ""
    for i in range(len(text)):
        if text[i - 1] == text[i]:
            insert_x += "x"
            insert_x += text[i]
        else:
            insert_x += text[i]

    return insert_x


def bigrams_index(text, matrix_key):
    """ визначаю індекси рядка і стовбця для кожної літери біграми """
    bigrams_list = []
    for index in range(0, len(text), 2):
        if index + 1 > len(text) - 1:
            bigrams_list.append(text[index] + "x")
        else:
            bigrams_list.append(text[index] + text[index + 1])

    items_index = []
    for items in bigrams_list:
        item_index = []
        for item in items:
            for i in range(len(matrix_key)):
                for x in range(len(matrix_key)):
                    if matrix_key[i][x] == item:
                        item_index.append([i, x])
        items_index.append(item_index)

    return items_index  # список індексів біграм


def encrypt(bigrams_index, matrix_key):
    """ Міняю місцями індекси рядків в біграм. Перевіряю чи індекси не виходять за межі"""
    encrypted_text = ""
    for i in bigrams_index:
        if i[0][1] == i[1][1]:
            if i[0][0] + 1 > len(matrix_key) - 1:
                encrypted_text += matrix_key[i[0][0] - len(matrix_key) + 1][i[0][1]] + matrix_key[i[1][0] + 1][i[1][1]]
            elif i[1][0] + 1 > len(matrix_key) - 1:
                encrypted_text += matrix_key[i[0][0] + 1][i[0][1]] + matrix_key[i[1][0] - len(matrix_key) + 1][i[1][1]]
            else:
                encrypted_text += matrix_key[i[0][0] + 1][i[0][1]] + matrix_key[i[1][0] + 1][i[1][1]]
        elif i[0][0] == i[1][0]:
            if i[0][1] + 1 > len(matrix_key) - 1:
                encrypted_text += matrix_key[i[0][0]][i[0][1] - len(matrix_key) + 1] + matrix_key[i[1][0]][i[1][1] + 1]
            elif i[1][1] + 1 > len(matrix_key) - 1:
                encrypted_text += matrix_key[i[0][0]][i[0][1] + 1] + matrix_key[i[1][0]][i[1][1] - len(matrix_key) + 1]
            else:
                encrypted_text += matrix_key[i[0][0]][i[0][1] + 1] + matrix_key[i[1][0]][i[1][1] + 1]
        else:
            encrypted_text += matrix_key[i[0][0]][i[1][1]] + matrix_key[i[1][0]][i[0][1]]

    return encrypted_text + "\n"


encrypted_result = open("encrypted.txt", "a")
for i in open("text.txt").readlines():
    text = ""
    for x in i:
        if x != " " and x != "\n":  # забираю пробіли і службові закінчення із тексту
            text += x.lower()
    text = insert_x(text)
    encrypted_result.write(encrypt(bigrams_index(text, matrix_key), matrix_key))
encrypted_result.close()
