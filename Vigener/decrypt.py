alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
key = open("key.txt", "r").readlines()
f = open("encrypted.txt", "r")
row_list = f.readlines()
decrypt_result = open("decrypted.txt", "a")


def decrypt(key, alphabet, row_list):
    """ розшифровує і записує в файл"""
    for i in row_list:
        for key_index in range(-1, -len(key) - 1, - 1):
            local_decrypt_text = ""
            key_list = list(key[key_index])
            i = list(i)
            if key_index != - 1:
                key_list.remove("\n")
            if key_index == -1:
                i.remove("\n")
            for x in range(len(i)):
                if x > len(key_list) - 1:
                    key_list += key_list
                local_decrypt_text += alphabet[(alphabet.index(i[x]) - alphabet.index(key_list[x].lower())) % 26]
            i = local_decrypt_text
        decrypted = i
        decrypted = decrypted + "\n"
        decrypt_result.write(decrypted)

    return "end"


decrypt(key, alphabet, row_list)
decrypt_result.close()


