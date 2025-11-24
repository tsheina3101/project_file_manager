# file_manager.py - Основной файл запуска

import sys
from interface import parse_arguments
#from commands import copy_file, delete_file, count_files, add_date, search
from utils import help

def main():

    # Извлекаем все части командной строки, кроме имени файла в виде списка
    # с помощью модуля sys, так как это проще.
    # Их анализ будет производиться в модуле interface
    args = sys.argv[1:]

    if not args or args[0] == 'help': # нет аргументов командной строки или вызван help
        help() # вызываем функцию для вывода справки
        return

    try:
        # Разбираем аргументы командной строки, используя функцию parse_arguments из модуля interface
        command, options = parse_arguments(args)

        if command == 'copy':
            copy_file(options.source, options.destination)
        elif command == 'delete':
            delete_file(options.path)
        elif command == 'count':
            count_files(options.path)
        elif command == 'add_date':
            add_date(options.path)
        elif command == 'search':
            search(options.source_dir, options.destination_dir)
        else:
            print("Неизвестная команда. Используйте 'help' для списка команд.")

    except Exception as e:
         print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
