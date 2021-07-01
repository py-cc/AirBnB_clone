#!/usr/bin/python3
"""
Console - Module
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
from models.engine.file_storage import FileStorage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Class
    """
    prompt = '(hbnb) '
    file = None

    classes = ['BaseModel', 'User']

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
        """args = arg.split()
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
            print("** no instance found **")"""
        args = arg.split()
        _id = False
        if bool(arg) is False:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            storage.reload()
            all_objs = storage.all()
            search = args[0]+'.'+args[1]
            for key, value in all_objs.items():
                if key == search:
                    print(value)
                    _id = True
                    break
            if _id is False:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        _id = False
        if bool(arg) is False:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            search = args[0] + '.' + args[1]
            for key, value in all_objs.items():
                if key == search:
                    del all_objs[key]
                    storage.save()
                    _id = True
                    break
            if _id is False:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg not in self.classes and arg != "":
            print("** class doesn't exist **")
        else:
            inst_list = []
            storage.reload()
            all_objs = storage.all()
            for key, value in all_objs.items():
                inst_list.append(str(value))
            print(inst_list)

    def do_update(self, arg):
        """Updates an instance adding or updating attribute\n"""
        args = arg.split()
        myobj = None
        _id = False
        if bool(arg) is False:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            storage.reload()
            all_objs = storage.all()
            search = args[0] + '.' + args[1]
            for key, value in all_objs.items():
                if key == search:
                    myobj = value
                    _id = True
                    break
            if _id is False:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                setattr(myobj, args[2], args[3])
                myobj.save()
                """ for obj_id in all_objs.keys():
                    if obj_id == args[0] + "." + args[1]:
                        dir_obj = all_objs[obj_id].to_dict()
                        if args[2] not in dir_obj.keys():
                            setattr(all_objs[obj_id], args[2], eval(args[3]))
                        else:
                            dir_obj[args[2]] = eval(args[3])
                        all_objs[obj_id] = dir_obj
                        storage.save()
                        break """

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
        """Execute nothing when there's not command"""
        pass

    def close(self):
        """Close method"""
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
