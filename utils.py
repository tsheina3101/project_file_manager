# utils.py
def help():
    print('''
     ФАЙЛОВЫЙ МЕНЕДЖЕР 
     Для запуска файлового менеджера наберите команду: python file_manager.py <command> [options]
     Команды:
     copy <source> <destination> - Копировать файл
     delete <path> - Удалить файл или папку
     count <path> - Подсчитать кол-во файлов в папке
     add_date <path>  - Добавить дату создания к имени файла или файлов внутри папки
     search <source_dir> <destination_dir> - Поиск папки внутри каталога с выводом пути к нему
     ''')