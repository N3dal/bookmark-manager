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
from webbrowser import open_new_tab
from webbrowser import open_new as open_new_window
import json
from time import ctime
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
    return 0


def read_file_data():
    """get the websites data from json file."""

    # first check out if the file exist or not.
    if Tools.websites_data_exist():
        # add error handling here.
        with open(Constants.WEBSITES_DATA_FILE_PATH+"/"+Constants.WEBSITES_DATA_FILE_NAME, "r") as file:
            return json.load(file)

    # if file not exist:
    return -1


def write_data_to_file(url_alias: str, url_link: str):
    """write data for example new websites,
    and other data to the json file."""

    # first we have to get all the data from the file.
    data_dict = read_file_data()

    # now append the new data:
    new_data = {url_alias: [url_link, ctime()]}

    # now add the new data with all the old data.
    data_dict.update(new_data)

    # now dump-out all the data to the json file,
    # notice that if the file is not exist then,
    # this lines will create one.
    with open(Constants.WEBSITES_DATA_FILE_PATH+"/"+Constants.WEBSITES_DATA_FILE_NAME, "w") as file:
        json.dump(data_dict, file)


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
    # and make sure to remove spaces.
    url = url.lower().strip()

    # make sure to remove all "//"
    url = url.replace(":", "##")

    # first remove all "https" and "http".
    url_parts = filter(lambda part: part not in (
        "http", "https"), url.split("//"))

    url = "".join(url_parts)

    # now remove all the colon's.
    url_parts = filter(lambda part: part not in (
        "http", "https"), url.split("##"))

    url = "".join(url_parts)

    # second remove all "www"
    url_parts = filter(lambda part: part not in ("www",), url.split("."))

    url = ".".join(url_parts)

    return f"https://www.{url}"


def url_end_check(url: str, ends: tuple = ("com", "org", "net"), default_end: int = 0):
    """checkout if the website contain a one of those,
    ends: (com, org, net) or the ends that the user provides,
    and add the default end if its not exist in the url."""

    # make sure that the default end don't go out of,
    # the ends tuple range.
    default_end %= len(ends)

    if url[-3:] in ends:
        return url

    return f"{url}.{ends[default_end]}"


def url_check(url):
    """checkout of the url and fix missing prefix and ends."""

    return url_end_check(check_missing_prefix(url))


def get_user_input():
    """get the url and the url alias from the user."""

    print("Press to enter to get back")
    usr_input_url = input("Enter URL: ").strip().lower()

    # Guard-Condition.
    # make sure that the user input is not empty,
    # if its empty that means the user want to get out.
    if not usr_input_url:
        # the user want to exit, simply out want to go back.
        # so end the function and we not need to the url-alias,
        # because in the first place we don't get the url.
        return 0, 0

    usr_input_url_alias = input("Enter URL Alias: ").strip()

    # Guard-Condition.
    if not usr_input_url_alias:
        # add default alias if the user didn't give us one.
        # by the using of the url that user give us we will,
        # create an alias from that url.
        usr_input_url_alias = create_default_alias(usr_input_url)

    return usr_input_url, usr_input_url_alias


def create_default_alias(url: str):
    """create a default alias from the url"""

    # first add the https and com or net or any end.
    url = url_check(url)

    # and make sure to remove the first item and the last one,
    # form the list.
    # ex:
    # https://keep.google.com
    # from that url we need only the 'keep' and 'google',
    # and join them using any char you want, to create default alias.
    url_name = url.split('.')[1:-1]

    return "-".join(url_name)


# "Add new website",
# "Show all websites",
# "Edit websites data",
# "Show program Log",
# "Quit"

def add_new_website():
    """let the users enter there favorite websites."""

    url_link, url_alias = get_user_input()

    if not url_link:
        # if the user didn't give us any thing.
        return 0

    else:
        write_data_to_file(url_alias, url_link)


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
