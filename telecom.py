import requests
from bs4 import BeautifulSoup


def res(url):
    """ To ping the website using the url for information"""

    response = requests.get(url)
    return response


def location():
    """ To find the location of the current user using his ip address"""

    url = 'https://ipinfo.io/'
    response = res(url)
    data = response.json()
    city = data['city']
    return city


def competitions(soup):
    """ To Find the cubing competitions"""
    my_data = []
    data = []
    try:

        ul = soup.find("ul", {"class":"list-group"})
        lis = ul.find_all("li")[1:20]
        for li in lis:
            date = li.find("span", {"class":"date"}).text
            name = li.find("div",{"class":"competition-link"}).text
            venue = li.find("div",{"class":"venue-link"}).text
            location = li.find("div",{"class":"location"}).text

            data.append([date, name, venue, location])
        for d in data:
            my_data.append(list(map(lambda x:x.strip(),d)))
        return my_data
    except AttributeError:
        pass


def get_comps():
    city = location()
    url = 'https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&region=all&search={}&state=present&year=all+years&from_date=&to_date=&delegate=&display=list'.format(city)
    response = res(url)
    soup = BeautifulSoup(response.text , "html.parser")
    return competitions(soup)

