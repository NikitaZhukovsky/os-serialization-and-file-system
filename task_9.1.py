import os
import platform

# ----------------------------------------------------------------------------------
# Task №1
print("Имя операционной системы:", platform.system())

current_directory = os.getcwd()
print(f"Путь до папки: {current_directory}")

# Создание словаря для хранения папок по расширениям файлов
folders = {}

# Получение списка файлов в текущей директории
files = os.listdir(current_directory)

# Создание папок для каждого расширения файла, кроме .py
for file in files:
    if os.path.isfile(file):
        file_extension = os.path.splitext(file)[1][1:]  # Получение расширения файла
        if file_extension != 'py' and file_extension not in folders:
            folders[file_extension] = os.path.join(current_directory, file_extension)
            os.makedirs(folders[file_extension], exist_ok=True)

# Перемещение файлов в соответствующие папки, исключая файлы .py
for file in files:
    if os.path.isfile(file):
        file_extension = os.path.splitext(file)[1][1:]  # Получение расширения файла
        if file_extension != 'py' and file_extension in folders:
            source_path = os.path.join(current_directory, file)
            destination_path = os.path.join(folders[file_extension], file)
            os.replace(source_path, destination_path)


# Переименование хотя бы одного файла в каждой поддиректории и вывод сообщения
for extension, folder in folders.items():
    files_in_folder = os.listdir(folder)
    if files_in_folder:
        file_to_rename = files_in_folder[0]  # Выбираем первый файл в поддиректории для переименования
        new_name = "some_" + file_to_rename
        old_path = os.path.join(folder, file_to_rename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"Файл {file_to_rename} был переименован в {new_name}")

# Вывод информации о перемещенных файлах
for extension, folder in folders.items():
    file_count = sum(1 for _ in os.listdir(folder) if os.path.isfile(os.path.join(folder, _)))
    total_size = 0
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            total_size += file_size
    print(f"В папке {folder} перемещено {file_count} файлов, их суммарный размер - {total_size} байт")
