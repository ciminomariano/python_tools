import io
import unittest

from crud_file_service import FileService


class TestUtils(unittest.TestCase):
    def test_create_file(self):
        class_instance = FileService()
        file_name = 'test_file.txt'
        created_file = FileService.create_file(class_instance, file_name)
        self.assertIsInstance(created_file, io.TextIOWrapper)

    def test_load_file(self):
        class_instance = FileService()
        file_name = 'test_file.txt'
        loaded_file = FileService.load_file(class_instance, file_name)
        self.assertIsInstance(loaded_file, io.TextIOWrapper)

    def test_read_file(self):
        class_instance = FileService()
        file_name = 'test_file.txt'
        loaded_file = FileService.read_file(class_instance, file_name, 'This is line 7\n')
        self.assertTrue(loaded_file, True)
