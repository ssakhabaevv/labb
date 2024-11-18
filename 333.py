def show_alphabet_with_indices():
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    print("Алфавит и нумерация:")
    for i, letter in enumerate(alphabet):
        print(f"{i}: {letter}", end='  ')
    print("\n")
def gronsfeld_encrypt(message, key):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    message = message.replace(' ', '').upper()
    key = [int(d) for d in str(key)]
    encrypted_message = []
    for i, char in enumerate(message):
        if char in alphabet:
            shift = key[i % len(key)]
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_message.append(alphabet[new_index])
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)
def gronsfeld_decrypt(encrypted_message, key):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    encrypted_message = encrypted_message.replace(' ', '').upper()
    key = [int(d) for d in str(key)]
    decrypted_message = []
    for i, char in enumerate(encrypted_message):
        if char in alphabet:
            shift = key[i % len(key)]
            new_index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_message.append(alphabet[new_index])
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)
show_alphabet_with_indices()
message = input("Введите текст для шифрования: ")
key = input("Введите числовой ключ: ")
encrypted_message = gronsfeld_encrypt(message, key)
print("Зашифрованное сообщение:", encrypted_message)
decrypted_message = gronsfeld_decrypt(encrypted_message, key)
print("Расшифрованное сообщение:", decrypted_message)
