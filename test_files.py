# test_main.py - Unit-тесты
import unittest
import os
import shutil
from commands import *
from interface import parse_arguments
from datetime import datetime


class TestFileManager(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые директории и файлы
        ''' Структура текстовых директорий:
        test_dir --
                   |
                   one --
                        |
                        empty_dir
                        test.txt
                   two --
                        |
                        test1.txt
                        test2.txt
        '''
        self.test_dir = "test_dir"
        self.test_dir1 = "test_dir/one/"
        os.makedirs(self.test_dir1, exist_ok=True)
        self.test_file = os.path.join(self.test_dir1, "test.txt")
        with open(self.test_file, "w") as f:
            f.write("test content")
        self.empty_dir = os.path.join(self.test_dir1, "empty_dir")
        os.makedirs(self.empty_dir, exist_ok=True)
        self.test_dir2 = "test_dir/two/"
        os.makedirs(self.test_dir2, exist_ok=True)
        self.test_file1 = os.path.join(self.test_dir2, "test1.txt")
        with open(self.test_file1, "w") as f:
            f.write("test content")
        self.test_file2 = os.path.join(self.test_dir2, "test2.txt")
        with open(self.test_file2, "w") as f:
            f.write("test content")

    def tearDown(self):
    # Удаляем тестовые директории и файлы после каждого теста
        shutil.rmtree(self.test_dir)

    def test_parse_argument(self):
        command, options = parse_arguments(['copy', 'source.txt', 'dest.txt'])
        self.assertEqual(command, 'copy')
        self.assertEqual(options.source, 'source.txt')
        self.assertEqual(options.destination, 'dest.txt')

    def test_copy_file(self):
        dest_file = os.path.join(self.test_dir1, "test_copy.txt")
        copy_file(self.test_file, dest_file)
        self.assertTrue(os.path.exists(dest_file))
        with open(dest_file, "r") as f:
            self.assertEqual(f.read(), "test content")

    def test_count_files(self):
        count = count_files(self.test_dir2)
        self.assertEqual(count, 2)

    def test_add_date(self):
        add_date(self.test_dir1)
        date_time = datetime.today().strftime("%d%m%Y")
        file1 = "test_" + date_time + '.txt'
        self.assertTrue(os.path.exists(self.test_dir1))

    def test_delete_file(self):
        delete_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))

    def test_delete_dir(self):
        delete_file(self.empty_dir)
        self.assertFalse(os.path.exists(self.empty_dir))

    def test_search(self):
        print(self.test_dir,"two")
        self.assertTrue(search(self.test_dir,"two"))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
