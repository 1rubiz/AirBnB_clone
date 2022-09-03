#!/usr/bin/python3
""" Program that contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
import sys

class HBNBCommand(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '
    def do_EOF(self, args):
	print()
	return True

    def do_create(self, arg):
	 """Create a new instance of BaseModel"""
	if not arg:
		print("** class name missing **")
		return None
	elif (arg not in self.level):
		print("** class doesn't exits **")
		return None
	else:
		inst = eval(line + "()")
		inst.save()
		print(inst.id)
    def do_show(self, arg):
	"""Prints the string representation of an
	instance based on the class name and id"""
	val = arg.split()
	if not arg:
		print("** class name missing **")
		return None
	elif (val[0] not in self.level):
		print("** class doesn't exist **")
		return None
	elif len(val) == 1
		print("** instance id missing **")
		return None
	else:
		key = "{}.{}".format(val[0], val[1])
		if key not is storage.all().keys():
			print("** no instance found **")
		else:
			obj = storage.all()
			print(obj[key])

    def do_destroy(self, arg):
	"""Deletes an instance based on the class name and id"""
        val = arg.split()
        if not arg:
            print("** class name missing **")
            return None
        elif (val[0] not in self.level):
            print("** class doesn't exist **")
            return None
        elif len(val) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(val[0], val[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()
    def do_all(self, arg):
	 """Prints all string representation of
        all instances based or not on the class name"""
        val = arg.split()
        obj_list = []
        if len(val) == 0:
            for value in storage.all().values():
                obj_list.append(value.__str__())
            print(obj_list)
        elif (val[0] not in self.level):
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if val[0] in key:
                    obj_list.append(storage.all()[key].__str__())
                else:
                    return
            print(obj_list)

    def do_update(self, arg):
	 """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        val = arg.split()
        if len(val) == 0:
            print("** class name missing **")
        elif (val[0] not in self.level):
            print("** class doesn't exist **")
        elif len(val) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(val[0], val[1])
            if (key not in obj):
                print("** no instance found **")
            elif len(val) == 2:
                print("** attribute name missing **")
            elif len(val) == 3:
                print("** value missing **")
            else:
                # cast to the attribute type
                # arg_type = type(eval(n[3]))
                # attr = n[3].strip('\'\"')
                setattr(obj[key], val[2], val[3])
                storage.save()

    def do_count(self, arg):
	 """ retrieve the number of instances of a class """
        count = 0
        for key in storage.all().keys():
            if arg in key:
                count += 1
        print(count)

    def default(self, arg):
	 """ Retrieve instances based on methods, i.e. <class name>.all() """
        n = line.split('.')
        inst = n[0]
        if n[1] == "all()":
            self.do_all(inst)
        elif n[1] == "count()":
            self.do_count(inst)
        elif n[1].startswith('show'):
            idsp = n[1].split('"')
            # BaseModel valid_id, idsp[1] to get the id
            line = inst + ' ' + idsp[1]
            self.do_show(line)
        elif n[1].startswith('destroy'):
            idsp = n[1].split('"')
            line = inst + ' ' + idsp[1]
            self.do_destroy(line)
        elif n[1].startswith('update'):
            sp = n[1].split('"')
            line = inst + ' ' + sp[1] + ' ' + sp[3] + ' ' + sp[5]
            self.do_update(line)
    def do_quit(self, arg):
	"""Quit command to exit the program\n"""
	return True
        sys.exit(1)

    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")

if __name__ == '__main__':
	HBNBCommand().cmdloop()
