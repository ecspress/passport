"""Contains FileHandler class"""

class FileHandler():
    """Handles io operations for a file"""
    def __init__(self, file_name):
        """Initialized the FileHandler object
        Input:
            file_name: string containing complete file name with path
        Output:
            None
        Raises:
            None
        """
        self.file_name = file_name

    def read_file(self):
        """Reads file in byte mode.
        Input:
            None
        Output:
            bytes: file data as bytes
        Raises:
            None
        """
        with open(self.file_name, "rb") as data_file:
            data = data_file.read()
        return data

    def write_file(self, data):
        """Writes byte data to file.
        Input:
            data: byte string containing data to write in file as bytes
        Output:
            None
        Raises:
            TypeError: if data is not bytes
        """
        if not isinstance(data, bytes):
            raise TypeError("Data to be written must be byte string")

        with open(self.file_name, "wb") as data_file:
            data_file.write(data)
