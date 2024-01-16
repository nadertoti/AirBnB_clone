#!/usr/bin/python3
'''the console of the AirBnB project'''
import cmd
import json
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instances"""
        args = shlex.split(arg)
        instances = []
        if not arg:
            for key, value in storage.all().items():
                instances.append(str(value))
            print(instances)
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == args[0]:
                    instances.append(str(value))
            print(instances)

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + '.' + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj = storage.all()[key]
                    attr_name = args[2]
                    attr_value = args[3]
                    setattr(obj, attr_name, eval(attr_value))
                    obj.save()

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
