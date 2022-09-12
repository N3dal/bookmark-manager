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
from tools import *
from url import Url
from websites_data import WebsitesData
from sys import exit


# TODO: split the script into small-scripts. => separated files.
# TODO: make sure to remove duplicate urls and assign them to different aliases names,
# TODO: for example ("www.github.com", ("github", "ghub", "git")).


Tools.clear()


def main_menu():
    """draw the main menu that will have,
    all the program options."""

    # first wipe the terminal screen.

    while True:
        Tools.clear()

        Tools.draw_box(*Constants.PROGRAM_OPTIONS, menu=True)

        usr_option = input(": ").strip().lower()

        if usr_option not in "12345":
            # if the user give us wrong option.
            continue

        elif not usr_option:
            # if we get an empty string.
            continue

        else:
            # if we get any of the option above,
            # that in the program_option tuple.
            option_call(usr_option)


def option_call(option: str):
    """call the function for the selected option."""

    functions = (
        add_new_website,
        show_all_websites,
        edit_websites_data,
        show_program_log,
        _quit
    )

    # make sure to clear the table.
    Tools.clear()
    functions[int(option)-1]()

    # now end the function.
    return None


def read_file_data():
    """get the websites data from json file."""

    # first check out if the file exist or not.
    if Tools.websites_data_exist():
        # add error handling here.
        with open(Constants.WEBSITES_DATA_FILE_PATH+"/"+Constants.WEBSITES_DATA_FILE_NAME, "r") as file:
            return json.load(file)

    # if file not exist:
    return -1


def write_data_to_file(url: Url):
    """write data for example new websites,
    and other data to the json file."""

    # first we have to get all the data from the file.
    data_dict = read_file_data()

    # now append the new data:
    new_data = {url.url_alias: [url.url, url.create_date]}

    # now add the new data with all the old data.
    data_dict.update(new_data)

    # now dump-out all the data to the json file,
    # notice that if the file is not exist then,
    # this lines will create one.
    with open(Constants.WEBSITES_DATA_FILE_PATH+"/"+Constants.WEBSITES_DATA_FILE_NAME, "w") as file:
        json.dump(data_dict, file)


def get_user_input():
    """get the url and the url alias from the user."""

    print("Press enter to get back")
    usr_input_url = input("Enter URL: ").strip().lower()

    # Guard-Condition.
    # make sure that the user input is not empty,
    # if its empty that means the user want to get out.
    if not usr_input_url:
        # the user want to exit, simply out want to go back.
        # so end the function and we not need to the url-alias,
        # because in the first place we don't get the url.
        return "", ""

    usr_input_url_alias = input("Enter URL Alias: ").strip()

    # Guard-Condition.
    if not usr_input_url_alias:
        # add default alias if the user didn't give us one.
        # by the using of the url that user give us we will,
        # create an alias from that url.
        usr_input_url_alias = Url.create_default_alias(usr_input_url)

    return usr_input_url, usr_input_url_alias


# "Add new website",
# "Show all websites",
# "Edit websites data",
# "Show program Log",
# "Quit"

def add_new_website():
    """let the users enter there favorite websites."""

    url = Url(*get_user_input())
    # url_link, url_alias = get_user_input()

    if not url.url:
        # if the user didn't give us any thing.
        return 0

    else:
        write_data_to_file(url)


def show_all_websites():
    """show all the password that available in the json data-file."""

    # get the data from the json file.
    websites_data = read_file_data()

    # all the dict-keys are the aliases for the websites.
    # so first we have to get all the aliases.
    url_aliases = websites_data.keys()

    # second get all the links from the dict-value,
    # notice that we store the link and adding-date,
    # as list so the first item from the list is the link.
    url_links = [link[0] for link in websites_data.values()]

    while True:
        # keep showing the table until user enter ['q', 'quit'].
        Tools.draw_box(*url_aliases)

        usr_input = input(
            "Enter website number to open it add w to open it in new-window,\nor enter [q]uit to go back to the main-menu: ").lower().strip()

        # get all the args the user pass.
        usr_args = usr_input.split()

        if usr_input in ("q", "quit"):
            # go back to the main-menu.
            break

        elif not usr_input:
            # if the user give us an empty string.
            continue

        elif usr_args[0].isdecimal():
            # if the user want to open one of the websites.
            usr_number_choice = int(usr_args[0])
            # first make sure if the number is in the right range.
            if usr_number_choice not in range(len(url_links)+1):
                error_msg()

            else:
                # and make sure to remove one from the user_number_choice,
                # because the index start from the zero.
                # check out if the user args contain 'w',
                # if then open the url in new window.
                open_in_new_window = 'w' in usr_args

                open_url_in_browser(
                    url_links[usr_number_choice-1], open_in_new_window)
        else:
            # any unwanted input.
            error_msg()


def edit_websites_data():
    """"""

    print("edit websites")
    input()


def show_program_log():
    """"""

    print("program log")
    input()


def _quit():
    """"""
    exit()


def error_msg():
    """just a simple error msg for wrong user input"""
    print("Error the Number is Out-of-Range!!!, press any key to continue: ")
    input()


def main():

    # url = url_check("www.google")

    # print(url)

    # Tools.draw_box(*Tools.Constants.)
    main_menu()

    # url = create_default_alias("https://keep.google.com")
    # print(url)


if __name__ == "__main__":
    main()
