# interface.py - Разбор аргументов командной строки

import argparse
from utils import help


# Так как у каждой команды разное количество параметров, то удобнее использовать подпарсеры,
# для каждого из которого будет свой специфичный набор команд (по другому не знаю как делать)

def parse_arguments(args):
    parser = argparse.ArgumentParser(description="Менеджер файловой системы")
    subparsers = parser.add_subparsers(dest='command', help='Команды файлового менеджера')

    if args[0] == 'copy' or args[0] == 'search':
        if len(args) != 3:
            raise TypeError
    elif args[0] == 'delete' or args[0] == 'count' or args[0] == 'add_date':
        if len(args) != 2:
            raise TypeError

    # Команда copy
    copy_parser = subparsers.add_parser('copy', help='Копировать файл')
    copy_parser.add_argument('source', help='Исходный файл')
    copy_parser.add_argument('destination', help='Конечный файл')

    # Команда delete
    delete_parser = subparsers.add_parser('delete', help='Удалить файл или папку')
    delete_parser.add_argument('path', help='Путь к файлу или папке')

    # Команда count
    count_parser = subparsers.add_parser('count', help='Подсчитать количество файлов в папке')
    count_parser.add_argument('path', help='Путь к папке')

    # Команда add_date
    # Работает только для одного файла или файлов одной папки (без рекурсивного обхода)
    add_date_parser = subparsers.add_parser('add_date',
                                            help='Добавить дату создания к имени файла или файлов папки')
    add_date_parser.add_argument('path', help='Путь к файлу или папке')

    # Команда search
    search_parser = subparsers.add_parser('search', help='Поиск папки')
    search_parser.add_argument('source_dir', help='Имя родительской папки для поиска')
    search_parser.add_argument('destination_dir', help='Имя папки для поиска')

    options = parser.parse_args(args)
    return options.command, options
