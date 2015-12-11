import pickle
import json

def readFileBytes(file_name):
    with open(file_name, "rb") as data_file:
        data = data_file.read()
    	return data

def writeBytesToFile(file_name, data):
    if not isinstance(data, bytes):
	    raise TypeError("Data to be written must be of type bytes")

    with open(file_name, "wb") as data_file:
        data_file.write(data)

def convertStringToBytes(str):
	return pickle.dumps(str)

def convertBytesToString(bytes):
	return pickle.loads(bytes)

def convertUserToString(obj):
	return json.dumps(obj, ascii=True)

def convertStringToUser(data):
	return json.loads(data)