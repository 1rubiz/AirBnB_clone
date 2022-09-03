
import json
import os
from models.base_model import BaseModel

class FileStorage:
	__file_path = "file.json"
	__objects = {}
	def all(self):
		""" returns the dictionary __objects"""
		return (self.__objects)

	def new(self, obj):
		""" sets in __objects the obj with key <obj class name>.id """
		if obj:
			key = "{}.{}".format(obj.__class__.__name__, obj.id)
			self.objects[key] = obj

	def save(self):
		""" serializes __objects to the json file (path: __file_path)"""
		serialDict = {}
		allDict = FileStorage.__objects
		with open(FileStorage.__file_path, 'w') as f:
			for value in allDict.values():
				key = "{}.{}".format(value.__class__.__name__, value.id)
				serialDict[key] = value.to_dict()
			json.dump(serialDict, f)

	def reload(self):
		""" Desrializes the json file to __objects (only if
		the json file (__file_path) exits, otherwise. do 
		nothing. if the file doesn't exit, no exception
		should be raised) """
		if os.path.isfile(self.__file_path):
			with open(self.__file_path, 'r') as f:
				des_json = json.load(f)
				for key, value in des_desjson.items():
					k = key.split('.')
					class_name = k[0]
					#set key and value pair in __objects
					self.new(eval("{}".format(class_name))(**value))

