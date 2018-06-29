import requests
from bs4 import BeautifulSoup


def scrape(url):
    """ To Fetch data from url """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def top_stories(soup):
    """ To find the Top Stories using soup object """
    data = []
    ltags = soup.find("ul", {"class":"itg-listing"}).find_all("li")
    for ltag in ltags:

        atags = ltag.find("a")
        if atags.get("title") != "Contest":
            title = atags.get("title")
            data.append(title)
    return data


def get_news():

    url = 'https://www.indiatoday.in/'
    soup = scrape(url)
    return top_stories(soup)

def handle_tables(table_data: list):
    """Creates a table for all the list data is passed to it
        :table_data: Data in a list format.
    """
    table = GFMT(table_data)
    table.inner_row_border = True
    table = table = "<pre>{}</pre>".format(table.table)
    return table
