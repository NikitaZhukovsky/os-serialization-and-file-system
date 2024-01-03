import re


with open('some_data.txt', 'r') as file:
    if file.read().strip() == '':
        print("Файл пуст.")
    else:
        file.seek(0)
    for line in file:
        numbers = re.findall(r'\d+', line)

        sum_numbers = 0
        for number in numbers:
            sum_numbers += int(number)

        print(f"Сумма чисел в строке: {sum_numbers}")
