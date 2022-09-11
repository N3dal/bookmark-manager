"""
Url type to deal with storing urls.
"""
from webbrowser import open_new_tab
from webbrowser import open_new as open_new_window


class Url:
    """"""

    def __init__(self, url: str):
        self.url = url
        self.url_alias = ""

    def open_in_browser(self, open_in_new_window=False):
        """
        open url using your default browser
        return True if everything going fine other wise its return False
        to open the url in new window change 'open_in_new_window' to True.
        """

        if open_in_new_window:
            # open the url on new window.
            open_in_new_window(self.url)

        else:
            # open the url in new tab.
            open_new_tab(self.url)
