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
        self.url = url
        self.url_alias = url_alias
        self.create_date = ctime()

        Url.all_urls.append(self)

    def __repr__(self):
        return f"Url('{self.url}', '{self.url_alias}')"

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


url1 = Url("www.keep.google.com", "google-keep")

print(url1.export_2_json())