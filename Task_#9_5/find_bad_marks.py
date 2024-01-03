print("Учащиеся с неудовлетворительной отметкой:")

with open('marks.txt', 'r', encoding='UTF-8') as file:
    if file.read().strip() == '':
        print("Файл пуст.")
    else:
        file.seek(0)
    for line in file:
        surname, name, mark = line.strip().split()
        if int(mark) < 3:
            print(surname, name, mark)
