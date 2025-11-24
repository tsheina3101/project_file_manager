# utils.py
def help():
    print("Для запуска файлового менеджера наберите команду: python main.py <command> [options]")
    print("Команды:")
    print("  copy <source> <destination> - Копировать файл")
    print("  delete <path> - Удалить файл или папку")
    print("  count <path> - Подсчитать кол-во файлов в папке")
    print("  add_date <path>  - Добавить дату создания к имени файла или файлов внутри папки")
    print("  search <namedir> - Поиск папки внутри каталога с выводом пути к нему")