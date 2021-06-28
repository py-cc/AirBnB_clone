#!/usr/bin/python3
"""
Console - Module
"""
import cmd
from models.base_model import BaseModel


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
        id = arg
        print(id)
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            try:
                if id is None or id == "":
                    print("** instance id missing **")
                    return
                for obj_id in eval(arg + ".keys()"):
                    if obj_id == id:
                        print(obj_id[id])
                        return
                print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
