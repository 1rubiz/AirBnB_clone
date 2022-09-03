#!/usr/bin/python3


""" base module for the base model """
import uuid
from datetime import datetime
# storage variable
import models

class BaseModel:
	""" main class model """
	def __init__(self, *args, **kwargs):
		""" Constructor and re-create an instance with
       		this dictionary representation"""
		if len(kwargs) > 0:
			for key, value in kwargs.items():
				if key == "created_at" or key == "updated_at":
					value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.f%")
				elif key == "__class__":
					continue
				setattr(self, key, value)
		else:
			#generates a random id
			self.id = str(uuid.uuid4())
			# assigns time
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			# calls the model storage on new instance
			models.storage.new(self)

	def __str__(self):
		myStr = "[{0}] ({1}) {2}".format((type(self).__name__,self.id,self.__dict__))
		return (myStr)
	def save(self):
		self.updated_at = datetime.now().isoformat
	def to_dict(self):
		myDict = {}
		myDict["__class__"] = type(self).__name__

		for key, value in self.__dict__.items():
			if isinstance(value, datetime):
				myDict[key] = value.isoformat()
			else:
				myDict[key] = value
		return (myDict)
