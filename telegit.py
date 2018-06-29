import requests
import json
from bs4 import BeautifulSoup
from terminaltables import GithubFlavoredMarkdownTable as GFMT


def get_contributions(url):
    """To get github contributions """
    my_data = []
    counter = 0
    total = 0
    header = ["S.No", "Date", "Count"]
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    rangles = soup.find_all("rect")
    for rangle in rangles:
        if rangle.get('data-count') != "0":
            date = rangle.get('data-date')
            count = rangle.get('data-count')
            total = total + int(count)
            counter += 1
            my_data.append([counter, date, count])
    print(Color("\nYour Github Contributions: \n"))
    print(tabulate(my_data, headers=header, tablefmt="fancy_grid"))
    print(Color("\nTotal Contributions : %d  \n" % total))


def get_repos(url):
    """ To get the total number of repos user has"""
    response = requests.get(url)
    data = response.text
    data = json.loads(data)
    my_data = []
    my_data.append(["S.No", "Repostitory"])

    for count, repos in enumerate(range(len(data)), 1):
        my_data.append([count, data[repos]['name']])

    table = handle_tables(my_data)
    return table


def get_starred(url):
    """ To get user's starred repos"""
    response = requests.get(url)
    data = response.text
    data = json.loads(data)
    my_data = []
    my_data.append(["S.No", "Starred Repository", "Owner of Repo"])

    for count, starred in enumerate(range(len(data)), 1):
        Srepo, owner = data[starred]['full_name'].split('/')
        my_data.append([count, Srepo, owner])
    table = handle_tables(my_data)
    return table


def handle_tables(table_data: list):
    """Creates a table for all the list data is passed to it
        :table_data: Data in a list format.
    """
    table = GFMT(table_data)
    table.inner_row_border = True
    table = table = "{}".format(table.table)
    return table
