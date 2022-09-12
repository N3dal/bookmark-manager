"""
Contain all the tools needed for this project.
"""
from os import name as OS_NAME
from os import (system, listdir)


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

    @staticmethod
    def draw_box(*items, menu: bool = False):
        """use this function to draw boxes,
        for menu or for websites.
        menu:
            responsible of setup the items index,
            either adding zero before the number or not,
            depending on the box type,
            if its for menu so we not need to zero,
            or box for show data so we probably need,
            some zero laying around.
        """

        # make sure to clear at first.
        Tools.clear()

        # note:
        # i use some special unicode chars,
        # link for this special uni-codes:
        # https://en.wikipedia.org/wiki/Box-drawing_character

        TOP_LEFT_PIPE = "┌"
        TOP_RIGHT_PIPE = "┐"

        BOTTOM_LEFT_PIPE = "└"
        BOTTOM_RIGHT_PIPE = "┘"

        HORIZONTAL_LINE = "─"
        VERTICAL_LINE = "│"

        index = 0
        for _ in range(len(items)//2):

            for _ in range(2):
                print(TOP_LEFT_PIPE, HORIZONTAL_LINE *
                      60, TOP_RIGHT_PIPE, sep='', end='')
            print()

            for _ in range(2):
                # add zero-fill or not depending on the menu argument.
                string_index_item = str(
                    index+1).zfill(2) if not menu else str(index+1)

                # adding menu is like adding '1' in case if menu==True,
                # else is like adding zero, and we do that because,
                # if we remove the zero's we get a missing space,
                # and this will make one of our vertical_line get back,
                # so add one space to fill that zero place,
                # and if we have a zero so we not need to fill that place.
                print(VERTICAL_LINE, f"[{string_index_item}]",
                      items[index].center(53+menu), VERTICAL_LINE, end='')
                index += 1
            print()

            for _ in range(2):
                print(BOTTOM_LEFT_PIPE, HORIZONTAL_LINE *
                      60, BOTTOM_RIGHT_PIPE, sep='', end='')
            print()

        if len(items) % 2:
            # add extra column.
            # note i use spaces for better control.
            SHIFT = 30
            print(' '*SHIFT, TOP_LEFT_PIPE, HORIZONTAL_LINE *
                  60, TOP_RIGHT_PIPE, sep='')

            print(' '*(SHIFT-1), VERTICAL_LINE, f"[{str(index+1).zfill(2)}]",
                  items[index].center(53), VERTICAL_LINE)

            print(' '*SHIFT, BOTTOM_LEFT_PIPE, HORIZONTAL_LINE *
                  60, BOTTOM_RIGHT_PIPE, sep='')
            # print('\t')

    @staticmethod
    def websites_data_exist():
        """checkout if the websites-data file is exist or not.
        return True if the data is exist other wise it return False."""

        return Constants.WEBSITES_DATA_FILE_NAME in listdir(Constants.WEBSITES_DATA_FILE_PATH)


class Constants:
    """all the constants that project needs to work"""

    # create program DEFAULTS:

    WEBSITES_DATA_FILE_NAME = "websites_data.json"

    WEBSITES_DATA_FILE_PATH = "./"

    PROGRAM_NAME = "Simple Bookmark Manager"

    PROGRAM_OPTIONS = (
        "Add new website",
        "Show all websites",
        "Edit websites data",
        "Show program Log",
        "Quit"
    )


class ErrorMsg:
    """"""

    def __init__(self, msg="Error!"):
        self.msg = msg

    def __repr__(self):
        return f"ErrorMsg('{self.msg}')"

    def eprint(self):
        """print the error msg on terminal."""
        print(self.msg)
        # now wait for the user to press Enter.
        input("Press Enter to Continue")

        return None
