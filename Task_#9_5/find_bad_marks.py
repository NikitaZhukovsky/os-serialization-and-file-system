print("Учащиеся с неудовлетворительной отметкой:")

with open('marks.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        surname, name, mark = line.strip().split()
        if int(mark) < 3:
            print(surname, name, mark)
