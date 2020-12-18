key = [[1, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0]]

text = open("text.txt", "r").read()


def povorot(key):
    """
    Повертає матрицю на 90 градусів
    """
    key1 = []
    for i in range(len(key[0])):
        local_matrix = []
        for x in range(-1, -len(key)-1, -1):
            local_matrix.append(key[x][i])
        key1.append(local_matrix)

    return key1


def matrix(key):
    """
    Створює пусту матрицю наповнену нулями
    """
    encrypted_matrix = []
    for i in range(len(key)):
        encrypted_matrix.append([0 for x in range(len(key))])

    return encrypted_matrix


def cipher(key, text):
    """
    Використувуючи ключ замінює нулі пустої матриці на текст. Виводить строку зашифрованого тексту
    """
    encrypted_matrix = matrix(key)
    count = 0
    index = 0
    while count != 4:
        count += 1
        for i in range(len(key)):
            for x in range(len(key)):
                if key[i][x] == 1:
                    if len(text) <= index:
                        count = 4
                    else:
                        encrypted_matrix[i][x] = text[index]
                        index += 1
        key = povorot(key)
    encrypted_matrix1 = ""
    for i in encrypted_matrix:
        for x in i:
            encrypted_matrix1 += str(x)

    return encrypted_matrix1


result = open("cipher_result.txt", "x")  # якщо файл вже існує то буде вибивати помилку
result.write(cipher(key, text))
result.close()
print(open("cipher_result.txt", "r").read())







