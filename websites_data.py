"""
this is used to create object can deal with websites_data.json file.
"""
import json
from tools import Tools, Constants


class WebsitesData:
    """to deal with the websites_data.json data."""

    def __init__(self):
        pass

    def get_data(self):
        """get the websites data from json file."""

        # first check out if the file exist or not.
        if Tools.websites_data_exist():
            # add error handling here.
            with open(Constants.WEBSITES_DATA_FILE_PATH+"/"+Constants.WEBSITES_DATA_FILE_NAME, "r") as file:
                return json.load(file)

        # if file not exist:
        return -1

    def set_data(self, url):
        """write data for example new websites,
        and other data to the json file,
        simply out update json file websites data."""

        # first we have to get all the data from the file.
        data = self.get_data()

        # now append the new data:
        data_to_set = {url.url_alias: [url.url, url.create_date]}

        # now add the new data with all the old data.
        data.update(data_to_set)

        # now dump-out all the data to the json file,
        # notice that if the file is not exist then,
        # this lines will create one.
        with open(Constants.WEBSITES_DATA_FILE_PATH+"/"+Constants.WEBSITES_DATA_FILE_NAME, "w") as file:
            json.dump(data, file)

        return None
