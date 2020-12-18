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


def bigrams_index(text, matrix_key):
    """ визначаю індекси рядка і стовбця для кожної літери біграми """
    bigrams_list = []
    for index in range(0, len(text), 2):
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


def decrypt(matrix_key, bigrams_index):
    """ повертаю індекси біграм на свої місця"""
    decrypted_text = ""
    for i in bigrams_index:
        if i[0][1] == i[1][1]:
            decrypted_text += matrix_key[i[0][0] - 1][i[0][1]] + matrix_key[i[1][0] - 1][i[1][1]]
        elif i[0][0] == i[1][0]:
            decrypted_text += matrix_key[i[0][0]][i[0][1] - 1] + matrix_key[i[1][0]][i[1][1] - 1]
        else:
            decrypted_text += matrix_key[i[0][0]][i[1][1]] + matrix_key[i[1][0]][i[0][1]]
    if decrypted_text[-1] == "x":              # вирізаю х з кінця речення, якщо він є
        decrypted_text = decrypted_text[:-1]
    if "x" in decrypted_text:
        if decrypted_text[decrypted_text.index("x") - 1] == decrypted_text[decrypted_text.index("x") + 1]:
            decrypted_text = decrypted_text[:decrypted_text.index("x")] + decrypted_text[decrypted_text.index("x") + 1:]  # вирізаю х, якщо він знаходиться між двох однакових символів
    result.write(decrypted_text + "\n")

    return "End"


result = open("decrypted.txt", "a")
for i in open("encrypted.txt").readlines():
    i = list(i)
    i.remove("\n")
    decrypt(matrix_key, bigrams_index(i, matrix_key))

result.close()
