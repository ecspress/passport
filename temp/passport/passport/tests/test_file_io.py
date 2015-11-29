"""Tests the file_io module"""
import os
from passport.file_io import FileHandler
import unittest


class FileIOTest(unittest.TestCase):
    """Contains tests for the file_io module"""
    files = {"dummy":("./passport/tests/data-files/dummy-file", b"dummy data represented as bytes"),
             "empty":("./passport/tests/data-files/empty-file", b""),
             "written-data":("./passport/tests/data-files/written-file",
                             b"dummy data represented as bytes"),
             "written-empty":("./passport/tests/data-files/written-empty-file", b"")
            }

    def test_read_file(self):
        """Read dummy file in byte mode and check its contents"""
        data_file = FileHandler(self.files["dummy"][0])
        data = data_file.read_file()
        self.assertEqual(data, self.files["dummy"][1])

    def test_read_empty_file(self):
        """Read empty file in byte mode and check its contents"""
        data_file = FileHandler(self.files["empty"][0])
        data = data_file.read_file()
        self.assertEqual(data, self.files["empty"][1])

    def test_read_missing_file(self):
        """Try to read file that doesnt exist"""
        data_file = FileHandler("")
        self.assertRaises(FileNotFoundError, data_file.read_file)

    def test_write_data(self):
        """Write data into file and check if written correctly"""
        file_name = self.files["written-data"][0]
        file_data = self.files["written-data"][1]

        data_file = FileHandler(file_name)
        data_file.write_file(file_data)

        data = data_file.read_file()
        os.remove(file_name)
        self.assertEqual(data, file_data)

    def test_write_empty_data(self):
        """Write empty data into file and check if written correctly"""
        file_name = self.files["written-empty"][0]
        file_data = self.files["written-empty"][1]

        data_file = FileHandler(file_name)
        data_file.write_file(file_data)

        data = data_file.read_file()
        os.remove(file_name)
        self.assertEqual(data, file_data)

    def test_write_wrong_data(self):
        """Try to write data that is not bytes to file in byte mode"""
        types = [5, 5.4, "fes", None, True]
        data_file = FileHandler("")
        for typ in types:
            self.assertRaises(TypeError, data_file.write_file, typ)
