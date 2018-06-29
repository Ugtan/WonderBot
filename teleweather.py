import requests
from terminaltables import GithubFlavoredMarkdownTable as GFMT


def res(url):
    """ To ping the website using the url for information"""

    response = requests.get(url)
    data = response.json()
    return data


def location():
    """ To find the location of the current user using his ip address"""
    url = 'https://ipinfo.io/'
    data = res(url)
    city = data['city']
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    return latitude,longitude


def get_weather():
    """ To find the weather of that current location"""
    lat,lon = location()
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=d5cba1979a99f72e6014b8127038248c&units=metric'.format(lat, lon)
    table_data = ["temp", "humidity", "pressure", "wspeed", "wdegree", "longitude", "latitude", "desc", "city"]
    data = res(url)
    temp = data['main']['temp']
    humidity= data['main']['humidity']
    pressure = data['main']['pressure']
    wspeed = data['wind']['speed']
    wdegree = data['wind']['deg']
    longitude = data['coord']['lon']
    latitude = data['coord']['lat']
    desc = data['weather'][0]['description']
    city = data['name']
    return temp, humidity, pressure, wspeed, wdegree, longitude, latitude, desc, city


def handle_tables(table_data: list):
    """Creates a table for all the list data is passed to it
        :table_data: Data in a list format.
    """
    table = GFMT(table_data)
    table.inner_row_border = True
    table = table = "<pre>{}</pre>".format(table.table)
    return table
