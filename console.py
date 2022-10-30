#!/usr/bin/python3
"""
Module console.py defines entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter HBNBCommand class
    Methods:
        def precmd(self, arg)
        def help_help(self)
        def emptyline(self)
        def do_count(self, cls_name)
        def do_quit(self, line)
        def do_EOF(self, line)
    """

    prompt = "(hbnb) "

    class_name = ['BaseModel', 'User', 'Amenity',
                  'Place', 'City', 'State', 'Review']

    commands = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """Parses inputted command arguments"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in self.class_name and cnd[0] in self.commands:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Prints description of help command"""
        print("Provides description of a given command")

    def emptyline(self):
        """Do not execute anything when empty line"""
        pass

    def do_count(self, cls_name):
        """Counts the number of instances of a given class"""
        count = 0
        all_objs = storage.all()
        for key, value in all_objs.items():
            clss = key.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
