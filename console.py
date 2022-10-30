#!/usr/bin/python3
"""
Module console.py defines entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter HBNBCommand class
    Methods:
        def precmd(self, arg)
        def help_help(self)
        def emptyline(self)
        def do_count(self, cls_name)
        def do_create(self, model_type)
        def do_show(self, arg)
        def do_destroy(self, arg)
        def do_all(self, arg)
        def do_update(self, arg)
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
        """Prints description of help command"""
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

    def do_create(self, model_type):
        """Creates an instance of a given class, saves it (JSON file)
         and prints the id"""

        if not model_type:
            print("** class name missing **")
        elif model_type not in self.class_name:
            print("** class doesn't exist **")
        else:
            model_dict = {'BaseModel': BaseModel, 'User': User}
            my_model = model_dict[model_type]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
         class name and id"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
         (changes are saved into the JSON file)"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints string representation of all instances based or not
         on the class name"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in self.class_name:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                if obj_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
         updating attribute (changes saved into the JSON file)"""

        if not arg:
            print("** class name missing **")
            return

        quote = ""
        for argv in arg.split(','):
            quote = quote + argv

        args = shlex.split(quote)

        if args[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
