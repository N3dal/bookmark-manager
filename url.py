"""
Url type to deal with storing urls.
"""
from webbrowser import open_new_tab
from webbrowser import open_new as open_new_window
from time import ctime


class Url:
    """"""

    # to store all the urls.
    all_urls = []

    def __init__(self, url: str, url_alias=""):
        self.url = Url.url_check(url)
        self.url_alias = url_alias
        self.create_date = ctime()

        Url.all_urls.append(self)

    def __repr__(self):
        return f"Url('{self.url}', '{self.url_alias}')"

    @staticmethod
    def url_check(url: str, default_url_end=0):
        """
        fix missing prefixes if its exist after checking out from user input,
        and make sure if the user forget,
        adding 'www' or 'https:// | http://' this function will edit,
        the string and add the missing ones and return it,
        as new value, and checkout if the website contain a one of those,
        ends: (com, org, net) or the ends that the user provides,
        and add the default end if its not exist in the url.
        """

        URL_ENDS = (
            "com",
            "org",
            "net"
        )

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

        if url[-3:] not in URL_ENDS:
            url = f"{url}.{URL_ENDS[default_url_end]}"

        return f"https://www.{url}"

    def open_in_browser(self, open_in_new_window=False):
        """
        open url using your default browser
        return True if everything going fine other wise its return False
        to open the url in new window change 'open_in_new_window' to True.
        """

        if open_in_new_window:
            # open the url on new window.
            open_new_window(self.url)

        else:
            # open the url in new tab.
            open_new_tab(self.url)

        return True

    def create_default_alias(url: str):
        """create an alias name for the url from the url name."""
        pass

    def export_2_json(self):
        """
        export the url data to json file,
        that's include (url_alias, url, create_date).
        """

        return {self.url_alias: [self.url, self.create_date]}


url1 = Url("amazon.net", "google-keep")

print(url1.export_2_json())
