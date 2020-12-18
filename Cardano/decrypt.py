key = [[1, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1],
       [1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 1, 0, 1, 0, 0]]

text = open("cipher_result.txt", "r").read()


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


def decoding(key, text):
    """
    Створює матрицю із зашифрованого тексту, після цього розшифровує матрицю за допомогою ключа
    """
    text_list = []
    for i in range(len(key), len(key) * len(key) + len(key), len(key)):
        text_list.append(text[i - len(key):i])
    encrypted_matrix = []
    for i in text_list:
        encrypted_matrix.append(list(i))

    decoding_text = ""
    count = 0
    while count != 4:
        count += 1
        for i in range(len(key)):
            for x in range(len(key)):
                if key[i][x] == 1:
                    decoding_text += str(encrypted_matrix[i][x])
        key = povorot(key)

    return decoding_text.strip("0")


cipher_text = open("decoding_result", "x")
cipher_text.write(decoding(key, text))
cipher_text.close()
print(decoding(key, text))
