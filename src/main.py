from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv
import pandas as pd


def get_soup(url: str):
    """Constructs and returns a soup using the HTML content of URL variable"""

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    LANGUAGE = "en-US,en;q=0.5"

    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    html = requests.get(url)
    content = html.content
    return BeautifulSoup(content, 'html.parser')


def get_data(date: str):
    url = f"https://www.weldsheriff.com/apps1/dailyArrests/index.cfm?date_booked={date}"

    soup = get_soup(url)

    data = []
    for row in soup.find_all("tr"):
        import code
        code.interact(local=dict(globals(), **locals()))

        # name = row.find("span", attrs={"class": "boldtextSmall"}).text

        row_data = row.find(
            "div", attrs={"class": "tdspace"}).text.split("\r\n")

        row_data = [x.strip() for x in row_data]
        data = [x for x in row_data if len(x.strip()) > 0]


initial_date = "02/14/06"
get_data(initial_date)
