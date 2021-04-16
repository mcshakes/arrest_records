from bs4 import BeautifulSoup
import requests
import csv
import os
import pandas as pd

from utils.date import format_date
from typing import Dict, List, Tuple


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

    cells = []

    for row in soup.find_all("tr"):

        arrest = ()
        offenses = []

        try:
            if not row.attrs:
                row_data = row.find(
                    "div", attrs={"class": "tdspace"}).text.split("\r\n")

                row_data = [x.strip() for x in row_data]
                data = [x for x in row_data if len(x.strip()) > 0]

                offense = data[0].split(": ")[1]
                bail_amount = data[2]

                offense_data = (offense, bail_amount)
                offenses.append(offense_data)

                cells.append(offenses)

            if row["class"] is not None and row["class"][0] == 'graybkgd':

                row_data = row.find(
                    "div", attrs={"class": "tdspace"}).text.split("\r\n")

                row_data = [x.strip() for x in row_data]
                data = [x for x in row_data if len(x.strip()) > 0]

                arrest = arrest_details(data)
                cells.append(arrest)

        except KeyError:
            pass

    write_csv(cells, date)


def write_csv(date: str):
    # File = open(date, "x", newline = "")
    # print("date", date)
    # print(os.getcwd())
    filename = format_date(date)
    cities = pd.DataFrame([['Sacramento', 'California'], [
                          'Miami', 'Florida']], columns=['City', 'State'])

    cities.to_csv(filename)
    # with open("12/221/2.csv", 'w') as out:
    # csv_out = csv.writer(out)
    # csv_out.writerow(['booking', 'name', 'arrest_date', 'arrest_time',
    #                   'arrest_agency', 'offence | bail'])

    # for row in data:
    #     # import code
    #     # code.interact(local=dict(globals(), **locals()))
    #     new_row = row

    #     if type(row) is list:
    #         offenses = [" | ".join(x) for x in row]
    #         File = open(date, "ab")
    #         File.write(offenses)

    #     csv_out.writerow(new_row)


def arrest_details(data: List[str]) -> Tuple[str, str, str, str, str]:

    booking_id = data[2].split(": ")[1]

    name = data[0].split("arrested:")[0].strip()
    date_time = [time.strip()
                 for time in data[0].split("arrested:")[1].split("at")]

    date = date_time[0]
    time = date_time[1]

    arresting_agency = data[1].split(": ")[1]

    booking_number = data[2].split(": ")[1]

    return (booking_id, name, date, time, arresting_agency)


initial_date = "02/14/06"
# get_data(initial_date)
write_csv(initial_date)
