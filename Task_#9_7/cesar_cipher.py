with open('file_with_words.txt', 'r') as file:
    lines = file.readlines()

    encrypted_lines = []
    for i, line in enumerate(lines):
        key = i + 1
        encrypted_word = ""
        for letter in line:
            if letter.isdigit():
                encrypted_letter = letter
            elif 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
                if letter.isupper():
                    encrypted_letter = chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
                else:
                    encrypted_letter = chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
            elif 'А' <= letter <= 'я' or 'Ё' <= letter <= 'ё':
                if letter.isupper():
                    encrypted_letter = chr((ord(letter) - ord('А') + key) % 33 + ord('А'))
                else:
                    encrypted_letter = chr((ord(letter) - ord('а') + key) % 33 + ord('а'))
            else:
                encrypted_letter = letter
            encrypted_word += encrypted_letter
        encrypted_lines.append(encrypted_word)

    with open('cipher.txt', 'w') as file_cipher:
        file_cipher.writelines(encrypted_lines)
