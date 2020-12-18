text = open("text.txt", "r").readlines()  # для роботи потрібен файл text.txt в якому знаходиться текст
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
key = open("key.txt", "r").readlines()


def encrypt(key, text_list, alphabet):
    """ шифрує текст """
    for key_index in range(len(key)):
        local_encrypted = ""
        key_list = list(key[key_index])
        if key_index != len(key) - 1:
            key_list.remove("\n")
        for i in range(len(text_list)):
            while len(text_list) > len(key_list):
                key_list += key_list
            local_encrypted += alphabet[(alphabet.index(text_list[i].lower()) + alphabet.index(key_list[i].lower())) % 26]
        text_list = local_encrypted
    encrypted_text = text_list

    return encrypted_text


result = open("encrypted.txt", "a")
for text_row in text:
    text_row = list(text_row)
    text_list = []
    for i in text_row:
        if i.isalpha():
            text_list.append(i)
    result.write(encrypt(key, text_list, alphabet) + "\n")
result.close()
