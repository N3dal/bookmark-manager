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
from os import (system, listdir)
from webbrowser import open_new_tab
from webbrowser import open_new as open_new_window
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

# create program DEFAULTS.
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


def is_exist():
    """checkout if the websites-data file is exist or not."""

    return WEBSITES_DATA_FILE_NAME in listdir(WEBSITES_DATA_FILE_PATH)


def read_file_data():
    """get the websites data from json file."""

    # first check out if the file exist or not.
    if is_exist():

        with open(WEBSITES_DATA_FILE_PATH+"/"+WEBSITES_DATA_FILE_NAME, "r") as file:
            return json.load(file)

    # if file not exist:
    return -1


def open_url_in_browser(url: str, open_in_new_window: bool = False):
    """open the given link using your default browser,
    in new window if you want or on new tab."""

    if open_in_new_window == True:
        # open the link on new window.
        open_new_window(url)

    else:
        # open the link on new tab,
        # the default.
        open_new_tab(url)


def check_missing_prefix(url: str):
    """check out from user input and make sure if the user forget,
    adding 'www' or 'https:// | http://' this function will edit,
    the string and add the missing ones and return it,
    as new value."""

    # note: make sure to save the website in,
    # lower-case.
    # so first we have to lower-case the url.

    url = url.lower()

    if url.startswith("https://") or url.startswith("http://"):
        # if the website contain either ("https://", "http://").

        return url

    else:
        # add either ("https://", "http://"), the default,
        # one that i select is "https://".

        return f"https://{url}"


def main():

    url = check_missing_prefix("https://https://www.google.com")

    print(url)


if __name__ == "__main__":
    main()
