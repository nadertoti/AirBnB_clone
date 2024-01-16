#!/usr/bin/python3
'''console of AirBnB project'''
import cmd
import json
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    '''HBNB Command'''
    prompt = ('(hbnb) ')

    def do_quit(self, args):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, args):
        '''EOF command to exit the program'''
        print()
        return True

    def emptyline(self):
        '''executes nothing'''
        pass

    def do_create(self, args):
        """create instance in basemodel class"""
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """print all instance in repo."""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = args[0] + '.' + args[1]
            print(storage.all()[key])
        except NameError:
            print("** class doesn't exist **")
            return


    def do_destroy(self, args):
        """delete all instance in repo console."""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = args[0] + '.' + args[1]
            del storage.all()[key]
            storage.save()
        except NameError:
            print("** class doesn't exist **")
            return

    def do_all(self, args):
        """output all repo instance."""
        list_obj = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    list_obj.append(val)
            else:
                list_obj.append(val)

        print(list_obj)

    def do_update(self, args):
        """update file storage."""
        storage = FileStorage()
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop() 
