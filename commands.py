# commands.py - Функции для работы с файлами (обработка команд)
import os
import shutil  # модуль для выполнения высокоуровневых действий с файлами
from datetime import datetime


# Копирования файлов в модуле os нет, поэтому использую модуль shutil
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Файл '{source}' скопирован в '{destination}'")
    except FileNotFoundError:  # нужный файл не найден
        print(f"Ошибка: Файл '{source}' не найден.")
    except Exception as e:  # другие ошибки копирования
        print(f"Ошибка при копировании: {e}")


# удаление файла или папки
def delete_file(path):
    try:
        if os.path.isfile(path):  # если это файл
            os.remove(path)
            print(f"Файл '{path}' удален.")
        elif os.path.isdir(path):  # если это папка
            shutil.rmtree(path)
            print(f"Папка '{path}' удалена.")
        else:  # ошибка имени
            print(f"Ошибка: Файл или папка '{path}' не найден.")
    except FileNotFoundError:  # файл не найден
        print(f"Ошибка: Файл или папка '{path}' не найден.")
    except Exception as e:  # прочие ошибки
        print(f"Ошибка при удалении: {e}")


# подсчет файлов
def count_files(path):
    count = 0
    if os.path.isdir(path):
        for _, _, files in os.walk(path):  # функция рекурсивного обхода дерева каталогов
            # первые два параметра пропущены, так как считаем только файлы
            count += len(files)
        print(f"Количество файлов в папке '{path}' и вложенных папках: {count}")
        return count
    else:
        print(f"Папка '{path}' не существует")
        return -1


# добавление даты к имени файла или к именам всех файлов внутри папки (без рекурсии)
def add_date(path):
    if os.path.isfile(path):  # если файл
        add_date_to_file(path)  # вызов функции добавления даты
        return True
    elif os.path.isdir(path):  # если папка
        for file in os.listdir(path):  # обходим все файлы
            file_path = os.path.join(path, file)  # формируем имя (путь)
            if os.path.isfile(file_path):  # если это файл (не папка)
                add_date_to_file(file_path)  # вызываем функцию добавления даты
        return True
    else:
        print(f"Ошибка: '{path}' не является файлом или папкой.")
        return False

# функция добавления даты к одному файлу
def add_date_to_file(file_path):
    try:
        # формируем текущую дату в формате ЧислоМесяцГод
        date_time = datetime.today().strftime("%d%m%Y")
        # выделяем имя файла из пути
        dir_name, file_name = os.path.split(file_path)
        # выделяем имя и расширение имени
        name, ext = os.path.splitext(file_name)
        # добавляем дату к имени
        new_name = f"{name}_{date_time}{ext}"
        # формируем новый путь к файлу
        new_path = os.path.join(dir_name, new_name)
        # переименовываем файл
        print(new_path)
        os.rename(file_path, new_path)
        print(f"Переименован '{file_path}' в '{new_path}'")
    except Exception as e:
        print(f"Ошибка при переименовании файла: {e}")


# генераторная функция для чтения текущей папки или файла
def gen_files_path(cur_path, my_dir):
    for current_dir in os.walk(cur_path):
        yield (current_dir)

# функция поиска папки
def search(source_dir, destination_dir):
    if not os.path.isdir(source_dir):
        print(f"Ошибка: '{source_dir}' не является папкой.")
    try:
        gen = gen_files_path(source_dir, destination_dir)
        # перебираем все вложенные папки и файлы
        for i_element in gen:
            if destination_dir in i_element[1]:  # если имя содержится в списке вложенных папок и файлов
                print('Папка найдена. Путь к папке: ')
                print(os.path.join(i_element[0], destination_dir))  # вывод пути
                return True
        else:
            print("Папка не найдена")
            return False
    except Exception as e:
        print(f"Ошибка поиска: {e}")
