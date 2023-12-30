import re


def censor_text(file_name):
    # Чтение запрещенных слов из файла stop_words.txt
    with open("stop_words.txt", "r", encoding="utf-8") as stop_words_file:
        stop_words = stop_words_file.read().split()

    # Чтение текстового файла для цензуры
    with open(file_name, "r", encoding="utf-8") as text_file:
        text = text_file.read()

    # Замена запрещенных слов звездочками
    for word in stop_words:
        pattern = r'(?i)\b' + re.escape(word)
        text = re.sub(pattern, '*' * len(word), text)

    # Вывод итогового текста
    print(text)


# Ввод названия текстового файла
input_file_name = input("Введите название текстового файла: ")

# Вызов функции для цензуры текста
censor_text(input_file_name)
