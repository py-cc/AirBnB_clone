#!/usr/bin/python3
"""
Console - Module
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Class
    """
    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """Creates a new instance of BaseModel\n"""
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            try:
                obj = eval(arg + "()")
                obj.save()
                print(obj.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
                return
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                dir_obj = all_objs[obj_id].to_dict()
                if dir_obj['__class__'] != args[0]:
                    print("** class doesn't exist **")
                    return
                if obj_id == args[0] + "." + args[1]:
                    print(all_objs[obj_id])
                    return
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        self.close()
        quit()
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        self.close()
        quit()
        return True

    def emptyline(self):
        pass

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
