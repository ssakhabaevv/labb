def get_column_order(key):
    key_positions = sorted((char, index) for index, char in enumerate(key))
    order = [0] * len(key)
    current_number = 1
    for _, index in key_positions:
        order[index] = current_number
        current_number += 1
    return order
def print_table_with_key(table, key):
    print(" ".join(key))
    for row in table:
        print(" ".join(cell if cell else " " for cell in row))
def encrypt_with_single_permutation(text, key):
    text = text.replace(" ", "").upper()
    key = key.upper()
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    table = [[""] * num_cols for _ in range(num_rows)]
    index = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if index < len(text):
                table[row][col] = text[index]
                index += 1
    column_order = get_column_order(key)
    print("\nИсходная таблица:")
    print_table_with_key(table, key)
    sorted_column_indices = sorted(range(num_cols), key=lambda x: column_order[x])
    print("\nТаблица после перестановки колонок:")
    sorted_table = [[""] * num_cols for _ in range(num_rows)]
    for col, sorted_col in enumerate(sorted_column_indices):
        for row in range(num_rows):
            sorted_table[row][col] = table[row][sorted_col]
    print_table_with_key(sorted_table, [key[i] for i in sorted_column_indices])
    encrypted_text = ""
    for col in sorted_column_indices:
        for row in range(num_rows):
            if table[row][col]:
                encrypted_text += table[row][col]
    return encrypted_text
def decrypt_with_single_permutation(encrypted_text, key):
    key = key.upper()
    num_cols = len(key)
    num_rows = (len(encrypted_text) + num_cols - 1) // num_cols
    column_order = get_column_order(key)
    sorted_column_indices = sorted(range(len(column_order)), key=lambda x: column_order[x])
    col_lengths = [num_rows] * num_cols
    extra_cells = num_rows * num_cols - len(encrypted_text)
    for i in range(extra_cells):
        col_lengths[sorted_column_indices[-(i + 1)]] -= 1
    table = [[""] * num_cols for _ in range(num_rows)]
    index = 0
    for col, length in zip(sorted_column_indices, col_lengths):
        for row in range(length):
            table[row][col] = encrypted_text[index]
            index += 1
    print("\nТаблица при восстановлении текста:")
    print_table_with_key(table, key)
    decrypted_text = ""
    for row in range(num_rows):
        for col in range(num_cols):
            if table[row][col]:
                decrypted_text += table[row][col]
    return decrypted_text
text = input("Введите текст для шифрования: ").strip()
key = input("Введите ключ: ").strip()
encrypted_text = encrypt_with_single_permutation(text, key)
print("\nШифротекст:", encrypted_text)
decrypted_text = decrypt_with_single_permutation(encrypted_text, key)
print("\nДешифрованный текст:", decrypted_text)
