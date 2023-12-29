import re

text = input("Введите текст: ")
pattern = r'\b[А-ЯЁ][а-яё]*(?:-[А-ЯЁ][а-яё]*)*(?:\s[А-ЯЁ][а-яё]*){2}\b'
matches = re.sub(pattern, 'N', text)

print(matches)