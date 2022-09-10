"""
Contain all the tools needed for this project.
"""
from os import name as OS_NAME
from os import system


class Tools:
    """tools needed for this project."""

    @staticmethod
    def clear():
        """wipe the terminal screen."""

        if OS_NAME == "posix":
            # for *nix machines.
            system("clear")

        elif OS_NAME == "windows":
            system("cls")

        else:
            # for all other os in the world.
            # system("your-command")
            pass

        return None
