import pickle
import json

def read_file_bytes(file_name):
    with open(file_name, "rb") as data_file:
        data = data_file.read()
        return data

def write_bytes_to_file(file_name, data):
    if not isinstance(data, bytes):
	    raise TypeError("Data to be written must be of type bytes")

    with open(file_name, "wb") as data_file:
        data_file.write(data)

def convert_object_to_bytes(obj):
	return pickle.dumps(obj)

def convert_bytes_to_object(bytes):
	return pickle.loads(bytes)

def convert_object_to_string(obj):
	return json.dumps(obj, ascii=True)

def convert_string_to_object(data):
	return json.loads(data)