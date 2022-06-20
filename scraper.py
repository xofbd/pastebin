import requests
from bs4 import BeautifulSoup


class PasteKeyScraper:
    """
    A class used to scrape paste keys from the pastekey.com archive page

    Attributes
    ----------
    url : str
        The url of the archive page
    archive : BeautifulSoup
        The contents of the retrieved archive page
    pastekeys : [str]
        The retrived pastekeys

    Methods
    -------
    get_pastekeys()
        Get the pastekeys from the archive page

    get_archive()
        Get the archive page as a BeautifulSoup object
    """

    def __init__(self):

        self.url = 'https://pastebin.com/archive'
        self.archive = None
        self.pastekeys = []

    def get_archive(self):
        page = requests.get(self.url)
        self.archive = BeautifulSoup(page.text, "html.parser")
        return self.archive

    def get_pastekeys(self):
        self.get_archive()
        els = self.archive.select('tr')[1:]
        self.pastekeys = []
        for el in els:
            self.pastekeys.append(el.find('a')['href'][1:])
        return self.pastekeys


if __name__ == "__main__":
    pks = PasteKeyScraper()
    print(pks.get_pastekeys())
