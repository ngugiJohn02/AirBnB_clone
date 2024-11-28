#!/usr/bin/python3
import cmd
from models import storage  # Import the storage instance
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB objects."""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()  # Dynamically create an instance of the given class
            storage.new(obj)  # Save the new object in storage
            storage.save()  # Persist storage to file
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Displays a string representation of an instance."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        print(obj if obj else "** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the interpreter."""
        return True

    def do_EOF(self, arg):
        """Handles EOF (Ctrl+D) to exit the interpreter."""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()

