import json
import csv


# -----------------------------------------------------------------
def read_json(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return data


# -----------------------------------------------------------------
def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow(item.values())


# -----------------------------------------------------------------
def add_employee_json(file_name):
    data = read_json(file_name)
    new_employee = {
        'name': input("Имя сотрудника: "),
        'birthday': input("Возраст сотрудника: "),
        'height': float(input("Рост сотрудника: ")),
        'weight': float(input("Введите вес сотрудника: ")),
        'car': input("Есть ли у сотрудника машина: "),
        'languages': input("Язык программирования: ")
    }
    data.append(new_employee)
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)


# -----------------------------------------------------------------
def add_employee_csv(file_name):
    data = read_json(file_name)
    new_employee = {
        'name': input("Имя сотрудника: "),
        'birthday': input("Возраст сотрудника: "),
        'height': float(input("Рост сотрудника: ")),
        'weight': float(input("Введите вес сотрудника: ")),
        'car': input("Есть ли у сотрудника машина: "),
        'languages': input("Язык программирования: ")
    }
    data.append(new_employee)
    write_csv(file_name, data)


# -----------------------------------------------------------------
def get_info(file_name, name):
    data = read_json(file_name)
    for employee in data:
        if employee['name'] == name:
            print(f"Имя: {employee['name']}")
            print(f"Дата рождения: {employee['birthday']}")
            print(f"Рост: {employee['height']}")
            print(f"Вес: {employee['weight']}")
            print(f"Наличие автомобиля: {employee['car']}")
            print(f"Языки программирования: {employee['languages']}")
            return
    print("Сотрудник с указанным именем не найден.")


# -----------------------------------------------------------------
def filter_by_language(file_name, programming_language):
    data = read_json(file_name)
    filtered_employees = [
        employee for employee in data if programming_language in employee['languages']
    ]
    if filtered_employees:
        print(f"Сотрудники, владеющие языком программирования {programming_language}:")
        for employee in filtered_employees:
            print(f"Имя: {employee['name']}, языки программирования: {employee['languages']}")
    else:
        print(f"Нет сотрудников, владеющих языком программирования {programming_language}.")


# -----------------------------------------------------------------
def filter_by_birth_year(file_name, birth_year):
    data = read_json(file_name)
    filtered_employees = [employee for employee in data if int(employee['birthday'].split('.')[2]) < birth_year]
    if filtered_employees:
        print("Сотрудники, у которых год рождения меньше заданного:")
        for employee in filtered_employees:
            print(f"Имя: {employee['name']}, рост: {employee['height']}")

        heights = [employee['height'] for employee in filtered_employees]
        average_height = sum(heights) / len(heights)
        print("Средний рост сотрудников, у которых год рождения меньше", birth_year, ":", average_height)
    else:
        print("Нет сотрудников с годом рождения меньше", birth_year)


# -----------------------------------------------------------------
def menu():
    file_employee = 'employees.json'
    while True:
        print("Меню:")
        print("1. Чтение данных из JSON и преобразование в CSV")
        print("2. Сохранение данных в CSV")
        print("3. Добавление нового сотрудника в JSON")
        print("4. Добавление нового сотрудника в CSV")
        print("5. Вывод информации о сотруднике по имени")
        print("6. Фильтрация сотрудников по языку программирования")
        print("7. Фильтрация сотрудников по году рождения")
        print("8. Выход")

        choice = int(input("Выберите действие (1-8): "))

        match choice:
            case 1:
                data = read_json(file_employee)
                write_csv('output.csv', data)
                print("Данные успешно преобразованы в CSV.")
            case 2:
                data = read_json(file_employee)
                write_csv('output.csv', data)
                print("Данные успешно сохранены в CSV.")
            case 3:
                add_employee_json(file_employee)
                print("Новый сотрудник успешно добавлен в JSON.")
            case 4:
                add_employee_csv(file_employee)
                print("Новый сотрудник успешно добавлен в CSV.")
            case 5:
                input_name = input("Введите имя сотрудника: ")
                get_info(file_employee, input_name)
            case 6:
                input_language = input("Введите язык программирования: ")
                filter_by_language(file_employee, input_language)
            case 7:
                year = int(input("Введите год рождения: "))
                filter_by_birth_year(file_employee, year)
            case 8:
                print("Выход из программы.")
                break
            case _:
                print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 8.")


menu()
