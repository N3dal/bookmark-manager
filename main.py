#!/usr/bin/python3
# -----------------------------------------------------------------
# Bookmark: program that use for storing favorite websites.
# you can add any number of websites that you want,
# and you can launch your website directly from the terminal,
# into your default web-browser.
#
#
#
# Author:N84.
#
# Create Date:Sat May  7 13:47:09 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------

from os import name as OS_NAME
from os import system
from webbrowser import (open_new, open_new_tab)
from webbrowser import open as open_web_browser
import json
import datetime


def clear():
    """wipe the terminal screen."""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()

# create the DEFAULTS.
WEBSITES_DATA_FILE_NAME = "websites_data.json"
PROGRAM_NAME = "Simple Bookmark Manager"
PROGRAM_OPTIONS = (
    "Add new website",
    "Show all websites",
    "Edit websites data",
    "Show program Log",
    "Quit"
)


def main_menu():
    """draw the main menu that will have,
    all the program options."""

    # first wipe the terminal screen.
    clear()

    print(PROGRAM_NAME.center(80, '-'))

    # print program options.
    for option_number, option_name in enumerate(PROGRAM_OPTIONS, 1):
        print(f"[{option_number}] {option_name}.".center(80))

    # now get the user input and return it.

    return input('\n'.ljust(40) + ': ').strip().lower()


def main():
    main_menu()


if __name__ == "__main__":
    main()
