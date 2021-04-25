from typing import Dict, List, Tuple
from utils.date import format_date
from utils.chromedriver import configure_chrome_driver
from bs4 import BeautifulSoup
import requests
import csv
import os
import pandas as pd
import time


def select_date(driver, date: str):
    driver.get(url)
    WebDriverWait(driver, 3).until(
        lambda s: s.find_element_by_id("arrestedtable").is_displayed()
    )

    return BeautifulSoup(driver.page_source, 'html.parser')


def get_soup(driver, url: str):

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    LANGUAGE = "en-US,en;q=0.5"

    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    html = requests.get(url)

    # content = html.content
    # return BeautifulSoup(content, 'html.parser')


def get_data(date: str):
    url = f"https://www.weldsheriff.com/apps1/dailyArrests/index.cfm?date_booked={date}"

    webdriver = configure_chrome_driver()

    select_date(webdriver, date)

    soup = get_soup(webdriver, url)

    # soup = get_soup(url)

    cells = []
    individuals = 0

    for row in soup.find_all("tr"):
        arrest = ()

        try:
            if not row.attrs:

                row_data = row.find(
                    "div", attrs={"class": "tdspace"}).text.split("\n")

                row_data = [x.strip() for x in row_data]
                data = [x for x in row_data if len(x.strip()) > 0]

                offense = data[0].split(": ")[1]
                bail_amount = data[2]

                offense_data = (offense, bail_amount)
                offense_data = offense_data

                cells[individuals - 1]["offenses"].append(offense_data)

            if row["class"] is not None and row["class"][0] == 'graybkgd':

                row_data = row.find(
                    "div", attrs={"class": "tdspace"}).text.split("\n")

                row_data = [x.strip() for x in row_data]
                data = [x for x in row_data if len(x.strip()) > 0]

                arrest = arrest_details(data)

                cells.append(arrest)
                individuals += 1

        except KeyError:
            pass

    write_csv(cells, date)


def write_csv(data, date: str):

    filename = format_date(date)

    # arrests = pd.DataFrame(data, columns=('booking', 'name', 'arrest_date', 'arrest_time',
    #                                       'arrest_agency', 'offences | bail'))
    arrests = pd.DataFrame.from_dict(data)
    arrests.to_csv(filename)


def arrest_details(data: List[str]) -> Tuple[str, str, str, str, str]:

    booking_id = data[2].split(": ")[1]

    arrested = data[0].split("arrested:")[0].strip()
    date_time = [time.strip()
                 for time in data[0].split("arrested:")[1].split("at")]

    a_date = date_time[0]
    a_time = date_time[1]

    arresting_agency = data[1].split(": ")[1]

    booking_number = data[2].split(": ")[1]

    return {"booking_id": booking_id, "name": arrested, "date": a_date, "time": a_time, "agency": arresting_agency, "offenses": []}


initial_date = "02/14/06"
get_data(initial_date)

# Show up at site
#start date loop
# Enter date in thing
# click search
# send site data to soup
# scrape and save
